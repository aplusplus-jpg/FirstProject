from email import header
import pandas as pd

def manejo(url):
    '''Recibe un csv, lo convierte a data frame'''
    data = pd.read_csv(url)
    for i in range(data.shape()):
        print(i)


manejo('https://raw.githubusercontent.com/aplusplus-jpg/resources/main/csv1.csv?token=GHSAT0AAAAAAB2IDGE6VGRY4IZOZUCZZFAWY2TPI6Q', header=None)
#print(manejo('https://raw.githubusercontent.com/aplusplus-jpg/resources/main/csv1.csv?token=GHSAT0AAAAAAB2IDGE6VGRY4IZOZUCZZFAWY2TPI6Q'))
