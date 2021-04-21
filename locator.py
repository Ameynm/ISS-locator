import requests
import json
import geopy
from geopy.geocoders import Nominatim
import webbrowser

response = requests.get("http://api.open-notify.org/iss-now.json")
a = response.json()
b = a['iss_position']
c, d = float(b['latitude']), float(b['longitude'])
locator = Nominatim(user_agent="myGeocoder")
print(c,d)
location = (c, d)
place = locator.reverse(location)
if place == None:
    print("address for this location cannot be found, please check the map")
else:
    print(place.address)
map_link = "https://www.google.com/maps/search/?api=1&query="+str(c)+','+str(d)
print(map_link)
webbrowser.open(map_link)
