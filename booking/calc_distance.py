from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic


key = '879ecf748ef44d9f8250a3411aa34c81'


def calc_distance(x, y):
    client = OpenCageGeocode(key)
    qs_src = client.geocode(x)
    source_lat = qs_src[0]['geometry']['lat']
    source_long = qs_src[0]['geometry']['long']

    qs_dest = client.geocode(y)
    dest_lat = qs_dest[0]['geometry']['long']
    dest_long = qs_dest[0]['geometry']['long']

    src = (source_lat, source_long)
    dest = (dest_lat, dest_long)
    result = geodesic(src, dest)
    return result