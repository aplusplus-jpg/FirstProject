import requests
import pandas as pd
from Direccion import *

def flatJson(json):
    '''Toma un json, lo aplana y regresa una lista'''
    Keys=['business_status', 'current_opening_hours', 'delivery', 'formatted_phone_number', 'place_id', 'rating', 'reviews', 'types', 'url', 'user_ratings_total', 'website']
    lista=[]

    for key in Keys:
        
        if key=='current_opening_hours':

            df1 = pd.json_normalize(json['result'][key]['periods']  , sep='_')
            lista.append(json['result'][key]['open_now'])
            lista.append(df1.values.tolist())
            lista.append(json['result'][key]['weekday_text'])
            continue
        
        if key=='reviews':
            try:
                for i in range(6):
                    df1=pd.json_normalize(json['result'][key][i], sep='_')
                    lista.append(df1.values.tolist())


            except Exception as e:

                continue
            continue
        lista.append(json['result'][key])
    print(lista)


flatJson(json)
"""['OPERATIONAL', True, [['2022-10-28', 5, '2359', True, '2022-10-22', 6, '0000', True]], ['Monday: Open 24 hours', 'Tuesday: Open 24 hours', 'Wednesday: Open 24 hours', 'Thursday: Open 24 hours', 'Friday: Open 24 hours', 'Saturday: Open 24 hours', 'Sunday: Open 24 hours'], True, '800 072 6722', 'ChIJFS9ULan_0YUR2oDnXuItc58', 4, [['Sergio Mendoza', 'https://www.google.com/maps/contrib/101711308695073375239/reviews', 'en', 'en', 'https://lh3.googleusercontent.com/a-/ACNPEu-swCIDBraZOp7qc53XCawotKoM81bzV3Wev-_L0tY=s128-c0x00000000-cc-rp-mo-ba5', 5, '5 years ago', 'Expensive but good variety pharmacy', 1490791031, False]], [['Joshua Castro', 'https://www.google.com/maps/contrib/107476593406833646576/reviews', 'en', 'en', 'https://lh3.googleusercontent.com/a-/ACNPEu-bGY0JQqJ30SehK2av6hjm-it27BQGQebWE-iuSw=s128-c0x00000000-cc-rp-mo-ba3', 5, '5 years ago', 'Nice', 1487826847, False]], [['raul acosta', 'https://www.google.com/maps/contrib/103882183736214876789/reviews', 'es', 'es', 'https://lh3.googleusercontent.com/a/ALm5wu2Zy8VTBtHHlDYCI9LHAhSJyApLJH-E_6dwtqU6=s128-c0x00000000-cc-rp-mo', 2, '3 months ago', 'Súper concurrido y más de 2 horas para prueba Covid. Busqué opciones y me fui a Pharmafam (Metro Etiopía), prueba de antígenos $350 y no hay nada de gente, consultorio súper limpio y excelente atención. Te dan resultado por escrito y digital a tu correo.', 1656180415, False]], [['C. G.', 'https://www.google.com/maps/contrib/112269348322247389494/reviews', 'en-US', 'es', 'https://lh3.googleusercontent.com/a/ALm5wu2-KwzcLA32V9xnBjgpDtT_9dY9Tv2FwSqLEBw=s128-c0x00000000-cc-rp-mo', 1, '3 months ago', 'Terrible service, more than an hour waiting because "they were cleaning" and they were eating. The lady at reception [stocky with long black hair] is 
arrogant and disrespectful to customers.', 1658682852, True]], [['José Antonio Pedraza Pérez', 'https://www.google.com/maps/contrib/105059887162258754531/reviews', 'en-US', 'es', 'https://lh3.googleusercontent.com/a-/ACNPEu-NlnpwK5czzgZ9H18VGdLmY0TrESLT9yIzO-QWfP8=s128-c0x00000000-cc-rp-mo-ba5', 2, 'a year ago', 'It is very cool how people who want to 
take a COVID test are trained with all the others, go to the BOX with all the others, and register in the same NOTEBOOK with the same PEN tied. BTW the shifts no longer use them, but since they do not warn or turn off the machine, everyone continues to bite it and continues to issue tickets that are thrown all over the place. It is not advisable to go 
through the remainder of the Pandemic.', 1629062804, True]], ['pharmacy', 'drugstore', 'store', 'health', 'point_of_interest', 'establishment'], 'https://maps.google.com/?cid=11489577524630356186', 220, 'https://www.farmaciasanpablo.com.mx/']"""