from sepal_ui import mapping as sm


class TestZoomControl:
    def test_init(self):

        m = sm.SepalMap()
        m.clear()
        zoom_control = sm.ZoomControl(m)
        m.add(zoom_control)

        assert isinstance(zoom_control, sm.ZoomControl)
        assert zoom_control in m.controls

        return

    def test_change_zoom(self):

        m = sm.SepalMap()
        zoom_control = next(c for c in m.controls if isinstance(c, sm.ZoomControl))
        m.zoom = 10

        zoom_control.zoom(zoom_control.plus)
        assert m.zoom == 11

        zoom_control.zoom(zoom_control.minus)
        assert m.zoom == 10

        return

    def test_min_max_zoom(self):

        m = sm.SepalMap()
        zoom_control = next(c for c in m.controls if isinstance(c, sm.ZoomControl))

        # click 40 times on plus and then 40 times on minus
        [zoom_control.zoom(zoom_control.plus) for i in range(40)]
        assert m.zoom == 24
        [zoom_control.zoom(zoom_control.minus) for i in range(40)]
        assert m.zoom == 0

        # ssame but with a min-max zoom on the map
        m.min_zoom = 5
        m.max_zoom = 18
        [zoom_control.zoom(zoom_control.plus) for i in range(40)]
        assert m.zoom == m.max_zoom
        [zoom_control.zoom(zoom_control.minus) for i in range(40)]
        assert m.zoom == m.min_zoom

        return
