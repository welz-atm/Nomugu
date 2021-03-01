from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic
import haversine as hs
from NoMugu.settings import opencage_key


def calc_distance(x, y):
    client = OpenCageGeocode(opencage_key)
    qs_src = client.geocode(x)
    source_lat = qs_src[0]['geometry']['lat']
    source_long = qs_src[0]['geometry']['lng']

    qs_dest = client.geocode(y)
    dest_lat = qs_dest[0]['geometry']['lat']
    dest_long = qs_dest[0]['geometry']['lng']

    src = (source_lat, source_long)
    dest = (dest_lat, dest_long)
    result = geodesic(src, dest).km
#    result = hs.haversine(src, dest)
    return result