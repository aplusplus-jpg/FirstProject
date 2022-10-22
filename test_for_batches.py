import pandas as pd


def concatenateDataFrame(path, newPath):
    """
    Create a new dataset with concatenated columns
    """
    df = pd.read_csv(path, header=0)
    nf = pd.DataFrame()
    nf['nombre'] = df['NombComp']
    nf["direccion"] = df["Direccion1"].map(str)  + " "+ df["Direccion2"].map(str) + " " + df["Direccion3"].map(str) + " " +df["Colonia"].map(str) + " " + df["MunicipioDel"].map(str) + " " + df["Estado"].map(str) + df["CP"].map(str)
    nf.to_csv(newPath)


for i in range(1, 6):
    concatenateDataFrame(f"../resources/csv{i}.csv", f"../resources/new{i}.csv")