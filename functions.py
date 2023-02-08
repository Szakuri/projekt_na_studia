
def linia():
    print("====================================")


def path():
    import os
    return os.path.dirname(os.path.abspath("MeczeRezultaty.xlsx"))




# def closeExcel():
#     import win32com.client as win
#     x = path()

#     path_excel_1 = f"{x}\MeczeRezultaty.xlsx"


#     x1 = win.gencache.EnsureDispatch("Excel.Application")
#     x2 = x1.Workbooks.Open(path_excel_1)
#     x2.Close(SaveChanges=False)
#     x1.Quit()
#     menu()


def start():
    print("Dzień dobry! Przedstawiam program współpracujący z arkuszami kalkulacyjnymi, mający na celu sprawdzić przewidywany tegoroczny sezon Ekstraklasy. Wybierz jedną z opcji aby przejść dalej.")
    


def menu():
    linia()
    print("Menu Główne")
    linia()
    print("1. Rozpocznij przewidywania sezonu")
    print("2. Poznaj siłę drużyn")
    print("3. Wyjście")
    try:
        wybor = int(input("Wybierz opcję [1-3]: "))
        linia()
        if wybor == 1:
            opcja_1()
        elif wybor == 2:
            opcja_2()
        elif wybor == 3:
            wyjscie()
        else:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")
            menu()
    except ValueError:
        print("Program został już wcześniej otwarty!")


def opcja_1():
    

    import pandas as pd
    import numpy as np
    import os
    import time

    

    excel_file= 'EkstraklasaMoc.xlsx'
    excel_file_delete = "MeczeRezultaty.xlsx"


    try:
        if os.path.exists(excel_file_delete):
            os.remove(excel_file_delete)
            print(f"Plik {excel_file_delete} został usunięty pomyślnie.")
        else:
            print(f"Plik {excel_file_delete} nie istnieje.")
    except PermissionError:
        print("Plik MeczeRezultaty.xlsx jest już otwarty. Zamknij go i ponownie wybierz opcję 1")
        menu()

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


    excel_file_4 = "Wynik na koniec sezonu.xlsx"


    filesOpen(excel_file_3)

    filesOpen(excel_file_4)

    print("Ładowanie plików z wynikami... .Potrwa to kilka sekund")

    pathSave = path()

    # fileSave(f"{pathSave}\{excel_file_4}")

    time.sleep(5)

    finish = pd.read_excel(excel_file_4, usecols=["KLUB","PKT"])


    finish.sort_values(by='PKT',ascending=False, inplace=True)

    print(finish.to_string(index=False))

    menu()


def opcja_2():
    import pandas as pd
    excel_file = "EkstraklasaMoc.xlsx"
    moc = pd.read_excel(excel_file, usecols=["KLUB","SUMA"])
    moc.sort_values(by='SUMA',ascending=False, inplace=True)
    print(moc.to_string(index=False))
    menu()




def wyjscie():
    pass



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


def filesOpen(file1):
    import os
    import time
    os.startfile(file1)   
    time.sleep(2)   

# def fileSave(path):
#     import win32com.client as win
#     x1 = win.gencache.EnsureDispatch("Excel.Application")
#     x2 = x1.Workbooks.Open(path)
#     x2.Save()
#     x1.Quit()

