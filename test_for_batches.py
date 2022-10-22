import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/aplusplus-jpg/resources/main/csv1.csv?token=GHSAT0AAAAAABYSA5PPWIJQVIRWAOU7FYQOY2T6P4A', header=0)
df = pd.read_csv('../resources/csv1.csv', header=0)
#print(df.info())

df["direccionk"] = df["Direccion1"].map(str)  + " "+ df["Direccion2"].map(str) + " " + df["Direccion3"].map(str) + " " +df["Colonia"].map(str) + " " + df["MunicipioDel"].map(str) + " " + df["Estado"].map(str) + df["CP"].map(str)
#print(df.head())  
#print(df.tail())  


print(range(len(df.columns) - 1))
for i in range(len(df.columns) - 1):
    print(df.columns[i])
    if df.columns[i] not in ["NombComp", "direccion"]:
        del df[df.columns[i]]

#print(df.info())
