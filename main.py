import pandas as pd
import numpy as np
import os
from functions import *




excel_file= 'EkstraklasaMoc.xlsx'

excel_file_delete = "MeczeRezultaty.xlsx"

if os.path.exists(excel_file_delete):
    os.remove(excel_file_delete)
    print(f"Plik {excel_file_delete} został usunięty pomyślnie.")
else:
    print(f"Plik {excel_file_delete} nie istnieje.")


es = pd.read_excel(excel_file, usecols=["KLUB","SUMA"])

kluby = es['KLUB'].values.tolist()
suma = es['SUMA'].values.tolist()


overall = dict(zip(kluby, suma))



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


winnersi = porównywarka(mecze_moc)






winnersi = mocNaNazwe(winnersi, overall)


new_em = pd.DataFrame({"Rezultaty": winnersi})

new_em.to_excel("rezultaty.xlsx",index=False)

mix_em = pd.concat([em,new_em],axis=1)

mix_em.to_excel("MeczeRezultaty.xlsx",index=False)

excel_file_3 = "MeczeRezultaty.xlsx"

excel_file_4 = "Wynik końcowy na koniec sezonu.xlsx"




    
filesOpenAndClose(excel_file_3,excel_file_4)


finish = pd.read_excel(excel_file_4, usecols=["KLUB","PKT"])


finish.sort_values(by='PKT',ascending=False, inplace=True)

print(finish.to_string(index=False))

