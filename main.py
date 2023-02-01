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


# def home_77(array_home):
#      for i in range(len(array_home)):
#          if i % 2 == 1:
#              array_home[i] -= 77
#      return array_home


# # home_mecze_moc = home_77(mecze_moc)

def opcjeRezultatuT1(lg,sm,diff,array):
    if diff >= 500:
        chance = random.random()
        if chance <= 0.9:
            array.append(lg-77)
        elif chance <= 0.95:
            array.append("Remis")
        elif chance > 0.95:
            array.append(sm)


    elif diff >= 300:
        chance = random.random()
        if chance <= 0.75:
            array.append(lg-77)
        elif chance <= 0.9:
            array.append("Remis")
        elif chance > 0.9:
            array.append(sm)

    elif diff >= 200:
        chance = random.random()
        if chance <= 0.6:
            array.append(lg-77)
        elif chance <= 0.85:
            array.append("Remis")
        elif chance > 0.85:
            array.append(sm)

    elif diff >= 150:
        chance = random.random()
        if chance <= 0.5:
            array.append(lg-77)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(sm)
        
    elif diff >= 100:
        chance = random.random()
        if chance <= 0.4:
            array.append(lg-77)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(sm)

    elif diff >= 50:
        chance = random.random()
        if chance <= 0.3:
            array.append(lg-77)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(sm)

    elif diff < 50:
        chance = random.random()
        if chance <= 0.25:
            array.append(lg-77)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(sm)


def opcjeRezultatuT2(lg,sm,diff,array):
    if diff >= 500:
        chance = random.random()
        if chance <= 0.9:
            array.append(lg)
        elif chance <= 0.95:
            array.append("Remis")
        elif chance > 0.95:
            array.append(sm-77)


    elif diff >= 300:
        chance = random.random()
        if chance <= 0.75:
            array.append(lg)
        elif chance <= 0.9:
            array.append("Remis")
        elif chance > 0.9:
            array.append(sm-77)

    elif diff >= 200:
        chance = random.random()
        if chance <= 0.6:
            array.append(lg)
        elif chance <= 0.85:
            array.append("Remis")
        elif chance > 0.85:
            array.append(sm-77)

    elif diff >= 150:
        chance = random.random()
        if chance <= 0.5:
            array.append(lg)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(sm-77)
        
    elif diff >= 100:
        chance = random.random()
        if chance <= 0.4:
            array.append(lg)
        elif chance <= 0.8:
            array.append("Remis")
        elif chance > 0.8:
            array.append(sm-77)

    elif diff >= 50:
        chance = random.random()
        if chance <= 0.3:
            array.append(lg)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(sm-77)

    elif diff < 50:
        chance = random.random()
        if chance <= 0.25:
            array.append(lg)
        elif chance <= 0.75:
            array.append("Remis")
        elif chance > 0.75:
            array.append(sm-77)

    


def porównywarkaMocy(team1,team2,array):
    team1 += 77
    if team1 > team2:
        larger = team1
        smaller = team2
        team_diff = larger - smaller
        opcjeRezultatuT1(larger,smaller,team_diff,array)
    else:
        larger = team2
        smaller = team1
        team_diff = larger - smaller
        opcjeRezultatuT2(larger,smaller,team_diff,array)

    





    

 

    




def porównywarka(array_home):
    zwycięzca = []
    for i in range(0,len(array_home) - 1,2):
        porównywarkaMocy(array_home[i],array_home[i+1],zwycięzca)
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




new_em = pd.DataFrame({"Rezultaty": winnersi})

new_em.to_excel("rezultaty.xlsx",index=False)

mix_em = pd.concat([em,new_em],axis=1)

mix_em.to_excel("MeczeRezultaty.xlsx",index=False)

