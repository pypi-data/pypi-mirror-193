import logging
import warnings
from collections import OrderedDict

import numpy as np
import xarray as xr

from . import resample

logger = logging.getLogger(__name__)


def calculate_thickness(ds, top="top", bot="botm"):
    """Calculate thickness from dataset.

    Parameters
    ----------
    ds : xarray.Dataset
        dataset containing information about top and bottom elevations
        of layers
    top : str, optional
        name of data variable containing tops, by default "top"
    bot : str, optional
        name of data variable containing bottoms, by default "botm"

    Returns
    -------
    thickness : xarray.DataArray
        DataArray containing thickness information
    """
    # calculate thickness
    if ds[top].ndim == ds[bot].ndim and ds[top].ndim in [2, 3]:
        if ds[top].shape[0] == ds[bot].shape[0]:
            # top is 3D, every layer has top and bot
            thickness = ds[top] - ds[bot]
        else:
            raise ValueError("3d top and bot should have same number of layers")
    elif ds[top].ndim == (ds[bot].ndim - 1) and ds[top].ndim in [1, 2]:
        if ds[top].shape[-1] == ds[bot].shape[-1]:
            # top is only top of first layer
            thickness = xr.zeros_like(ds[bot])
            for lay in range(len(thickness)):
                if lay == 0:
                    thickness[lay] = ds[top] - ds[bot][lay]
                else:
                    thickness[lay] = ds[bot][lay - 1] - ds[bot][lay]
        else:
            raise ValueError("2d top should have same last dimension as bot")
    if isinstance(ds[bot], xr.DataArray):
        if hasattr(ds[bot], "units"):
            if ds[bot].units == "mNAP":
                thickness.attrs["units"] = "m"
            else:
                thickness.attrs["units"] = ds[bot].units

    return thickness


def layer_split_top_bot(ds, split_dict, layer="layer", top="top", bot="botm"):
    """Calculate new tops and bottoms for split layers.

    Parameters
    ----------
    ds : xarray.Dataset
        xarray Dataset containing information about layers
        (layers, top and bot)
    split_dict : dict
        dictionary with index of layers to split as keys and iterable
        of fractions that add up to 1 to indicate how to split up layer.
        E.g. {0: [0.25, 0.75]} will split layer 0 into 2 layers, with first
        layer equal to 0.25 of original thickness and second layer 0.75 of
        original thickness.
    layer : str, optional
        name of layer dimension, by default 'layer'
    top : str, optional
        name of data variable containing top of layers, by default 'top'
    bot : str, optional
        name of data variable containing bottom of layers, by default 'botm'

    Returns
    -------
    new_top, new_bot : xarray.DataArrays
        DataArrays containing new tops and bottoms after splitting layers.
    reindexer : OrderedDict
        dictionary mapping new to old layer indices.
    """

    # calculate thickness
    thickness = calculate_thickness(ds, top=top, bot=bot)

    # check if top is 2d or 3d
    top3d = ds[top].ndim == ds[bot].ndim

    # calculate new number of layers
    new_nlay = (
        ds[layer].size + sum((len(sf) for sf in split_dict.values())) - len(split_dict)
    )

    # create new DataArrays for storing new top/bot
    new_bot = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={"layer": np.arange(new_nlay), "y": ds.y.data, "x": ds.x.data},
    )
    new_top = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={"layer": np.arange(new_nlay), "y": ds.y.data, "x": ds.x.data},
    )

    # dict to keep track of old and new layer indices
    reindexer = OrderedDict()

    j = 0  # new layer index
    isplit = 0  # split layer index

    # loop over original layers
    for i in range(ds[layer].size):
        # check if layer should be split
        if i in split_dict:
            # set new top based on old top
            if top3d:
                new_top.data[j] = ds[top].data[i]
            else:
                if i == 0:
                    new_top.data[j] = ds[top].data
                else:
                    new_top.data[j] = ds[bot].data[i - 1]

            # get split factors
            sf = split_dict[i]

            # check if factors add up to 1
            if np.sum(sf) != 1.0:
                raise ValueError("Sum of split factors for layer must equal 1.0!")
            logger.debug(
                f"{i}: Split layer {i} into {len(sf)} layers with fractions: {sf}"
            )

            # loop over split factors
            for isf, factor in enumerate(sf):
                logger.debug(
                    f"  - {isf}: Calculate new top/bot for new layer index {j}"
                )

                # calculate new bot and new top
                new_bot.data[j] = new_top.data[j] - (factor * thickness[i])
                new_top.data[j + 1] = new_bot.data[j]

                # store new and old layer index
                reindexer[j] = i

                # increase new index
                j += 1

            # go to next layer to split
            isplit += 1

        # no split, remap old layer to new layer index
        else:
            logger.debug(f"{i:2d}: No split: map layer {i} to new layer index {j}")
            if top3d:
                new_top.data[j] = ds[top].data[i]
            else:
                if i == 0:
                    new_top.data[j] = ds[top].data.squeeze()
                else:
                    new_top.data[j] = ds[bot].data[i - 1]

            new_bot.data[j] = ds[bot].data[i]
            reindexer[j] = i
            j += 1

    return new_top, new_bot, reindexer


