# -*- coding: utf-8 -*-
"""Created on Thu Jan  7 16:23:35 2021.

@author: oebbe
"""

import nlmod
from nlmod.read import geotop, regis

import test_001_model


# @pytest.mark.skip(reason="too slow")
def test_get_regis(extent=[98600.0, 99000.0, 489400.0, 489700.0]):
    regis_ds = regis.get_regis(extent)

    assert regis_ds.dims["layer"] == 20

    return regis_ds


# @pytest.mark.skip(reason="too slow")
def test_get_regis_botm_layer_BEk1(
    extent=[98700.0, 99000.0, 489500.0, 489700.0],
    botm_layer="MSc",
):
    regis_ds = regis.get_regis(extent, botm_layer)
    assert regis_ds.dims["layer"] == 15
    assert regis_ds.layer.values[-1] == botm_layer
    return regis_ds


# @pytest.mark.skip(reason="too slow")
def test_get_geotop(extent=[98600.0, 99000.0, 489400.0, 489700.0]):
    geotop_ds = geotop.get_geotop(extent)
    return geotop_ds


# @pytest.mark.skip(reason="too slow")
def test_get_regis_geotop(extent=[98600.0, 99000.0, 489400.0, 489700.0]):
    regis_geotop_ds = regis.get_combined_layer_models(
        extent, use_regis=True, use_geotop=True
    )
    regis_geotop_ds = nlmod.base.to_model_ds(regis_geotop_ds)
    assert regis_geotop_ds.dims["layer"] == 24
    return regis_geotop_ds


# @pytest.mark.skip(reason="too slow")
def test_get_regis_geotop_keep_all_layers(
    extent=[98600.0, 99000.0, 489400.0, 489700.0],
):
    regis_geotop_ds = regis.get_combined_layer_models(
        extent, use_regis=True, use_geotop=True, remove_nan_layers=False
    )
    assert regis_geotop_ds.dims["layer"] == 137
    return regis_geotop_ds
