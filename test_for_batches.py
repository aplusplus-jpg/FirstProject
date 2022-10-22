import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/aplusplus-jpg/resources/main/csv1.csv?token=GHSAT0AAAAAABYSA5PPWIJQVIRWAOU7FYQOY2T6P4A', header=0)
df = pd.read_csv('../resources/csv1.csv', header=0)
print(df.info())

df["direccion"] = df["Direccion1"]  + " "+ df["Direccion2"] + " " + df["Direccion3"] + " " +df["Colonia"] + " " + df["MunicipioDel"] + " " + df["Estado"] + str(df["CP"])
print(df.head())  
print(df.tail())  
