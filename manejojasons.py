import json
import reviewsFromDetails as rfd

def jasonalista(jason):
    '''Toma un json y devuelve un df con nombre de columna de la clave
    del jason'''
    return json.loads(jason)

dire="REGINA 135 ACCE A CENTRO AREA 9 CUAUHTEMOC 6090 125 126 CDMX"
nom="CENTRO PAPELERO SUN-RISE SA DE CV"
prueba = Alrededores_google(dire, nom)
print(prueba.map(jasonalista))