def fill_data_split_layers(da, reindexer):
    """Fill data for split layers with values from original layer.

    Parameters
    ----------
    da : xarray.DataArray or numpy.ndarray
        original array with data
    reindexer : dict
        dictionary containing mapping between new layer index and
        original layer index.

    Returns
    -------
    da_new : xarray.DataArray or numpy.ndarray
        array with filled data for split layers
    """
    if isinstance(da, xr.DataArray):
        da_new = xr.DataArray(
            data=np.nan,
            dims=["layer", "y", "x"],
            coords={
                "layer": np.arange(list(reindexer.keys())[-1] + 1),
                "y": da["y"],
                "x": da["x"],
            },
        )
        for k, v in reindexer.items():
            da_new.data[k] = da.data[v]
    elif isinstance(da, np.ndarray):
        da_new = np.zeros((list(reindexer.keys())[-1] + 1), *da.shape[1:])
        for k, v in reindexer.items():
            da_new[k] = da[v]
    else:
        raise TypeError(f"Cannot fill type: '{type(da)}'!")
    return da_new


def split_layers_ds(
    ds, split_dict, layer="layer", top="top", bot="botm", kh="kh", kv="kv"
):
    """Split layers based in Dataset.

    Parameters
    ----------
    ds : xarray.Dataset
        xarray Dataset containing information about layers
        (layers, top and bot)
    split_dict : dict
        dictionary with index of layers to split as keys and iterable
        of fractions that add up to 1 to indicate how to split up layer.
        E.g. {0: [0.25, 0.75]} will split layer 0 into 2 layers, with first
        layer equal to 0.25 of original thickness and second layer 0.75 of
        original thickness.
    layer : str, optional
        name of layer dimension, by default 'layer'
    top : str, optional
        name of data variable containing top of layers, by default 'top'
    bot : str, optional
        name of data variable containing bottom of layers, by default 'botm'
    kh : str, opti
        name of data variable containg horizontal hydraulic conductivity,
        by default 'kh'
    kv : str, optional
        name of data variable containg vertical hydraulic conductivity,
        by default 'kv'

    Returns
    -------
    ds_split : xarray.Dataset
        Dataset with new tops and bottoms taking into account split layers,
        and filled data for hydraulic conductivities.
    """

    parsed_dv = set([top, bot, kh, kv])

    dropped_dv = set(ds.data_vars.keys()) - parsed_dv
    if len(dropped_dv) > 0:
        logger.warning(f"Following data variables will be dropped: {dropped_dv}")

    # calculate new tops/bots
    logger.info("Calculating new layer tops and bottoms...")

    new_top, new_bot, reindexer = layer_split_top_bot(
        ds, split_dict, layer=layer, top=top, bot=bot
    )

    # fill kh/kv
    logger.info(f"Fill value '{kh}' for split layers with value original layer.")
    da_kh = fill_data_split_layers(ds["kh"], reindexer)
    logger.info(f"Fill value '{kv}' for split layers with value original layer.")
    da_kv = fill_data_split_layers(ds["kv"], reindexer)

    # get new layer names
    layer_names = []
    for j, i in reindexer.items():
        layercode = ds[layer].data[i]

        if layercode in layer_names:
            if isinstance(layercode, str):
                ilay = (
                    np.sum([1 for ilay in layer_names if ilay.startswith(layercode)])
                    + 1
                )
                layercode += f"_{ilay}"
            else:
                layercode = j

        layer_names.append(layercode)

    # assign new layer names
    new_top = new_top.assign_coords(layer=layer_names)
    new_bot = new_bot.assign_coords(layer=layer_names)
    da_kh = da_kh.assign_coords(layer=layer_names)
    da_kv = da_kv.assign_coords(layer=layer_names)

    # add reindexer to attributes
    attrs = ds.attrs.copy()
    attrs["split_reindexer"] = reindexer

    # create new dataset
    logger.info("Done! Created new dataset with split layers!")
    ds_split = xr.Dataset(
        {top: new_top, bot: new_bot, kh: da_kh, kv: da_kv}, attrs=attrs
    )

    return ds_split


