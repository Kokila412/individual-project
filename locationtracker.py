import phonenumbers
from phonenumbers import geocoder
# from test import number
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

key="2004b4281ee944df8873419c3eff3fea"
number=input("enter the number with country code")
check=phonenumbers.parse(number)
loc=geocoder.description_for_number(check,"en")
print(loc)

service_provider=check
simname=carrier.name_for_number(check,"en")
print(simname)

geocoder=OpenCageGeocode(key)

num=str(loc)
result=geocoder.geocode(num)

latitude=result[0]['geometry']['lat']
longitude=result[0]['geometry']['lng']
print(latitude,longitude)

mapping=folium.Map(location=[latitude,longitude],zoom_start=9)
folium.Marker([latitude,longitude], popup=loc).add_to(mapping)
mapping.save("mylocation.html")
