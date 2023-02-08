# projekt_na_studia

Projekt tworzony w języku Python w celu zaliczenia przedmiotu.

Wersja Python 3.10.9

Program który wykonałem ma za pomocą dużej ilości zmiennych obliczać za pomocą algorytmów predykcję, kolejnego sezonu polskiej 1 ligi piłki nożnej tzw. Ekstraklasy.

Strona która pomogła mi uzbierać dane na temat drużyn: https://ekstrastats.pl/

Aplikacja którą musiałem pobrać, żeby móc dołączyć arkusz kalkulacyjny na Github: Git XL, instalując ją przy użyciu komendy:

git xl install

Na diagnozowanie danych z Excel w Pythonie użyłem biblioteki pandas oraz openpyxl,
obie zainstalowałem poleceniem pip install.

=============================================

INSTRUKCJA DZIAŁANIA PROGRAMU:

Program ma główną funkcję: Przewidywać rezultaty meczów na podstawie innych danych. Arkusz kalkulacyjny taki jak Ekstraklasa-Statystyki.xlsx miałbyć jedynie pomocniczym arkuszem, który pomógł mi wyliczyć ilość punktów, które robiłem według swojego wzoru.

Funkcje znajdują się w pliku functions.py, żeby można było sobie podejrzeć całe działanie programu a szczególnie funkcji opcja_1

(Opcja 1) Na samym początku program pobiera potrzebne biblioteki, potrzebne do działania paru funkcji.
Usuwa plik MeczeRezultaty.xlsx ponieważ, chciałem uniknąć tworzenia kopii arkusza, żeby nie zrobić większego śmietniku w pliku projektu.

Następnie pobiera dane 2 kolumn z arkusza EkstraklasaMoc.xlsx i tworzy z nich listy, którą później przerabia na klucz i wartość w dzienniku.

Kolejnym etapem jest pobranie kolejnej listy, ze wszystkimi meczami odbywającymi się w tegorycznym sezonie Ekstraklasy. I utworzenie z każdego meczu listy w liście.

Później program zamienił każdą drużynę na ilość punktów jakie posiadają, do tego właśnie potrzebowałem dziennika i listy.

Dalsza część to po prostu porównywanie punktów w każdym meczu i tworzenie dla każdej możliwości. Im większa była przewaga punktowa tym rosła szansa na zwyciężenie w spotkaniu, jesli przewaga była mała rosła szansa na remis. Rezultatem była albo ilość punktów drużyny zwycięskiej albo napis "Remis"

Kolejną funkcja powodowała odszyfrowanie ilości punktów drużyny zwycięskiej na przypisaną jej drużynę oraz utworzenie z niej listy.

Następnie utworzenie arkusza pomocniczego który spisywał wszystkie rezultaty spotkań, bez biorących w nich udziału drużyn o nazwie rezultaty.xlsx

Następnie program połączył wcześniej już istniejącą tabelę EkstraklasaMecze.xlsx z pomocniczym arkuszem rezultaty.xlsx

Przygotowany już wcześniej arkusz kalkulacyjny "Wynik na koniec sezonu.xlsx" oblicza ilość wygranych, porażek i remisów danej drużyny i obliczał punkty, na podstawie punktacji piłkarskiej.

Program otwiera arkusze kalkulacyjne, ponieważ arkusz "Wynik na koniec sezonu.xlsx" musi wcześniej widzieć jakie były rezultaty (Arkusze są ze sobą podpięte)

Program zczytuje i wyświetla dane w kolejności od najlepszej do najgorszej drużyny sezonu. (Wyświetla dane poprzedniego przewidywania, ze względu na to że arkusz Wynik na koniec sezonu nie zapisuje się przed pobieraniem z jego danych.)

UWAGA WAŻNE! Próbowałem zautomatyzować zapisywanie pliku i wyłączanie, lecz niestety musiałem usunąć tą opcję, ponieważ robiła anomalia wynikowe oraz tworzyły się kopie arkusza, ponieważ ten stawał się plikiem do odczytu.
Żeby program rozpoczął przewidywanie po wybraniu opcji 1, musimy wcześniej wyłączyć arkusz MeczeRezultaty.xlsx, oraz żeby otrzymywać odświeżone końcowe dane, zapisywać plik Wynik na koniec sezonu.xlsx.