def layer_combine_top_bot(ds, combine_layers, layer="layer", top="top", bot="botm"):
    """Calculate new tops and bottoms for combined layers.

    Parameters
    ----------
    ds : xarray.Dataset
        xarray Dataset containing information about layers
        (layers, top and bot)
    combine_layers : list of tuple of ints
        list of tuples, with each tuple containing integers indicating
        layer indices to combine into one layer. E.g. [(0, 1), (2, 3)] will
        combine layers 0 and 1 into a single layer (with index 0) and layers
        2 and 3 into a second layer (with index 1).
    layer : str, optional
        name of layer dimension, by default 'layer'
    top : str, optional
        name of data variable containing top of layers, by default 'top'
    bot : str, optional
        name of data variable containing bottom of layers, by default 'botm'

    Returns
    -------
    new_top, new_bot : xarray.DataArrays
        DataArrays containing new tops and bottoms after splitting layers.
    reindexer : OrderedDict
        dictionary mapping new to old layer indices.
    """
    # calculate new number of layers
    new_nlay = (
        ds[layer].size - sum((len(c) for c in combine_layers)) + len(combine_layers)
    )

    # create new DataArrays for storing new top/bot
    new_bot = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={"layer": np.arange(new_nlay), "y": ds.y.data, "x": ds.x.data},
    )
    new_top = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={"layer": np.arange(new_nlay), "y": ds.y.data, "x": ds.x.data},
    )

    # dict to keep track of old and new layer indices
    reindexer = OrderedDict()

    j = 0  # new layer index
    icomb = 0  # combine layer index

    # loop over original layers
    for i in range(ds.layer.size):
        # check whether to combine layers
        if i in np.concatenate(combine_layers):
            # get indices of layers
            c = combine_layers[icomb]
            # store new and original layer indices
            reindexer[j] = c
            # only need to calculate new top/bot once for each merged layer
            if i == np.min(c):
                logger.debug(
                    f"{j:2d}: Merge layers {c} as layer {j}, calculate new top/bot."
                )
                tops = ds[top].data[c, :, :]
                bots = ds[bot].data[c, :, :]
                new_top.data[j] = np.nanmax(tops, axis=0)
                new_bot.data[j] = np.nanmin(bots, axis=0)

            elif i == np.max(c):
                # advance combine layer index after merging layers
                icomb += 1
                # advance new layer index
                j += 1
                continue
            else:
                # no need to merge more than once, so continue loop
                continue
        else:
            # do not merge, only map old layer index to new layer index
            logger.debug(
                f"{j:2d}: Do not merge, map old layer index to new layer index."
            )
            new_top.data[j] = ds[top].data[i]
            new_bot.data[j] = ds[bot].data[i]
            reindexer[j] = i
            j += 1

    return new_top, new_bot, reindexer


def sum_param_combined_layers(da, reindexer):
    """Calculate combined layer parameter with sum.

    Parameters
    ----------
    da : xarray.DataArray
        data array to calculate combined parameters for
    reindexer : OrderedDict
        dictionary mapping new layer indices to old layer indices

    Returns
    -------
    da_new : xarray.DataArray
        data array containing new parameters for combined layers and old
        parameters for unmodified layers.
    """
    da_new = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={
            "layer": np.arange(list(reindexer.keys())[-1] + 1),
            "y": da["y"],
            "x": da["x"],
        },
    )

    for k, v in reindexer.items():
        if isinstance(v, tuple):
            psum = np.sum(da.data[v, :, :], axis=0)
        else:
            psum = da.data[v]
        da_new.data[k] = psum
    return da_new


