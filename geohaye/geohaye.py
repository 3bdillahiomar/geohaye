"""Main module."""

import ipyleaflet

class Map(ipyleaflet.Map):
    def __init__(self, center=[9.56, 44.065], zoom=12, **kwargs):  # center=[lat, lon] # zoom=12 (default) Hargeisa Test
        super().__init__(center=center,zoom=zoom, **kwargs)
        self.add_control(ipyleaflet.LayersControl())