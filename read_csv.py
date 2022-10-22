import pandas as pd
from tkinter import filedialog as fd


csv = pd.read_csv('C:\Users\Oceloconetl\FirstProject')
#csv[:5000].to_csv()
renglones = csv.shape(500) // 6