def kheq_combined_layers(kh, thickness, reindexer):
    """Calculate equivalent horizontal hydraulic conductivity.

    Parameters
    ----------
    kh : xarray.DataArray
        data array containing horizontal hydraulic conductivity
    thickness : xarray.DataArray
            data array containing thickness per layer
    reindexer : OrdererDict
        dictionary mapping new layer indices to old layer indices

    Returns
    -------
    da_kh : xarray.DataArray
        data array containing equivalent horizontal hydraulic conductivity
        for combined layers and original hydraulic conductivity in unmodified
        layers
    """
    da_kh = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={
            "layer": np.arange(list(reindexer.keys())[-1] + 1),
            "y": kh["y"],
            "x": kh["x"],
        },
    )

    for k, v in reindexer.items():
        if isinstance(v, tuple):
            kheq = np.nansum(
                thickness.data[v, :, :] * kh.data[v, :, :], axis=0
            ) / np.nansum(thickness.data[v, :, :], axis=0)
        else:
            kheq = kh.data[v]
        da_kh.data[k] = kheq
    return da_kh


def kveq_combined_layers(kv, thickness, reindexer):
    """Calculate equivalent vertical hydraulic conductivity.

    Parameters
    ----------
    kv : xarray.DataArray
        data array containing vertical hydraulic conductivity
    thickness : xarray.DataArray
        data array containing thickness per layer
    reindexer : OrdererDict
        dictionary mapping new layer indices to old layer indices

    Returns
    -------
    da_kv : xarray.DataArray
        data array containing equivalent vertical hydraulic conductivity
        for combined layers and original hydraulic conductivity in unmodified
        layers
    """
    da_kv = xr.DataArray(
        data=np.nan,
        dims=["layer", "y", "x"],
        coords={
            "layer": np.arange(list(reindexer.keys())[-1] + 1),
            "y": kv["y"],
            "x": kv["x"],
        },
    )

    for k, v in reindexer.items():
        if isinstance(v, tuple):
            kveq = np.nansum(thickness.data[v, :, :], axis=0) / np.nansum(
                thickness.data[v, :, :] / kv.data[v, :, :], axis=0
            )
        else:
            kveq = kv.data[v]
        da_kv.data[k] = kveq
    return da_kv


def combine_layers_ds(
    ds,
    combine_layers,
    layer="layer",
    top="top",
    bot="botm",
    kh="kh",
    kv="kv",
    kD="kD",
    c="c",
):
    """Combine layers in Dataset.

    Parameters
    ----------
    ds : xarray.Dataset
        xarray Dataset containing information about layers
        (layers, top and bot)
    combine_layers : list of tuple of ints
        list of tuples, with each tuple containing integers indicating
        layer indices to combine into one layer. E.g. [(0, 1), (2, 3)] will
        combine layers 0 and 1 into a single layer (with index 0) and layers
        2 and 3 into a second layer (with index 1).
    layer : str, optional
        name of layer dimension, by default 'layer'
    top : str, optional
        name of data variable containing top of layers, by default 'top'
    bot : str, optional
        name of data variable containing bottom of layers, by default 'botm'
    kh : str, optional
        name of data variable containg horizontal hydraulic conductivity,
        by default 'kh'. Not parsed if set to None.
    kv : str, optional
        name of data variable containg vertical hydraulic conductivity,
        by default 'kv'. Not parsed if set to None.
    kD : str, optional
        name of data variable containg transmissivity or kD,
        by default 'kD'. Not parsed if set to None.
    c : str, optional
        name of data variable containg resistance or c,
        by default 'c'. Not parsed if set to None.

    Returns
    -------
    ds_combine : xarray.Dataset
        Dataset with new tops and bottoms taking into account combined layers,
        and recalculated values for parameters (kh, kv, kD, c).
    """

    data_vars = []
    for dv in [kh, kv, kD, c]:
        if dv is not None:
            data_vars.append(dv)
    parsed_dv = set([top, bot] + data_vars)

    dropped_dv = set(ds.data_vars.keys()) - parsed_dv
    if len(dropped_dv) > 0:
        logger.warning(f"Following data variables will be dropped: {dropped_dv}")

    # calculate new tops/bots
    logger.info("Calculating new layer tops and bottoms...")

    da_dict = {}

    new_top, new_bot, reindexer = layer_combine_top_bot(
        ds, combine_layers, layer=layer, top=top, bot=bot
    )
    da_dict[top] = new_top
    da_dict[bot] = new_bot

    # calculate original thickness
    thickness = calculate_thickness(ds, top=top, bot=bot)

    # calculate equivalent kh/kv
    if kh is not None:
        logger.info(f"Calculate equivalent '{kh}' for combined layers.")
        da_dict[kh] = kheq_combined_layers(ds[kh], thickness, reindexer)
    if kv is not None:
        logger.info(f"Calculate equivalent '{kv}' for combined layers.")
        da_dict[kv] = kveq_combined_layers(ds[kv], thickness, reindexer)
    if kD is not None:
        logger.info(f"Calculate value '{kD}' for combined layers with sum.")
        da_dict[kD] = sum_param_combined_layers(ds[kD], reindexer)
    if c is not None:
        logger.info(f"Calculate value '{c}' for combined layers with sum.")
        da_dict[c] = sum_param_combined_layers(ds[c], reindexer)

    # get new layer names, based on first sub-layer from each combined layer
    layer_names = []
    for _, i in reindexer.items():
        if isinstance(i, tuple):
            i = i[0]
        layercode = ds[layer].data[i]
        layer_names.append(layercode)

    # assign new layer names
    for k, da in da_dict.items():
        da_dict[k] = da.assign_coords(layer=layer_names)

    # add reindexer to attributes
    attrs = ds.attrs.copy()
    attrs["combine_reindexer"] = reindexer

    # create new dataset
    logger.info("Done! Created new dataset with combined layers!")
    ds_combine = xr.Dataset(da_dict, attrs=attrs)

    return ds_combine


