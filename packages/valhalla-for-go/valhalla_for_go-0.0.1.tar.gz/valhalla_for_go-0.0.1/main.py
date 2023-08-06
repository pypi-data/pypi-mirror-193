from valhalla import Actor, get_config
from valhalla.utils import decode_polyline

def locate(lat, lon, tile_path):
    config = get_config(tile_extract=tile_path)
    actor = Actor(config)
    location = actor.locate({'verbose': True, 'locations':[{'lat': lat, 'lon': lon}]})
    return location[0]['edges']

def decode_polygon(shape):
    return [t[::-1] for t in decode_polyline(shape)]
