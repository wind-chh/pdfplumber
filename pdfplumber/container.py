from itertools import chain
from . import utils, convert


class Container(object):
    cached_properties = ["_rect_edges", "_edges", "_objects"]

    def flush_cache(self, properties=None):
        props = self.cached_properties if properties is None else properties
        for p in props:
            if hasattr(self, p):
                delattr(self, p)

    def close_file(self):
        """
        A placeholder, to be overridden when necessary (as in PDF.open)
        """
        pass

    def close(self):
        self.flush_cache()
        self.close_file()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    @property
    def rects(self):
        return self.objects.get("rect", [])

    @property
    def lines(self):
        return self.objects.get("line", [])

    @property
    def curves(self):
        return self.objects.get("curve", [])

    @property
    def images(self):
        return self.objects.get("image", [])

    @property
    def chars(self):
        return self.objects.get("char", [])

    @property
    def rect_edges(self):
        if hasattr(self, "_rect_edges"):
            return self._rect_edges
        visible_rects = filter(utils.is_visible, self.rects)
        rect_edges_gen = (utils.rect_to_edges(r) for r in visible_rects)
        self._rect_edges = list(chain(*rect_edges_gen))
        return self._rect_edges

    @property
    def edges(self):
        if hasattr(self, "_edges"):
            return self._edges
        visible_lines = filter(utils.is_visible, self.lines)
        line_edges = list(map(utils.line_to_edge, visible_lines))
        self._edges = self.rect_edges + line_edges
        return self._edges

    @property
    def horizontal_edges(self):
        def test(x):
            return x["orientation"] == "h"

        return list(filter(test, self.edges))

    @property
    def vertical_edges(self):
        def test(x):
            return x["orientation"] == "v"

        return list(filter(test, self.edges))


Container.to_json = convert.to_json
Container.to_csv = convert.to_csv