def add_kh_kv_from_ml_layer_to_ds(
    ml_layer_ds, ds, anisotropy, fill_value_kh, fill_value_kv
):
    """add kh and kv from a model layer dataset to the model dataset.

    Supports structured and vertex grids.

    Parameters
    ----------
    ml_layer_ds : xarray.Dataset
        dataset with model layer data with kh and kv
    ds : xarray.Dataset
        dataset with model data where kh and kv are added to
    anisotropy : int or float
        factor to calculate kv from kh or the other way around
    fill_value_kh : int or float, optional
        use this value for kh if there is no data in the layer model. The
        default is 1.0.
    fill_value_kv : int or float, optional
        use this value for kv if there is no data in the layer model. The
        default is 1.0.

    Returns
    -------
    ds : xarray.Dataset
        dataset with model data with new kh and kv

    Notes
    -----
    some model dataset, such as regis, also have 'c' and 'kd' values. These
    are ignored at the moment
    """
    warnings.warn(
        "add_kh_kv_from_ml_layer_to_ds is deprecated. Please use update_ds_from_layer_ds instead.",
        DeprecationWarning,
    )

    ds.attrs["anisotropy"] = anisotropy
    ds.attrs["fill_value_kh"] = fill_value_kh
    ds.attrs["fill_value_kv"] = fill_value_kv

    logger.info("add kh and kv from model layer dataset to modflow model")

    kh, kv = get_kh_kv(
        ml_layer_ds["kh"],
        ml_layer_ds["kv"],
        anisotropy,
        fill_value_kh=fill_value_kh,
        fill_value_kv=fill_value_kv,
    )

    ds["kh"] = kh
    ds["kv"] = kv

    return ds


def set_model_top(ds, top, min_thickness=0.0):
    """Set the model top, changing layer bottoms when necessary as well.

    If the new top is higher than the previous top, the extra thickness is added to the
    highest layer with a thickness larger than 0.

    Parameters
    ----------
    ds : xarray.Dataset
        The model dataset, containing the current top.
    top : xarray.DataArray
        The new model top, with the same shape as the current top.

    Returns
    -------
    ds : xarray.Dataset
        The model dataset, containing the new top.
    """
    if "gridtype" not in ds.attrs:
        raise (Exception("Make sure the Dataset is build by nlmod"))
    if isinstance(top, (float, int)):
        top = xr.full_like(ds["top"], top)
    if not top.shape == ds["top"].shape:
        raise (
            Exception("Please make sure the new top has the same shape as the old top")
        )
    if np.any(np.isnan(top)):
        raise (Exception("Please make sure the new top does not contain nans"))
    # where the botm is equal to the top, the layer is inactive
    # set the botm to the new top at these locations
    ds["botm"] = ds["botm"].where(ds["botm"] != ds["top"], top)
    # make sure the botm is never higher than the new top
    ds["botm"] = ds["botm"].where(top - ds["botm"] > min_thickness, top)
    # change the current top
    ds["top"] = top
    # recalculate idomain
    ds = set_idomain(ds)
    return ds


