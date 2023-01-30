import pandas as pd
import numpy as np

excel_file= 'EkstraklasaMoc.xlsx'


df = pd.read_excel(excel_file)

print(df.head())

print(df)