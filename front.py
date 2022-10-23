from distutils import archive_util
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import time
import random
import re

from difflib import SequenceMatcher as SM

st.set_page_config(page_title = "Hackaton 2022 BBVA",page_icon=":bar_chart:",layout="wide")
st.title('A++ Hackaton BBVA - 2022')

# st.file_uploader("Please, upload your csv")
#st.button("Read a dataset (.csv)", on_click=)

#--------CARGA DE DATOS--------
#df = pd.read_excel('dataset/output.xlsx',nrows= 100)
df = pd.read_csv('dataset/Final_Data_Hackathon_2022.csv')
st.dataframe(df[0:5])

for fila in df.iterrows():
    st.text_area(fila)


#-----SIDEBAR SECCION-----------
st.sidebar.header("Filtra aqui.")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# In[656]:





# In[511]:


def awsRequest(nombre,direccion):
    return requests.get(f"https://mdta6lzp19.execute-api.us-east-1.amazonaws.com/negocio?nombre={nombre}&direccion={direccion}")

def awsRequestDenue(nombre,direccion):
    return requests.get(f"https://fi028kzaj9.execute-api.us-east-1.amazonaws.com/default/denue?nombre={nombre}&direccion={direccion}")



lat = []
log = []

for i in a:
    try:
        lat.append(float(json.loads(i.text)['result']['geometry']['location']['lat']))
        log.append(float(json.loads(i.text)['result']['geometry']['location']['lng']))
    except:
        lat.append(None)
        log.append(None)
        



tokens_google = ["AIzaSyDJ0YiKOKwfksHXf6wKIk6J0SCkkh_wM3g","AIzaSyBJd3stl1KcTQ-9YT0sA8ZhgaK1KUNsJzA"]
token_google = random.choice(tokens_google)



headers = {} 
payload = {}


def coincidenciasNombres(nombre_buscar,nombre_resultado,radio = 0.70):
    if nombre_resultado.lower() >= nombre_buscar.lower():
        return True
    elif SM(None,nombre_buscar, nombre_resultado).ratio()> radio:
        return True
    else:
        return False

def url_google_alrededores(latitud,longitud,metros,condiciones):
    return f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitud}%2C{longitud}&radius={metros}&type={condiciones}&key={token_google}'




def alrededoresGoogle(address,nombre):
    coordenadas=address_to_coordinates(address)
    url=url_google_alrededores(coordenadas[0],coordenadas[1],10,nombre)
    response=requests.request("GET",url,headers={},data={})

    if len(response.json()['results'])>0:
        for i in response.json()['results']:
            print(i)
            print(i['name'])
            print(i['name'])
            if nombre in i['name'] or i['name'] in nombre:
                return i['place_id']
        return "No"

def replace_text(text):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="&fields=name,place_id"
    imput_type="&inputtype=textquery"
    base_url= base_url + text + imput_type + fields + token_i
    return base_url.replace(" ","%20")

def buscarNombreGoogle(nombre):
    response = requests.request("GET", replace_text(nombre), headers={}, data={})
    resultado_google = response.json()
    if len(resultado_google['candidates']) > 0:
        for i in resultado_google['candidates']:
            return i['place_id']
    return "Nada"

def busquedaIdGoogle(ID):
    url="https://maps.googleapis.com/maps/api/place/details/json?place_id="+ID
#     fields="&fields=name%2Cbusiness_status%2Ctype%2Curl%2Ccurrent_opening_hours%2Cdelivery%2Cformatted_phone_number%2Cplace_id%2Cprice_level%2Crating%2Creviews%2Ctypes%2Curl%2Cuser_ratings_total%2Cwebsite"
    fields="&fields=geometry"
    token_api_google = "&key=AIzaSyDRhQ9HRGDmnGI6Rd79x1fp-vhCaWoJeYo"
    url=url+fields+token_api_google
    
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def address_to_coordinates(address):
    address=address.replace(" ", "%20")

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={ address }&key={token_google}"
    
    response = requests.request("GET", url, headers={}, data={})

    try:
        coordinates_dict = response.json()['results'][0]['geometry']['location']
        print(coordinates_dict['lat'], coordinates_dict['lng'] )
        return (coordinates_dict['lat'], coordinates_dict['lng'] )
    except:
        print("ingrese una idrección correcta")
def chida(nombre):
    google = buscarNombreGoogle(nombre)

    if google == "No":
        result = "No"
    else:
        result = busquedaIdGoogle(google)


    return result




# llaves = {"aguascalientes":"01","baja california sur":"03","baja california":"02","campeche":"04",
#             "coahuila de zaragoza":"05","coahuila":"05","colima":"06","chiapas":"07",
#             "chihuahua":"08","cdmx":"09","ciudad de méxico":"09","distrito federal":"09",
#             "durango":"10","guanajuato":"11","guerrero":"12","hidalgo":"13","jalisco":"14","edo. de méxico":"15",
#             "michoacán de ocampo":"16","michoacán":"16","morelos":"17","nayarit":"18","nuevo león":"19","oaxaca":"20","puebla":"21",
#             "querétaro":"22","quintana roo":"23","san luis potosí":"24","sinaloa":"25","sonora":"26",
#             "tabasco":"27","tamaulipas":"28","tlaxcala":"29","veracruz de ignacio de la llave":"30","veracruz":"30",
#             "yucatán":"31","zacatecas":"32"
#             }