def set_layer_top(ds, layer, top):
    """Set the top of a layer"""
    assert layer in ds.layer
    lay = np.where(ds.layer == layer)[0][0]
    if lay == 0:
        # change the top of the model
        ds["top"] = top
        # make sure the botm of all layers is never higher than the new top
        ds["botm"] = ds["botm"].where(ds["botm"] < top, top)
    else:
        # change the botm of the layer above
        ds["botm"][lay - 1] = top
        # make sure the top of the layers above is never lower than the new top
        ds["top"] = ds["top"].where(ds["top"] > top, top)
        # make sure the botm of the layers above is never higher than the new top
        ds["botm"][: lay - 1] = ds["botm"][: lay - 1].where(
            ds["botm"][: lay - 1] > top, top
        )
        # make sure the botms of lower layers are lower than top
        ds["botm"][lay:] = ds["botm"][lay:].where(ds["botm"][lay:] < top, top)
    ds = set_idomain(ds)
    return ds


def set_layer_botm(ds, layer, botm):
    """Set the bottom of a layer"""
    assert layer in ds.layer
    lay = np.where(ds.layer == layer)[0][0]
    # if lay > 0 and np.any(botm > ds["botm"][lay - 1]):
    #    raise (Exception("set_layer_botm cannot change botm of higher layers yet"))
    ds["botm"][:lay] = ds["botm"][:lay].where(ds["botm"][:lay] > botm, botm)
    ds["botm"][lay] = botm
    # make sure the botm of the layers below is never higher than the new botm
    mask = ds["botm"][lay + 1 :] < botm
    ds["botm"][lay + 1 :] = ds["botm"][lay + 1 :].where(mask, botm)
    # make sure the botm of the layers above is lever lower than the new botm

    ds = set_idomain(ds)
    return ds


def set_layer_thickness(ds, layer, thickness, change="botm"):
    """Set the layer thickness by changing the bottom of the layer"""
    assert layer in ds.layer
    assert change == "botm", "Only change=botm allowed for now"
    lay = np.where(ds.layer == layer)[0][0]
    if lay == 0:
        top = ds["top"]
    else:
        top = ds["botm"][lay - 1]
    new_botm = top - thickness
    ds = set_layer_botm(ds, layer, new_botm)
    return ds


def set_minimum_layer_thickness(ds, layer, min_thickness, change="botm"):
    """Make sure layer has a minimum thickness by lowering the botm of the layer where neccesary"""
    assert layer in ds.layer
    assert change == "botm", "Only change=botm allowed for now"
    lay = np.where(ds.layer == layer)[0][0]
    if lay == 0:
        top = ds["top"]
    else:
        top = ds["botm"][lay - 1]
    botm = ds["botm"][lay]

    mask = (top - botm) > min_thickness
    new_botm = botm.where(mask, top - min_thickness)
    ds = set_layer_botm(ds, layer, new_botm)
    return ds


def get_kh_kv(kh_in, kv_in, anisotropy, fill_value_kh=1.0, fill_value_kv=1.0):
    """create kh en kv grid data for flopy from existing kh, kv and anistropy
    grids with nan values (typically from REGIS).

    fill kh grid in these steps:
    1. take kh from kh_in, if kh_in has nan values:
    2. take kv from kv_in and multiply by anisotropy, if this is nan:
    3. take fill_value_kh

    fill kv grid in these steps:
    1. take kv from kv_in, if kv_in has nan values:
    2. take kh from kh_in and divide by anisotropy, if this is nan:
    3. take fill_value_kv

    Supports structured and vertex grids.

    Parameters
    ----------
    kh_in : np.ndarray
        kh from regis with nan values shape(nlay, nrow, ncol) or
        shape(nlay, len(icell2d))
    kv_in : np.ndarray
        kv from regis with nan values shape(nlay, nrow, ncol) or
        shape(nlay, len(icell2d))
    anisotropy : int or float
        factor to calculate kv from kh or the other way around
    fill_value_kh : int or float, optional
        use this value for kh if there is no data in kh_in, kv_in and
        anisotropy. The default is 1.0.
    fill_value_kv : int or float, optional
        use this value for kv if there is no data in kv_in, kh_in and
        anisotropy. The default is 1.0.

    Returns
    -------
    kh_out : np.ndarray
        kh without nan values (nlay, nrow, ncol) or shape(nlay, len(icell2d))
    kv_out : np.ndarray
        kv without nan values (nlay, nrow, ncol) or shape(nlay, len(icell2d))
    """
    for layer in kh_in.layer.data:
        if ~np.all(np.isnan(kh_in.loc[layer])):
            logger.debug(f"layer {layer} has a kh")
        elif ~np.all(np.isnan(kv_in.loc[layer])):
            logger.debug(f"layer {layer} has a kv")
        else:
            logger.debug(f"kv and kh both undefined in layer {layer}")

    kh_out = kh_in.where(~np.isnan(kh_in), kv_in * anisotropy)
    kh_out = kh_out.where(~np.isnan(kh_out), fill_value_kh)

    kv_out = kv_in.where(~np.isnan(kv_in), kh_in / anisotropy)
    kv_out = kv_out.where(~np.isnan(kv_out), fill_value_kv)

    return kh_out, kv_out


