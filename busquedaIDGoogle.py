import requests
    
def busquedaIdGoogle(id):
    url="https://maps.googleapis.com/maps/api/place/details/json?place_id="+id
    fields="&fields=business_status%2Ctype%2Curl%2Ccurrent_opening_hours%2Cdelivery%2Cformatted_phone_number%2Cplace_id%2Cprice_level%2Crating%2Creviews%2Ctypes%2Curl%2Cuser_ratings_total%2Cwebsite"
    token_api_google = "&key=AIzaSyDRhQ9HRGDmnGI6Rd79x1fp-vhCaWoJeYo"
    url=url+fields+token_api_google
    print(url)

    response = requests.request("GET", url, headers={}, data={})
    return response.json()

place_id = 'ChIJFS9ULan_0YUR2oDnXuItc58'

lista_address_components = busquedaIdGoogle(place_id)['result']
print(lista_address_components)