import pandas as pd

def manejo(url):
    '''Recibe un csv, lo convierte a data frame'''
    data = pd.read_csv(url)
    data['Direccion'] = data['Direccion1'].map(str) + ' ' + data['Direccion2'].map(str) + ' ' + data['Direccion3'].map(str)
    
    for i in range(len((data.columns))):
        if data.column[i] not in ['NombComp', 'Direccion']:
            del data[i]
    
    print(data.info())