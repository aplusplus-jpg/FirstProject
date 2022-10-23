import json
from pickletools import read_uint1
import re
import requests
import random

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

def lambda_handler(event, context):
    print(event)
    direccion = event["queryStringParameters"]["direccion"]
    nombre = event["queryStringParameters"]["nombre"]
    
    
    
    tokens_denue = ["d477dd27-255c-4449-baef-957ee33e94b6","3364a743-4c46-4528-985c-5a01d6fcaf8a","99a7f211-3b4a-4a18-5254-dac3c479840e",
                    "5e57ddfb-688e-4c78-a3d5-1898fd356ba3","c5135a58-1123-4d5f-927a-dd3773ae564c","56984dff-3daf-4328-afeb-66175d877b38",
                    "300bebf9-6de0-4d8a-a3fb-b5fd9b2a6acc","e04a9d5d-7267-4e21-9868-4b2468ebe1fd","de354429-5a37-4dee-bf77-75464e2abd7c",
                    "f1a899c7-9f92-4600-b324-2eb0b65e4b57","75c7770c-c24c-4a00-1da2-f52eec3a3a26","3769ef57-9ed9-40d6-aec9-a5262dc27304",
                    "2f14a0f0-c2ef-48cf-bab7-a0f82282a409","c6709043-0fdd-4772-a7df-4e0d36a12773"]

    def url_denue_nombre(nombre,entidad_federal):
        a = random.randint(0,len(tokens_denue))
        return f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{nombre}/{entidad_federal}/1/10/{tokens_denue[a]}"

        
    def buscarEntidad(direccion):
        for i in entidades:
            if i in direccion.lower():
                return llaves[i]
        return "00"    
    
    def buscarNombreDenue(nombre,direccion):
        entidad_federal = buscarEntidad(direccion)
        nombre = nombre.replace("'"," ")
        url = url_denue_nombre(nombre,entidad_federal)
        return requests.get(url).json()
    
    
    result = buscarNombreDenue(nombre, direccion)
    if result == "No hay resultados.":
        pass
    else:
        result = json.dumps(result[0])
    # result = "HOla fallo"
    # result = json.dumps(result)
    # if http_method == "GET" and event['queryStringParameters']['query']:
    #     nombre = event['queryStringParameters']['nombre']
    #     direccion = event['queryStringParameters']['direccion'']
    #     result = {"nombre":nombre,"direccion":direccion}
    return {
    
        'statusCode': 200,
        'body': result
        
    }
