token = "AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
from audioop import add
import requests
import pandas as pd
import json


def replace_text_search(text):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="&fields=formatted_address%2Cname%2Cbusiness_status%2Cgeometry%2Cplace_id%2Ctype"
    return base_url + text +fields+ token_i
def replace_text(text):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
    token_i = "&key=AIzaSyD9Jg7-4i7hnAQ7vXaCBaOSBZqdwdloHKg"
    fields="&fields=formatted_address%2Cname%2Cbusiness_status%2Cgeometry%2Cplace_id%2Ctype"
    imput_type="&inputtype=textquery"
    base_url= base_url + text+imput_type +fields+ token_i
    print(base_url.replace(" ","%20"))
    return base_url.replace(" ","%20")


pymes_df = pd.read_csv("https://raw.githubusercontent.com/arielmerinos/A-first-Shiny-project/main/examples.csv",
                       names=['name', 'address'])

def find_by_address():
    for add_pyme in pymes_df['address']:
        response = requests.request("GET", replace_text_search(add_pyme), headers={}, data={})
        print(response.text)
def find_by_name():
    i=1
    for add_pyme in pymes_df['name']:
        response=requests.request("GET", replace_text(add_pyme), headers={}, data={})
        print(response.json())
        