def fill_top_bot_kh_kv_at_mask(ds, fill_mask):
    """Fill values in top, bot, kh and kv.

    Fill where:
    1. the cell is True in fill_mask
    2. the cell thickness is greater than 0

    Fill values:
    - top: 0
    - bot: minimum of bottom_filled or top
    - kh: kh_filled if thickness is greater than 0
    - kv: kv_filled if thickness is greater than 0

    Parameters
    ----------
    ds : xr.DataSet
        model dataset
    fill_mask : xr.DataArray
        1 where a cell should be replaced by masked value.

    Returns
    -------
    ds : xr.DataSet
        model dataset with adjusted data variables: 'top', 'botm', 'kh', 'kv'
    """

    # zee cellen hebben altijd een top gelijk aan 0
    ds["top"].values = np.where(fill_mask, 0, ds["top"])

    for lay in range(ds.dims["layer"]):
        bottom_nan = xr.where(fill_mask, np.nan, ds["botm"][lay])
        bottom_filled = resample.fillnan_da(bottom_nan, ds=ds)

        kh_nan = xr.where(fill_mask, np.nan, ds["kh"][lay])
        kh_filled = resample.fillnan_da(kh_nan, ds=ds)

        kv_nan = xr.where(fill_mask, np.nan, ds["kv"][lay])
        kv_filled = resample.fillnan_da(kv_nan, ds=ds)

        if lay == 0:
            # top ligt onder bottom_filled -> laagdikte wordt 0
            # top ligt boven bottom_filled -> laagdikte o.b.v. bottom_filled
            mask_top = ds["top"] < bottom_filled
            ds["botm"][lay] = xr.where(fill_mask * mask_top, ds["top"], bottom_filled)
        else:
            # top ligt onder bottom_filled -> laagdikte wordt 0
            # top ligt boven bottom_filled -> laagdikte o.b.v. bottom_filled
            mask_top = ds["botm"][lay - 1] < bottom_filled
            ds["botm"][lay] = xr.where(
                fill_mask * mask_top, ds["botm"][lay - 1], bottom_filled
            )
        ds["kh"][lay] = xr.where(fill_mask * mask_top, ds["kh"][lay], kh_filled)
        ds["kv"][lay] = xr.where(fill_mask * mask_top, ds["kv"][lay], kv_filled)

    return ds


def fill_nan_top_botm_kh_kv(
    ds,
    anisotropy=10.0,
    fill_value_kh=1.0,
    fill_value_kv=0.1,
    remove_nan_layers=True,
):
    """Update a model dataset, by removing nans and adding necessary info.

    Steps:

    1. Compute top and botm values, by filling nans by data from other layers
    2. Compute idomain from the layer thickness
    3. Compute kh and kv, filling nans with anisotropy or fill_values
    """

    # 1
    ds = fill_top_and_bottom(ds)

    # 2
    ds = set_idomain(ds, remove_nan_layers=remove_nan_layers)

    # 3
    ds["kh"], ds["kv"] = get_kh_kv(
        ds["kh"],
        ds["kv"],
        anisotropy,
        fill_value_kh=fill_value_kh,
        fill_value_kv=fill_value_kv,
    )
    return ds


def fill_top_and_bottom(ds):
    """Remove Nans in botm variable, and change top from 3d to 2d if needed."""
    if "layer" in ds["top"].dims:
        ds["top"] = ds["top"].max("layer")
    top = ds["top"].data
    botm = ds["botm"].data
    # remove nans from botm
    for lay in range(botm.shape[0]):
        mask = np.isnan(botm[lay])
        if lay == 0:
            # by setting the botm to top
            botm[lay, mask] = top[mask]
        else:
            # by setting the botm to the botm of the layer above
            botm[lay, mask] = botm[lay - 1, mask]
    return ds


