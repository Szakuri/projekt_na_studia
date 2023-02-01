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


# # home_mecze_moc = home_77(mecze_moc)



def opcjeRezultatu(team1,team2,array):
    team1 += 77
    if team1 > team2:
        larger = team1
        smaller = team2
    else:
        larger = team2
        smaller = team1

    team_diff = larger - smaller

 

    if team_diff >= 500:
        chance = random.random()
        if chance <= 0.9:
            array.append(larger)
        elif chance <= 0.95:
            array.append("Remis")
        elif chance > 0.95:
            array.append(smaller)


    elif team_diff >= 300:
        chance = random.random()
        if chance <= 0.75:
            array.append(larger)
        elif chance <= 0.9:
            array.append("Remis")
        elif chance > 0.9:
            array.append(smaller)

    elif team_diff >= 200:
        chance = random.random()
        if chance <= 0.6:
            array.append(larger)
        elif chance <= 0.85:
            array.append("Remis")
        elif chance > 0.85:
            array.append(smaller)

    elif team_diff >= 150:
        chance = random.random()
        if chance <= 0.5:
            array.append(larger)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(smaller)
        
    elif team_diff >= 100:
        chance = random.random()
        if chance <= 0.4:
            array.append(larger)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(smaller)

    elif team_diff >= 50:
        chance = random.random()
        if chance <= 0.3:
            array.append(larger)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(smaller)

    elif team_diff < 50:
        chance = random.random()
        if chance <= 0.25:
            array.append(larger)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(smaller)




def porównywarka(array_home):
    zwycięzca = []
    for i in range(0,len(array_home) - 1,2):
        opcjeRezultatu(array_home[i],array_home[i+1],zwycięzca)
    return zwycięzca


winnersi = porównywarka(mecze_moc)





def mocNaNazwe(array, dict):
    for i, item in enumerate(array):
        for k, ov in dict.items():
            if item == ov:
                array[i] = k
    return array


winnersi = mocNaNazwe(winnersi, overall)

print(winnersi)

