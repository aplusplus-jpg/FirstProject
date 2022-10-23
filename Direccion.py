import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

from cmath import nan
import pandas as pd
import requests

import random 


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def obtenercontacto(url):
    '''A partir de la página de una PyME, se obtienen correo, facebook,
    instagram, tiktok, twitter y youtube'''
    links = {'correo':None, 'facebook':None, 'instagram':None,
             'tiktok':None, 'twitter':None, 'youtube':None}
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        ref = [tag.get('href', None) for tag in tags]
        for i in ref:
            if '@' in i:
                links['correo'] = i
            if 'facebook' in i:
                links['facebook'] = i
            if 'instagram' in i:
                links['instagram'] = i
            if 'tiktok' in i:
                links['tiktok'] = i
            if 'twitter' in i:
                links['twitter'] = i
            if 'youtube' in i:
                links['youtube'] = i
        return [direc for direc in links.values()]
    except:
        return links


def Busqueda_por_dirección(dir,tipo,rad=50):
    coordenas=address_to_coordinates(dir)
    url=url_google_alrededores(coordenas[0],coordenas[1],rad,tipo)
    return requests.get(url).json()

def buscarEntidad(direccion):
    for i in entidades:
        if i in direccion.lower():
            return llaves[i]
    return "00"
# Denue
token_denue = "3364a743-4c46-4528-985c-5a01d6fcaf8a"

def url_denue_alrededores(condiciones,latitud,longitud,metros):
    return f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{condiciones}/{latitud},{longitud}/{metros}/{token_denue}"

def url_denue_nombre(nombre,entidad_federal):
    return f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{nombre}/{entidad_federal}/1/10/{token_denue}"

# Google
token_google = "AIzaSyDJ0YiKOKwfksHXf6wKIk6J0SCkkh_wM3g"

def url_google_alrededores(latitud,longitud,metros,condiciones):
    return f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud},{longitud}&radius={metros}&type={condiciones}&key={token_google}'

def replace_text_search(text):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="fields=name"
    return base_url + text +fields+ token_i

def replace_text(text):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="&fields=formatted_address,name,business_status,geometry,place_id,type"
    imput_type="&inputtype=textquery"
    base_url= base_url + text+imput_type +fields+ token_i
    return base_url.replace(" ","%20")


def buscarNombreGoogle(nombre):
    response=requests.request("GET", replace_text(nombre), headers={}, data={})
    return response.json()

def buscarAlrededoresDenue():
    pass

def Busqueda_por_dirección(dir,tipo,rad=50):
    coordenas=address_to_coordinates(dir)
    url=url_google_alrededores(coordenas[0],coordenas[1],rad,tipo)
    return requests.get(url).json()

def alrededoresGoogle(dir,nombre):
    #regresa el id del lugar 
    coordenadas=address_to_coordinates(dir)
    url=url_google_alrededores(coordenadas[0],coordenadas[1],10,nombre)
    response=requests.request("GET",url,headers={},data={})
    
    for i in response.json()['results']:
        
        if nombre in i['name'] or i['name'] in nombre:
            return i['place_id']
    return False
  
def buscarNombreDenue(nombre,direccion):
    entidad_federal = buscarEntidad(direccion)
    nombre = nombre.replace("'"," ")
    url = url_denue_nombre(nombre,entidad_federal)
    return requests.get(url).json()

    
    
def address_to_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ address +"&key=AIzaSyDJ0YiKOKwfksHXf6wKIk6J0SCkkh_wM3g"
    response = requests.request("GET", url, headers={}, data={})
    
    try:
        coordinates_dict = response.json()['results'][0]['geometry']['location']
        return (coordinates_dict['lat'], coordinates_dict['lng'] )
    except:
        return (0, 0)
    

def busquedaIdGoogle(id):
    if id==False:
        return "no se encontraron resultados"
    url="https://maps.googleapis.com/maps/api/place/details/json?place_id="+id
    fields="&fields=business_status,geometry,type,url,current_opening_hours,delivery,formatted_phone_number,place_id,price_level,rating,reviews,types,url,user_ratings_total,website"
    token_api_google = "&key=AIzaSyDRhQ9HRGDmnGI6Rd79x1fp-vhCaWoJeYo"
    url=url+fields+token_api_google
    headers={}
    payload={}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
    


def flatJson(lista_de_json):
    path="Final.csv"
    headers=['business_status', 'delivery', 'formatted_phone_number','nombre','place_id',"rating",'rating1','text1','rating2','text2','rating3','text3','rating4','text4','rating5','text5', 'types', 'url', 'user_ratings_total', 'website']
    df=pd.DataFrame(columns=headers)
    for json in lista_de_json:
        Keys='business_status', 'delivery', 'formatted_phone_number', 'name', 'place_id', 'rating', 'reviews', 'types', 'url', 'user_ratings_total', 'website'
        lista=[]
        for key in Keys:
            try:
            
                if key=='current_opening_hours':

                    """df1 = pd.json_normalize(json['result'][key]['periods']  , sep='_')
                    lista.append(json['result'][key]['open_now'])
                    lista.append(df1.values.tolist())
                    lista.append(json['result'][key]['weekday_text'])"""
                    continue
                
                if key=='reviews':
                    try:
                        for i in range(6):
                            lista.append(json['result'][key][i]['rating'])
                            lista.append(json['result'][key][i]['text'])
                
                    except Exception as e:

                        continue

                    continue
                if key=='geometry':

                    continue
                if key=='types':
                    str=""
                    for i in range(len(json['result'][key])):
                        str=str+json['result'][key][i]
                    lista.append(str)
                    continue

                lista.append(json['result'][key])
            except:
                lista.append(None)

        df.loc[len(df)] = lista
        
        
    
    return df.to_csv(path)
    
    
tokens_google = ["AIzaSyDJ0YiKOKwfksHXf6wKIk6J0SCkkh_wM3g","AIzaSyBJd3stl1KcTQ-9YT0sA8ZhgaK1KUNsJzA"]
token_google = random.choice(tokens_google)
data=pd.read_csv("resources\limpia.csv")
def awsRequest(nombre,direccion):

    return requests.get(f"https://mdta6lzp19.execute-api.us-east-1.amazonaws.com/negocio?nombre={nombre}&direccion={direccion}")
def otra(x):   
    a = []
    for i in range(x):
        print(data["NombComp"][i],"-",data["DirComp"][i])
        a.append(awsRequest(data["NombComp"][i],data["DirComp"][i]).json())
    return a   
    

lista=otra()
#l2=flatJson(lista)

<<<<<<< HEAD
=======

dir="C. Dr. José María Vértiz 1148, Independencia, Benito Juárez, 03630 Ciudad de México, CDMX"
nom="Farmacia San Pablo Vertiz"
json=busquedaIdGoogle(alrededoresGoogle(dir, nom))
>>>>>>> main
