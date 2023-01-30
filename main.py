import pandas as pd
import numpy as np

excel_file= 'EkstraklasaMoc.xlsx'


es = pd.read_excel(excel_file, usecols=["KLUB","SUMA"])

kluby = es['KLUB'].values.tolist()
suma = es['SUMA'].values.tolist()


overall = dict(zip(kluby, suma))


print(overall)

overall = {
    klub.replace(' ',''): ov
    for klub, ov in overall.items()
}

for klub, ov in overall.items():
    exec(f"{klub}={repr(ov)}")

print(ZagłębieLubin)