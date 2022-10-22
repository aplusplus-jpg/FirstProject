import requests
import pandas as pd


api_key = "AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"


def address_to_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ address +"&key=" + api_key
    response = requests.request("GET", url, headers={}, data={})
    try: 
        coordinates_dict = response.json()['results'][0]['geometry']['location']
        coordinates_tuple = (coordinates_dict['lat'], coordinates_dict['lng'] )
        return coordinates_tuple 
    except IndexError:
        return (0,0)


def concatenateDataFrame(path, newPath):
    """
    Create a new dataset with concatenated columns
    """
    df = pd.read_csv(path, header=0)
    nf = pd.DataFrame()
    nf['nombre'] = df['NombComp']
    nf["direccion"] = df["Direccion1"].map(str)  + " "+ df["Direccion2"].map(str) + " " + df["Direccion3"].map(str) + " " +df["Colonia"].map(str) + " " + df["MunicipioDel"].map(str) + " " + df["Estado"].map(str) + df["CP"].map(str)
    #nf['geocodes'] = nf["direccion"].map(address_to_coordinates)
    nf.to_csv(newPath)

nd = pd.read_csv("/home/alex/FirstProject/examples.csv", header=0)
nd["geocodes"] = nd["direccion"].map(address_to_coordinates)
nd.to_csv('examples.csv')
print(nd)




