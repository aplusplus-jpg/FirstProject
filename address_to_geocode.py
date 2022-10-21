import requests
import pandas as pd

api_key = "AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
pymes_df = pd.read_csv("https://raw.githubusercontent.com/arielmerinos/A-first-Shiny-project/main/examples.csv",
                       names=['name', 'address'])


def address_to_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ address +"&key=" + api_key
    response = requests.request("GET", url, headers={}, data={})
    coordinates_dict = response.json()['results'][0]['geometry']['location']
    return (coordinates_dict['lat'], coordinates_dict['lng'] )

for index, pyme in pymes_df.iterrows():
    print(pyme['name'], address_to_coordinates(pyme['address']))

