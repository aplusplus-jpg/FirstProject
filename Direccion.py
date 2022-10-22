from dataclasses import fields
import pandas as pd
import requests
from urllib import response


def busqueda_id_google(id):
    url="https://maps.googleapis.com/maps/api/place/details/json?place_id="+id
    fields="&filds=name"
    token_api_google = "&key=AIzaSyDRhQ9HRGDmnGI6Rd79x1fp-vhCaWoJeYo"
    payload={}
    headers = {}
    url=url+fields+token_api_google
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
id="Ek5WZXJzbyA4OSwgSmFpbWUgVG9ycmVzIEJvZGV0LCBUbMOhaHVhYywgMTM1MzAgU2FuIEp1YW4gSXh0YXlvcGFuLCBDRE1YLCBNZXhpY28iMBIuChQKEgnlxCWjRhvOhRE5SpX8QUfMgxBZKhQKEgl7nF-9RhvOhRFLFd1H7q8i8g"    
busqueda_id_google(id)
