import requests
from difflib import SequenceMatcher as SM
import random
import json

def lambda_handler(event, context):
    print(event)
    direccion = event["queryStringParameters"]["direccion"]
    nombre = event["queryStringParameters"]["nombre"]

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
        #fields="&fields=name%2Cgeometry%2Cbusiness_status%2Ctype%2Curl%2Ccurrent_opening_hours%2Cdelivery%2Cformatted_phone_number%2Cplace_id%2Cprice_level%2Crating%2Creviews%2Ctypes%2Curl%2Cuser_ratings_total%2Cwebsite"
        fields = "&fields=address_component,adr_address,business_status,formatted_address,geometry,name,place_id,type,url,current_opening_hours,formatted_phone_number,opening_hours,website,delivery,price_level,rating,review,user_ratings_total"

        # fields="&fields=geometry"
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
            return result
        else:
            result = busquedaIdGoogle(google)
            return result

    result = chida(nombre)

    return {
    
        'statusCode': 200,
        'body': json.dumps(result)
        
    }
