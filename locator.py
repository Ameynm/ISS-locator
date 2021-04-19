import requests
import json
import geopy
from geopy.geocoders import Nominatim
response = requests.get("http://api.open-notify.org/iss-now.json")
a = response.json()
b = a['iss_position']
c = float(b['latitude'])
d = float(b['longitude'])
locator = Nominatim(user_agent="myGeocoder")
location = (c, d)
place = locator.reverse(location)
print(place.address)
