from sepal_ui import reclassify as rec


class TestTableView:
    def test_init(self):

        # default init
        view = rec.TableView()
        assert isinstance(view, rec.TableView)

        return

    def test_get_class(self):

        return

    def test_nest_tile(self):

        # nest the tile
        view = rec.TableView()
        res = view.nest_tile()

        assert res == view
        assert view._metadata["mount_id"] == "nested_tile"
        assert view.elevation == 0
        assert len(view.children[0].children) == 1

        return