llaves = {'Aguascalientes':"01",
 'Baja California Sur':"03",
 'Baja California':"02",
 'CDMX':"09",
 'Campeche':"04",
 'Chiapas':"07",
 'Chihuahua':"08",
 'Coahuila':"05",
 'Colima':"06",
 'Durango':"10",
 'Estado de Mexico':"15",
 'Guanajuato':"11",
 'Guerrero':"12",
 'Hidalgo':"13",
 'Jalisco':"14",
 'Michoacan':"16",
 'Morelos':"17",
 'Nuevo Leon':"19",
 'Oaxaca':"20",
 'Puebla':"21",
 'Queretaro':"22",
 'Quintana Roo':"23",
 'San Luis Potosi':"24",
 'Sinaloa':"25",
 'Sonora':"26",
 'Tabasco':"27",
 'Tamaulipas':"28",
 'Tlaxcala':"29",
 'Veracruz':"30",
 'Yucatan':"31",
 'Zacatecas':"32"}

entidades = ['Aguascalientes',
 'Baja California Sur',
 'Baja California',
 'CDMX',
 'Campeche',
 'Chiapas',
 'Chihuahua',
 'Coahuila',
 'Colima',
 'Durango',
 'Estado de Mexico',
 'Guanajuato',
 'Guerrero',
 'Hidalgo',
 'Jalisco',
 'Michoacan',
 'Morelos',
 'Nuevo Leon',
 'Oaxaca',
 'Puebla',
 'Queretaro',
 'Quintana Roo',
 'San Luis Potosi',
 'Sinaloa',
 'Sonora',
 'Tabasco',
 'Tamaulipas',
 'Tlaxcala',
 'Veracruz',
 'Yucatan',
 'Zacatecas']




tokens_denue = ["d477dd27-255c-4449-baef-957ee33e94b6","3364a743-4c46-4528-985c-5a01d6fcaf8a","99a7f211-3b4a-4a18-5254-dac3c479840e",
                "5e57ddfb-688e-4c78-a3d5-1898fd356ba3","c5135a58-1123-4d5f-927a-dd3773ae564c","56984dff-3daf-4328-afeb-66175d877b38",
                "300bebf9-6de0-4d8a-a3fb-b5fd9b2a6acc","e04a9d5d-7267-4e21-9868-4b2468ebe1fd","de354429-5a37-4dee-bf77-75464e2abd7c",
                "f1a899c7-9f92-4600-b324-2eb0b65e4b57","75c7770c-c24c-4a00-1da2-f52eec3a3a26","3769ef57-9ed9-40d6-aec9-a5262dc27304",
                "2f14a0f0-c2ef-48cf-bab7-a0f82282a409","c6709043-0fdd-4772-a7df-4e0d36a12773"]
token_denue = random.choice(tokens_denue)

def buscarEntidad(direccion):
    for i in entidades:
        if i in direccion:
            return llaves[i]
    return "00"    

def buscarNombreDenue(nombre,direccion):
    entidad_federal = buscarEntidad(direccion)
#     print(direccion,entidad_federal)
#     print(nombre)

    nombre = nombre.replace(" ", "%20")
#     print(nombre)
    while nombre[-1]=="0":
        nombre = nombre[0:-3]
#         print(nombre)
#     print(token_denue)
    url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{nombre}/{entidad_federal}/1/10/{token_denue}"
    url.replace("%20/","/")
#     print(url)
    respons= requests.get(url).json()
    return respons

def chidoDenue(nombre,direccion):

    result = buscarNombreDenue(nombre, direccion)

    if result == "No hay resultados.":
        result = json.dumps(result)
    else:
        result = result[0]
    return result








def denueArreglo(result,elementos):
    result = json.loads(result.text)
    arreglo = []
    if result == "No hay resultados." or result == "N":
        for i in range(len(elementos)):
            arreglo.append(None)
    else:
        for i in range(len(elementos)):
#             print(elementos[i],"-",result[elementos[i]] )
            print(i)
            if len(result[elementos[i]])>0:
                arreglo.append(result[elementos[i]])
    
    return arreglo



resultados_busqueda_nombre_denue_significado = ["CLEE"
                                    ,"Id"
                                    ,"Nombre"
                                    ,"Razon_social"
                                    ,"Clase_actividad"
                                    ,"Estrato"
                                    ,"Tipo_vialidad"
                                    ,"Calle"
                                    ,"Num_Exterior"
                                    ,"Num_Interior"
                                    ,"Colonia"
                                    ,"CP"
                                    ,"Ubicacion"
                                    ,"Telefono"
                                    ,"Correo_e"
                                    ,"Sitio_internet"
                                    ,"Tipo"
                                    ,"Longitud"
                                    ,"Latitud"
                                    ,"tipo_corredor_industrial"
                                    ,"nom_corredor_industrial"
                                    ,"numero_local"]


    
for i in dataframe.iterrows:
    # for i in range(len(data["nombre"])):
    a = []
    b = []
    time.sleep(0.1)
    a.append(chida(i[1]))
    b.append(chidoDenue(data["NombComp"][i],data["DirComp"][i]))

archivo = open("resultados.txt","w") 

for i in len(a):
    archivo.write(a[i].text)
    archivo.write(b[i].text)


archivo.close()

def awsRequestsentimientos(texto,idioma):
    return requests.get(f"https://rlanpvxdde.execute-api.us-east-1.amazonaws.com/default/sentimientos?texto={texto}&idioma={idioma}")




# awsRequestsentimientos(texto,idioma).text

with open("resultados.txt", "rb") as file:
    btn = st.download_button(
            label="Download results",
            data=file,
            file_name="resultados.txt"
          )


