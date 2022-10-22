from audioop import add
from urllib import response
import requests
import pandas as pd
import json
import time

token_denue = "3364a743-4c46-4528-985c-5a01d6fcaf8a"
token_google = "AIzaSyDJ0YiKOKwfksHXf6wKIk6J0SCkkh_wM3g"

llaves = {"aguascalientes":"01","baja california sur":"03","baja california":"02","campeche":"04",
            "coahuila de zaragoza":"05","coahuila":"05","colima":"06","chiapas":"07",
            "chihuahua":"08","cdmx":"09","ciudad de méxico":"09","distrito federal":"09",
            "durango":"10","guanajuato":"11","guerrero":"12","hidalgo":"13","jalisco":"14","edo. de méxico":"15",
            "michoacán de ocampo":"16","michoacán":"16","morelos":"17","nayarit":"18","nuevo león":"19","oaxaca":"20","puebla":"21",
            "querétaro":"22","quintana roo":"23","san luis potosí":"24","sinaloa":"25","sonora":"26",
            "tabasco":"27","tamaulipas":"28","tlaxcala":"29","veracruz de ignacio de la llave":"30","veracruz":"30",
            "yucatán":"31","zacatecas":"32"
            }


entidades = ["aguascalientes","baja california sur","baja california","campeche",
            "coahuila de zaragoza","coahuila","colima","chiapas",
            "chihuahua","cdmx","ciudad de méxico","distrito federal",
            "durango","guanajuato","guerrero","hidalgo","jalisco","edo. de méxico",
            "michoacán de ocampo","michoacán","morelos","nayarit","nuevo león","oaxaca","puebla",
            "querétaro","quintana roo","san luis potosí","sinaloa","sonora",
            "tabasco","tamaulipas","tlaxcala","veracruz de ignacio de la llave","veracruz",
            "yucatán","zacatecas"]


def url_denue_alrededores(condiciones,latitud,longitud,metros):
    return f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{condiciones}/{latitud},{longitud}/{metros}/{token_denue}"


def url_denue_nombre(nombre,entidad_federal):
    return f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{nombre}/{entidad_federal}/1/10/{token_denue}"

#data = pd.read_csv("https://raw.githubusercontent.com/aplusplus-jpg/resources/main/examples.csv?token=GHSAT0AAAAAABZOXJDQAG63MDUZNGN4P6GWY2R6O7A", header=None)


def Busqueda_por_dirección(dir,tipo,rad=50):
    coordenas=address_to_coordinates(dir)
    url=url_google_alrededores(coordenas[0],coordenas[1],rad,tipo)
    return requests.get(url).json()


def busqueda_placeid():
    pass


def buscarEntidad(direccion):
    for i in entidades:
        if i in direccion.lower():
            return llaves[i]
    return "00"


def url_google_alrededores(latitud,longitud,metros,condiciones):
    return f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud}%2C{longitud}&radius={metros}&type={condiciones}&key={token_google}'

def replace_text_search(text):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="fields=name"
    return base_url + text +fields+ token_i

def replace_text(text):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="&fields=formatted_address%2Cname%2Cbusiness_status%2Cgeometry%2Cplace_id%2Ctype"
    imput_type="&inputtype=textquery"
    base_url= base_url + text+imput_type +fields+ token_i
    return base_url.replace(" ","%20")


def buscarNombreDenue(nombre,direccion):
    entidad_federal = buscarEntidad(direccion)
    nombre = nombre.replace("'"," ")
    url = url_denue_nombre(nombre,entidad_federal)
    return requests.get(url).json()


def buscarNombreGoogle(nombre):
    response=requests.request("GET", replace_text(nombre), headers={}, data={})
    return response.json()


def buscarAlrededoresDenue():
    pass


def buscarNombre(nombre,direccion):
    """
    nombre = es una variable string que contiene el nombre del negocio
    direccion = contiene la direccion del negocio como lista en coordenadas (latitud y longitud)
    
    Esta fucion le pasamos los datos de un negocio y lo buscara en la base de datos de denue y google 
    
    """ 
    resultado_denue = buscarNombreDenue(nombre,direccion)
    resultado_google = buscarNombreGoogle(nombre)
    
    if resultado_denue == "No hay resultados." and len(resultado_google['candidates']) > 0:
        if resultado_google['candidates'][0]['name'].lower() >= nombre:
            print("si")
    else:
        print("si")    
    print("------------------")


def Busqueda_por_dirección(dir,tipo,rad=50):
    coordenas=address_to_coordinates(dir)
    url=url_google_alrededores(coordenas[0],coordenas[1],rad,tipo)
    return requests.get(url).json()


def Alrededores_google(dir,nombre):
    coordenadas=address_to_coordinates(dir)
    print("dir",dir)
    print("coord",coordenadas)
    url=url_google_alrededores(coordenadas['lat'],coordenadas['lng'],50,nombre)
    response=requests.request("GET",url,headers={},data={})
    return response


def address_to_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ address +"&key=" + token_google
    response = requests.request("GET", url, headers={}, data={})
    try:
        coordinates_dict = response.json()['results'][0]['geometry']['location']
        return (coordinates_dict['lat'], coordinates_dict['lng'] )
    except:
        coordinates_dict = response.json()
        return coordinates_dict

        
"""
-----EXAMPLES----

"""        
dire="REGINA 135 ACCE A CENTRO #AREA 9# CUAUHTEMOC 6090 125 126 CDMX"
nom="CENTRO PAPELERO SUN-RISE SA DE CV"
Alrededores_google(dire, nom)
