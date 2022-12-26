# Programowanie komponentowe - projekt zaliczeniowy zespołowy


## Draft projektu

Projekt zaliczeniowy ma składać się z:
- GUI
- skryptu wykonującego konkretne akcje

Naszą propozycją projektu zaliczeniowego jest prosty program obsługujący sortowanie plików z wybranego folderu do innych, wskazanych folderów. Uzytkownik powinien móc:

- Stworzyć prosty config (tj. przypisać konkretne rozszerzenia plików do konkretnych folderów - pamiętając o tym, ze to samo rozszerzenie nie moze pojawic sie w dwoch roznych folderach)
- Wskazac co powinno dziac sie z pozostalymi (tj. takmi, ktorych rozszerzenia nie zostaly zdefiniowane w configu) plikami:
    - Powinny zostać pominięte
    - Powinny wylądować w innym, zbiorczym folderze (np.: Trash, Others etc.)
- Uruchomić i zatrzymać skrypt
    - Fajnie by było, gdybyśmy zrobili to z udziałem paczki watchdog (https://pythonhosted.org/watchdog/quickstart.html#a-simple-example), bo dzięki temu ten skrypt mógłby sobie chodzić w tle i sortować ciągle pliki (np.: pobieramy coś po prostu do Downloads i to odrazu ląduje tam gdzie chcemy)
    
- Załadować juz istniejacy config lub wybrany ze sciezki, którą wskaze
- Modyfikować config (przy wylaczonym skrypcie)
- Sprawdzić historię działań na plikach (powinniśmy logować to co się dzieje z plikami, na wypadek gdyby coś się zgubiło czy w ogóle byłaby potrzeba odtworzenia tego co się działo)


# 

TODO:
- [x] GUI
- [ ] Logowanie plików (logger)
- [ ] Tworzenie, modyfikowanie, zapisywanie i wczytywanie gotowego configu
- [ ] Sortowanie plików
