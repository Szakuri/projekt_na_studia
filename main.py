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



mecze_moc = [0] * len(mecze)

for i, item in enumerate(mecze):
    for klub in overall:
        if item[:5] == klub[:5]:
            mecze_moc[i] = overall[klub]
            break


def home_77(array_home):
    for i in range(len(array_home)):
        if i % 2 == 1:
            array_home[i] -= 77
    return array_home


home_mecze_moc = home_77(mecze_moc)



def porównywarka(array_home):
    zwycięzca = []
    for i in range(0,len(array_home) - 1,2):
        if array_home[i] > array_home[i + 1]:
            zwycięzca.append(array_home[i])
        else:
            zwycięzca.append(array_home[i + 1])
    return zwycięzca

winnersi = porównywarka(home_mecze_moc)

print(winnersi)