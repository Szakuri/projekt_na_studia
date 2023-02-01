import pandas as pd
import numpy as np
import random

excel_file= 'EkstraklasaMoc.xlsx'


es = pd.read_excel(excel_file, usecols=["KLUB","SUMA"])

kluby = es['KLUB'].values.tolist()
suma = es['SUMA'].values.tolist()


overall = dict(zip(kluby, suma))


print(overall)

# overall = {
#     klub.replace(' ',''): ov
#     for klub, ov in overall.items()
# }

# for klub, ov in overall.items():
#     exec(f"{klub}='{ov}'")


excel_file_2= 'EkstraklasaMecze.xlsx'

em = pd.read_excel(excel_file_2, usecols=["TEAM1","TEAM2"])




gospodarz = em['TEAM1'].values.tolist()
gość = em['TEAM2'].values.tolist()


# mecze = [m for m in zip(gospodarz, gość)]

mecze = [m for pair in zip(gospodarz,gość) for m in pair]


for i, klub in enumerate(mecze):
    mecze[i] = klub.strip()

print(mecze)



mecze_moc = [0] * len(mecze)

for i, item in enumerate(mecze):
    for klub in overall:
        if item[:5] == klub[:5]:
            mecze_moc[i] = overall[klub]
            break


print(mecze_moc)

