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
    nf["direccion"] = df["Direccion1"].map(str)  + " "+ df["Direccion2"].map(str) + " " + df["Direccion3"].map(str) + " " +df["Colonia"].map(str) + " " + df["MunicipioDel"].map(str) + " " +  df["CP"].map(str) + " " + df["Estado"].map(str)  
    nf["direccion"] = nf['direccion'].str.replace("#", "")
    #nf['geocodes'] = nf["direccion"].map(address_to_coordinates)
    nf.to_csv(newPath)


concatenateDataFrame("../resources/csv1.csv", "./new1.csv")
#for i in range(1,7):
#    concatenateDataFrame(f"../resources/csv{i}.csv", f"./new{i}.csv")





