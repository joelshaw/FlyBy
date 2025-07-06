import geocoder
import requests


def get_location():
    g = geocoder.ip('me')
    if g.ok:
        print(f"Flights near {g.city}, {g.state} \n ----------")
        return g.latlng
    return None, None
