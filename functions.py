

def start():
    import os
    print("Dzień dobry! Przedstawiam program współpracujący z arkuszami kalkulacyjnymi, mający na celu sprawdzić przewidywany tegoroczny sezon Ekstraklasy. Jeśli chcemy poznać now")




def menu():
    print("Menu Główne")






def opcjeRezultatuT1(lg,sm,diff,array):
    import random
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
    import random
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



def mocNaNazwe(array, dict):
    for i, item in enumerate(array):
        for k, ov in dict.items():
            if item == ov:
                array[i] = k
    return array


def filesOpenAndClose(file1,file2):
    import os
    import time
    os.startfile(file1)   
    time.sleep(1)   
    os.startfile(file2)
    file1.exit()


 