def set_idomain(ds, remove_nan_layers=True):
    """Set idmomain in a model Dataset.

    Parameters
    ----------
    ds : xr.Dataset
        The model Dataset.
    remove_nan_layers : bool, optional
        Removes layers which only contain inactive cells. The default is True.

    Returns
    -------
    ds : TYPE
        DESCRIPTION.
    """
    # set idomain with a default of -1 (pass-through)
    ds["idomain"] = xr.full_like(ds["botm"], -1, int)
    # set idomain of cells  with a positive thickness to 1
    thickness = calculate_thickness(ds)
    ds["idomain"].data[thickness.data > 0.0] = 1
    # set idomain to 0 in the inactive part of the model
    if "active" in ds:
        ds["idomain"] = ds["idomain"].where(ds["active"], 0)
    if remove_nan_layers:
        # only keep layers with at least one active cell
        ds = ds.sel(layer=(ds["idomain"] > 0).any(ds["idomain"].dims[1:]))
    # TODO: set idomain above/below the first/last active layer to 0
    # TODO: remove 'active' and replace by logic of keeping inactive cells in idomain
    return ds


def get_first_active_layer(ds, **kwargs):
    """Get the first active layer in each cell from a model ds.

    Parameters
    ----------
    ds : xr.DataSet
        DESCRIPTION.
    **kwargs : dict
        Kwargs are passed on to get_first_active_layer_from_idomain.

    Returns
    -------
    first_active_layer : xr.DataArray
        raster in which each cell has the zero based number of the first
        active layer. Shape can be (y, x) or (icell2d)
    """
    return get_first_active_layer_from_idomain(ds["idomain"], **kwargs)


def get_first_active_layer_from_idomain(idomain, nodata=-999):
    """get the first active layer in each cell from the idomain.

    Parameters
    ----------
    idomain : xr.DataArray
        idomain. Shape can be (layer, y, x) or (layer, icell2d)
    nodata : int, optional
        nodata value. used for cells that are inactive in all layers.
        The default is -999.

    Returns
    -------
    first_active_layer : xr.DataArray
        raster in which each cell has the zero based number of the first
        active layer. Shape can be (y, x) or (icell2d)
    """
    logger.debug("get first active modellayer for each cell in idomain")

    first_active_layer = xr.where(idomain[0] == 1, 0, nodata)
    for i in range(1, idomain.shape[0]):
        first_active_layer = xr.where(
            (first_active_layer == nodata) & (idomain[i] == 1),
            i,
            first_active_layer,
        )
    first_active_layer.attrs["_FillValue"] = nodata
    return first_active_layer


def update_idomain_from_thickness(idomain, thickness, mask):
    """get new idomain from thickness in the cells where mask is 1 (or True).

    Idomain becomes:
    -    1: if cell thickness is bigger than 0
    -    0: if cell thickness is 0 and it is the top layer
    -   -1: if cell thickness is 0 and the layer is in between active cells

    Parameters
    ----------
    idomain : xr.DataArray
        raster with idomain of each cell. dimensions should be (layer, y, x) or
        (layer, icell2d).
    thickness : xr.DataArray
        raster with thickness of each cell. dimensions should be (layer, y, x)
        or (layer, icell2d).
    mask : xr.DataArray
        raster with ones in cell where the ibound is adjusted. dimensions
        should be (y, x) or (icell2d).

    Returns
    -------
    idomain : xr.DataArray
        raster with adjusted idomain of each cell. dimensions should be
        (layer, y, x) or (layer, icell2d).
    """
    warnings.warn(
        "update_idomain_from_thickness is deprecated. Please use set_idomain instead.",
        DeprecationWarning,
    )
    for ilay, thick in enumerate(thickness):
        if ilay == 0:
            mask1 = (thick == 0) * mask
            idomain[ilay] = xr.where(mask1, 0, idomain[ilay])
            mask2 = (thick > 0) * mask
            idomain[ilay] = xr.where(mask2, 1, idomain[ilay])
        else:
            mask1 = (thick == 0) * mask * (idomain[ilay - 1] == 0)
            idomain[ilay] = xr.where(mask1, 0, idomain[ilay])

            mask2 = (thick == 0) * mask * (idomain[ilay - 1] != 0)
            idomain[ilay] = xr.where(mask2, -1, idomain[ilay])

            mask3 = (thick != 0) * mask
            idomain[ilay] = xr.where(mask3, 1, idomain[ilay])

    return idomain
