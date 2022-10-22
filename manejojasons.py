import json
from principal import*

def jasonalista(jason):
    return json.loads(jason)

dire="REGINA 135 ACCE A CENTRO AREA 9 CUAUHTEMOC 6090 125 126 CDMX"
nom="CENTRO PAPELERO SUN-RISE SA DE CV"
prueba = Alrededores_google(dire, nom)
print(prueba.map(jasonalista))