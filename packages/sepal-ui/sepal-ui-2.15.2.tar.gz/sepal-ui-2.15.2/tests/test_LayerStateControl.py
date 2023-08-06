import ee
import pytest
from ipyleaflet import RasterLayer
from traitlets import Bool

from sepal_ui import mapping as sm


class TestLayerStateControl:
    def test_init(self):

        m = sm.SepalMap()
        state = sm.LayerStateControl(m)
        m.add(state)

        assert isinstance(state, sm.LayerStateControl)
        assert state.w_state.loading is False

        return

    @pytest.mark.skipif(not ee.data._credentials, reason="GEE is not set")
    def test_update_nb_layer(self, map_with_layers):

        # create the map and controls
        m = map_with_layers
        state = next(c for c in m.controls if isinstance(c, sm.LayerStateControl))

        # TODO I don't know how to check state changes but I can at least check the conclusion
        assert state.w_state.msg == "2 layer(s) loaded"

        # remove a layer to update the nb_layer
        m.remove_layer(-1)
        assert state.w_state.msg == "1 layer(s) loaded"

        return

    @pytest.mark.skipif(not ee.data._credentials, reason="GEE is not set")
    def test_update_loading(self, map_with_layers):

        # get the map and control
        m = map_with_layers
        state = next(c for c in m.controls if isinstance(c, sm.LayerStateControl))

        # check that the parameter is updated with existing layers
        m.layers[-1].loading = True
        assert state.nb_loading_layer == 1
        assert state.w_state.msg == "loading 1 layer(s) out of 2"

        # check when this loading layer is removed
        m.remove_layer(-1)
        assert state.nb_loading_layer == 0
        assert state.w_state.msg == "1 layer(s) loaded"

        return

    @pytest.fixture
    def map_with_layers(self):
        """create a map with 2 layers and a stateBar."""
        # create the map and controls
        m = sm.SepalMap()
        state = sm.LayerStateControl(m)
        m.add(state)

        # add some ee_layer (loading very fast)
        # world lights
        dataset = ee.ImageCollection("NOAA/DMSP-OLS/CALIBRATED_LIGHTS_V4").filter(
            ee.Filter.date("2010-01-01", "2010-12-31")
        )
        m.addLayer(dataset, {}, "Nighttime Lights")

        # a fake layer with loading update possibilities
        m.add_layer(self.FakeLayer())

        return m

    class FakeLayer(RasterLayer):
        """
        layer class that have only one parameter: the laoding trait.
        """

        loading = Bool(False).tag(sync=True)
