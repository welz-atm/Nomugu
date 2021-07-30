from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic
from django.conf import settings


def calc_distance(x, y):
    client = OpenCageGeocode(settings.OPENCAGE_KEY)
    qs_src = client.geocode(x)
    source_lat = qs_src[0]['geometry']['lat']
    source_long = qs_src[0]['geometry']['lng']

    qs_dest = client.geocode(y)
    dest_lat = qs_dest[0]['geometry']['lat']
    dest_long = qs_dest[0]['geometry']['lng']

    src = (source_lat, source_long)
    dest = (dest_lat, dest_long)
    result = geodesic(src, dest).km
    return result