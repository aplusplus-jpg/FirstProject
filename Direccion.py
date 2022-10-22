
from main import *
import requests

    
def Alrededores_google(dir,nombre):
    coordenadas=address_to_coordinates(dir)
    print("dir",dir)
    print("coord",coordenadas)
    url=url_google_alrededores(coordenadas[0],coordenadas[1],50,nombre)
    response=requests.request("GET",url,headers={},data={})
    return response




