import time
import datetime
import tkinter as tk
from tkinter import *
from pathlib import Path
import re

sciezka = str('baza_wypitych_trunkow.txt')

baza_danych = open(sciezka, 'a')
baza_danych.close()

tablica_danych = []
data = datetime.date.today()

okno = tk.Tk()
window_height = 350
window_width = 515
screen_width = okno.winfo_screenwidth()
screen_height = okno.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
okno.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

okno.title("Alkomierz 2.5G Alpha")
okno.configure(background='seagreen')
okno.resizable(False, False)
okno.wm_iconbitmap('ikona.ico')


def menu_info():

    wyczysc_ramke()
    menu_gorna = tk.Frame(okno)
    menu_gorna.pack()
    menu_gorna.configure(background='gray')
    menu = tk.Menu(okno)
    okno.config(menu=menu)
    menu.add_command(labe="DODAJ TRUNEK", command=dodaj)
    menu.add_command(labe="SPIS WYPITYCH TRUNKÓW", command=podglad)
    menu.add_command(labe="O PROGRAMIE", command=info)
    menu.add_command(label="WYJŚCIE", command=zamykanie)
    opis = tk.Label(okno, text="\nWitaj w programie\n\n\n\n\n", fg="lightskyblue", bg="seagreen",
                    font='Helvetica 12 bold')
    opis2 = tk.Label(okno, text="A L K O M I E R Z\n", fg="brown", bg="seagreen", font='gothic 26 bold')
    opis3 = tk.Label(okno, text="\n\n\n\n\n\nTomasz Kasperek                                                      "
                                "           Wersja: 2.5G Alpha",
                     fg="lightskyblue", bg="seagreen", font='Helvetica 10 bold')
    opis.pack()
    opis2.pack()
    opis3.pack()


def dodaj():

    global ilosc
    global moc
    global opis
    global data2
    wyczysc_ramke()
    menu_gorna = tk.Frame(okno)
    menu_gorna.pack(side=TOP)
    menu_gorna.configure(background='darkseagreen')
    menu = tk.Menu(okno)
    okno.config(menu=menu)
    menu.add_command(labe="DODAJ TRUNEK", command=dodaj)
    menu.add_command(labe="SPIS WYPITYCH TRUNKÓW", command=podglad)
    menu.add_command(labe="O PROGRAMIE", command=info)
    menu.add_command(label="WYJŚCIE", command=zamykanie)
    kolejnosc = tk.Label(menu_gorna, text="WPISUJESZ " + str(ilosc_dawek()) + ". TRUNEK!",
                         bg="darkseagreen", fg="brown4",
                         font='Helvetica 14 bold')
    kolejnosc.pack()
    ilosc_tekst = tk.Label(menu_gorna, text="WPISZ ILOŚĆ WYPITEGO TRUNKU(ml)", bg='darkseagreen',
                           fg="gold",
                           font='Helvetica 11 bold')
    ilosc_tekst.pack()
    ilosc = Entry(menu_gorna)
    ilosc.pack()
    ilosc.focus_set()
    ilosc.get()
    moc_tekst = tk.Label(menu_gorna, text="\nWPISZ MOC WYPITEGO TRUNKU(%)", bg='darkseagreen',
                         fg="gold", font='Helvetica 11 bold')
    moc_tekst.pack()
    moc = Entry(menu_gorna)
    moc.pack()
    opis_tekst = tk.Label(menu_gorna, text="\nCO TO ZA TRUNEK?", bg="darkseagreen", fg="gold", font="Helvetica 11 bold")
    opis_tekst.pack()
    opis = Entry(menu_gorna)
    opis.pack()
    opis.get()
    data_tekst = tk.Label(menu_gorna, text="\nKIEDY GO WYPIŁEŚ?(PUSTE=DZIŚ)", bg="darkseagreen", fg="gold",
                          font="Helvetica 12 bold")
    data_format_tekst = tk.Label(menu_gorna, text="RRRR-MM-DD", bg="darkseagreen", fg="red",
                          font="Helvetica 8 bold")
    data_tekst.pack()
    data_format_tekst.pack()
    data2 = Entry(menu_gorna)
    data2.pack()
    data2.get()
    przerwa = tk.Label(menu_gorna, text="", bg="darkseagreen")
    przerwa.pack()
    przycisk_dodaj = tk.Button(menu_gorna, text="          DODAJ TRUNEK!          ", bg="seagreen2", command=spr_zap)
    przycisk_dodaj.pack(side=LEFT)
    przycisk_tosamo = tk.Button(menu_gorna, text="         TO CO OSTATNIO!         ", bg="seagreen2",
                                command=to_co_ostatnio)
    przycisk_tosamo.pack(side=RIGHT)


def podglad():

    if ilosc_element_baza() >= 5:
        try:
            wyczysc_ramke()
            menu_gorna = tk.Frame(okno)
            menu_gorna.pack(side=TOP, fill=X)
            menu_gorna.configure(background='seagreen')
            menu = tk.Menu(okno)
            okno.config(menu=menu)
            menu.add_command(labe="DODAJ TRUNEK", command=dodaj)
            menu.add_command(labe="SPIS WYPITYCH TRUNKÓW", command=podglad)
            menu.add_command(labe="O PROGRAMIE", command=info)
            menu.add_command(label="WYJŚCIE", command=zamykanie)
            scrollbar = Scrollbar(okno)
            lista_trun = Listbox(menu_gorna, yscrollcommand=scrollbar.set, bg="darkgreen", fg="gold",
                                 font='Helvetica 10 bold')
            scrollbar = Scrollbar(lista_trun)
            lista_trun.pack(side=TOP)
            scrollbar.config(command=lista_trun.yview)
            lista_trun.config(height=10, width=85)

            alkoholomierz()
            if ilosc_element_baza() <= 1:
                powrot()
            if ilosc_element_baza() >= 5:
                try:
                    pozycja = 0
                    pozycja = int(pozycja)
                    a, b, c, d = 2, 3, 4, 1
                    for lista_trunek, pozycja_trunek in enumerate(tablica_danych):
                        lista_trun.insert(END, str(pozycja + 1) + ".|    " + str(tablica_danych[pozycja + d]) +
                                          " WYPIŁEŚ " + str(tablica_danych[pozycja + a]) + "ml " +
                                          str(tablica_danych[pozycja + b]) + "% TRUNKU: " +
                                          str(tablica_danych[pozycja + c]))
                        lista_trun.see(tk.END)
                        if str(tablica_danych[pozycja + d]) != str(tablica_danych[pozycja + d + 4]):
                            lista_trun.insert(END, "-----------------------------------------------------------------"
                                                   "--------------------------------------------------------------")
                        pozycja = pozycja + 1
                        a = a + 3
                        b = b + 3
                        c = c + 3
                        d = d + 3
                except IndexError:
                    None

                przycisk_usun_trunek = tk.Button(menu_gorna, text="                     USUŃ OSTATNI TRUNEK        "
                                                                  "             ", bg="seagreen2", font='Helvetica 10 ',
                                                 command=pewien_usun_wpis)
                przycisk_usun_baze = tk.Button(menu_gorna, text="                     USUŃ BAZĘ DANYCH           "
                                                                "          ", bg="seagreen2", fg="red",
                                               font='Helvetica 10 bold', command=pewien_usun_baze)
                przycisk_usun_trunek.pack(side=LEFT)
                przycisk_usun_baze.pack(side=LEFT)

                menu_dolna = tk.Frame(okno)
                menu_dolna.pack(side=TOP, fill=X)
                menu_dolna.configure(background='seagreen')
                wyliczenia1 = Label(menu_dolna, text="\nOD " + dat + "(" + str(podglad_ile_dni()) + ") WYPIŁEŚ " +
                                                     str(ilosc_plynu()) + "L TRUNKÓW,\n W KTÓRYCH ZNAJDOWAŁO SIĘ "
                                                     + str(alkoholomierz()) + "g CZYSTEGO ALKOHOLU.",
                                    bg="seagreen", fg="gold",
                                    font='Helvetica 11 bold')
                wyliczenia2 = Label(menu_dolna, text=porownanie_do_polakow(),
                                    bg="seagreen", fg="blue",
                                    font='Helvetica 11 bold')
                wyliczenia3 = Label(menu_dolna, text="ŚREDNIO PODCZAS JEDNEGO POSIEDZENIA WYPIJASZ " +
                                                     str(srednia_posiadowy())
                                                     + "g CZYSTEGO ALKOHOLU.", bg="seagreen", fg="gold",
                                    font='Helvetica 9 bold')
                wyliczenia1.pack()
                wyliczenia2.pack()
                wyliczenia3.pack()
        except ValueError:
            usun_ostatni_wpis()
            podglad()

    else:
        wyczysc_ramke()
        menu_gorna = tk.Frame(okno)
        menu_gorna.pack()
        menu_gorna.configure(background='gray')
        menu = tk.Menu(okno)
        okno.config(menu=menu)
        menu.add_command(labe="DODAJ TRUNEK", command=dodaj)
        menu.add_command(labe="SPIS WYPITYCH TRUNKÓW", command=podglad)
        menu.add_command(labe="O PROGRAMIE", command=info)
        menu.add_command(label="WYJŚCIE", command=zamykanie)
        opis = tk.Label(okno, text="\nWitaj w programie\n\n\n\n\n", fg="lightskyblue", bg="seagreen",
                        font='Helvetica 12 bold')
        informacja = tk.Label(okno, text="BAZA JEST PUSTA!", fg="red2", bg="seagreen",
                        font='Helvetica 21 bold')
        informacja2 = tk.Label(okno, text="Dodaj pierwszy trunek", fg="red2", bg="seagreen",
                              font='Helvetica 10 bold')
        opis2 = tk.Label(okno, text="A L K O M I E R Z\n", fg="brown", bg="seagreen", font='gothic 26 bold')
        opis3 = tk.Label(okno,
                         text="\n\nTomasz Kasperek                                                      "
                              "           Wersja: 2.5G Alpha",
                         fg="lightskyblue", bg="seagreen", font='Helvetica 10 bold')
        opis.pack()
        opis2.pack()
        informacja.pack()
        informacja2.pack()
        opis3.pack()


def info():

    powrot()


def zamykanie():

    time.sleep(0.2)
    baza_danych.close()
    sys.exit()


def powrot():

    menu_info()


def wyczysc_ramke():

    for obiekty in okno.winfo_children():
        obiekty.destroy()


def ilosc_element_baza():

    wpis_bazy_do_tablicy()
    sztuki = len(tablica_danych)
    return int(sztuki)


def ilosc_dawek():

    wpis_bazy_do_tablicy()
    enty = (len(tablica_danych)) / 4
    enty = int(enty) + 1
    if enty == 0:
        enty = 1
    return enty


def usun_ostatni_wpis():

    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    okno_kom.destroy()
    if uwierzytelnienie() == 1:
        if ilosc_element_baza() > 5:
            wpis_bazy_do_tablicy()
            baza_danych = open(sciezka, 'w')
            us = len(tablica_danych) - 1
            us = int(us)
            tablica_danych.pop(us)
            us = len(tablica_danych) - 1
            us = int(us)
            tablica_danych.pop(us)
            us = len(tablica_danych) - 1
            us = int(us)
            tablica_danych.pop(us)
            us = len(tablica_danych) - 1
            us = int(us)
            tablica_danych.pop(us)
            wpis_tablicy_do_bazy()
            baza_danych.close()
        else:
            baza_danych = open(sciezka ,'w')
            baza_danych = open(sciezka ,'a')
            baza_danych.close()
        podglad()
    else:
        podglad()


def usun_baze():

    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    okno_kom.destroy()
    if uwierzytelnienie() == 1:
        baza_danych = open(sciezka, 'w')
        baza_danych = open(sciezka, 'a')
        baza_danych.close()
        podglad()
    else:
        podglad()


def alkoholomierz():

    global dat
    global czysty_alkohol
    pozycja = 0
    pozycja = int(pozycja)
    a = 2
    b = 3
    czyste = []
    try:
        while ilosc_element_baza() > pozycja:
            wpis_bazy_do_tablicy()
            czysta = float(int(tablica_danych[pozycja + a]) * (float(tablica_danych[pozycja + b]) / 100))
            czyste.append(czysta)
            pozycja += 1
            a += 3
            b += 3
    except IndexError:
        None

    if len(tablica_danych) != 0:
        czysty_alkohol = int(sum(czyste))
        dat = str(tablica_danych[1])
        return czysty_alkohol


def wpis_tablicy_do_bazy():

    poz = 0
    poz = int(poz)
    while len(tablica_danych) > poz:
        baza_danych = open(sciezka, 'a')
        baza_danych.write(str(tablica_danych[poz]) + "\n")
        baza_danych.close()
        poz = poz + 1
        baza_danych.close()


def wpis_bazy_do_tablicy():

    tablica_danych.clear()
    with open(sciezka, 'r') as zawartosc:
        for linia in zawartosc:
            linia = linia.replace("\n", "")
            linia = str(linia)
            tablica_danych.append(linia)
    baza_danych.close()


def nowy_trunek(ilosc, moc):

    baza_danych = open(sciezka, 'a')
    baza_danych.write(ilosc_element + "\n")
    baza_danych.write(moc_element + "\n")
    baza_danych.close()


def dni_wpisywania():

    data_start = tablica_danych[1]

    rok = data_start[0:4]
    rok = int(rok)
    miesiac = data_start[5:7]
    miesiac = int(miesiac)
    dzien = data_start[8:10]
    dzien = int(dzien)
    tab_data = [rok, miesiac, dzien]

    start = datetime.date(tab_data[0], tab_data[1], tab_data[2])
    today = datetime.date.today()
    interwal = today - start
    dni = int(interwal.total_seconds() / 86400)
    return dni


def zapisz_opis():

    global opis
    opis_trunku = opis.get()
    opis_trunku = str(opis_trunku)
    baza_danych = open(sciezka, 'a')
    baza_danych.write(opis_trunku + "\n")
    baza_danych.close()


def zapisz_date():

    data_trunku = data2.get()
    data_trunku = str(data_trunku)
    if data_trunku == "":
        wpis_bazy_do_tablicy()
        baza_danych = open(sciezka, 'a')
        baza_danych.write(str(data) + "\n")
        baza_danych.close()
    else:
        wpis_bazy_do_tablicy()
        baza_danych = open(sciezka, 'a')
        baza_danych.write((data_trunku) + "\n")
        baza_danych.close()


def ilosc_plynu():

    pozycja = 2
    pozycja = int(pozycja)
    ilosc_pl = []
    try:
        while ilosc_element_baza() > pozycja:
            wpis_bazy_do_tablicy()
            ilosc_plynu = int(int(tablica_danych[pozycja]))
            ilosc_pl.append(ilosc_plynu)
            pozycja += 4
            ilosc_suma = sum(ilosc_pl)
            ilosc_suma = ilosc_suma/1000
            ilosc_suma = float(ilosc_suma)
    except IndexError:
        None
    return ilosc_suma


def porownanie_do_polakow():

    dzielnik = dni_wpisywania()
    if dni_wpisywania() == 0:
        dzielnik = 1
    if alkoholomierz() / dzielnik > 30:
        return "PIJESZ WIĘCEJ("+str(porownanie_do_polakow_wartosc())+"g/dzień) NIŻ PRZECIĘTNY POLAK(30g/dzień)!"
    if alkoholomierz() / dzielnik < 30:
        return "PIJESZ MNIEJ("+str(porownanie_do_polakow_wartosc())+"g/dzień) NIŻ PRZECIĘTNY POLAK(30g/dzień)!"
    if alkoholomierz() / dzielnik == 30:
        return "PIJESZ TYLE CO PRZECIĘTNY POLAK(30g/dzień)!"


def porownanie_do_polakow_wartosc():

    if dni_wpisywania() == 0:
        return int(alkoholomierz() / 1)
    else:
        return int(alkoholomierz() / dni_wpisywania())


def podglad_ile_dni():

    if dni_wpisywania() == 0:
        return "DZIŚ"
    else:
        return str(dni_wpisywania()) + " DNI TEMU"


def srednia_posiadowy():

    pozycja = 1
    dni_picia = []
    try:
        for lista_trunek, pozycja_trunek in enumerate(tablica_danych):
            if str(tablica_danych[pozycja]) != str(tablica_danych[pozycja + 4]):
                dni_picia.append(tablica_danych[pozycja])
            pozycja += 4
    except IndexError:
        None
    return int(alkoholomierz() / (len(dni_picia) + 1))


def to_co_ostatnio():

    if ilosc_element_baza() >= 4:
        zapisz_date()
        wpis_bazy_do_tablicy()
        global ilosc_element
        global moc_element
        ilosc_element = tablica_danych[ilosc_element_baza()-4]
        ilosc_element = int(ilosc_element)
        moc_element = tablica_danych[ilosc_element_baza()-3]
        moc_element = float(moc_element)
        if ilosc_element > 1 and moc_element > 0.1 and ilosc_element <= 1000 and moc_element <= 100:
            ilosc_element = str(ilosc_element)
            moc_element = str(moc_element)
            nowy_trunek(ilosc_element, moc_element)
            opis_trunku = str(tablica_danych[ilosc_element_baza()-4])
            opis_trunku = str(opis_trunku)
            baza_danych = open(sciezka, 'a')
            baza_danych.write(opis_trunku + "\n")
            baza_danych.close()
            dodaj()
        else:
            dodaj()
    else:
        dodaj()


def pewien_usun_baze():

    global klucz_autoryzacyjny
    global okno_kom
    okno_kom = tk.Toplevel()
    window_height = 120
    window_width = 280
    screen_width = okno_kom.winfo_screenwidth()
    screen_height = okno_kom.winfo_screenheight()
    x_cordinate = int(okno.winfo_x() + (screen_width / 16.5))
    y_cordinate = int(okno.winfo_y() + (screen_height / 9))
    okno_kom.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    okno_kom.title("Usuwanie bazy")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="\nJESTEŚ PEWIEN?", bg="seagreen", fg="red4", font='Helvetica 12 bold')
    info3.pack()
    autoryzacja = tk.Label(ramka2, text="Klucz autoryzacyjny:", bg='seagreen', fg='red4', font='Helvetica 9 bold')
    autoryzacja.pack(side=LEFT)
    klucz_autoryzacyjny = Entry(ramka2)
    klucz_autoryzacyjny.pack(side=RIGHT)
    klucz_autoryzacyjny.get()
    klucz_autoryzacyjny.focus_set()
    przerwa = tk.Label(ramka2, text='\n', bg='seagreen')
    przerwa.pack()
    ramka3 = tk.Frame(okno_kom)
    ramka3.configure(bg='seagreen')
    ramka3.pack()
    tak = tk.Button(ramka3, text="    TAK    ", command=usun_baze, bg="red3")
    tak.pack(side=LEFT)
    przerwa2 = tk.Label(ramka3, text='               ', bg='seagreen')
    przerwa2.pack(side=LEFT)
    nie = tk.Button(ramka3, text="    NIE    ", command=komunikat_nie, bg="dimgray")
    nie.pack(side=RIGHT)


def komunikat_nie():

    okno_kom.destroy()
    podglad()


def pewien_usun_wpis():

    global klucz_autoryzacyjny
    global okno_kom
    okno_kom = tk.Toplevel()
    window_height = 120
    window_width = 280
    screen_width = okno_kom.winfo_screenwidth()
    screen_height = okno_kom.winfo_screenheight()
    x_cordinate = int(okno.winfo_x() + (screen_width / 16.5))
    y_cordinate = int(okno.winfo_y() + (screen_height / 9))
    okno_kom.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    okno_kom.title("Usuwanie wpisu")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="\nJESTEŚ PEWIEN?", bg="seagreen", fg="red4", font='Helvetica 12 bold')
    info3.pack()
    autoryzacja = tk.Label(ramka2, text="Klucz autoryzacyjny:", bg='seagreen', fg='red4', font='Helvetica 9 bold')
    autoryzacja.pack(side=LEFT)
    klucz_autoryzacyjny = Entry(ramka2)
    klucz_autoryzacyjny.pack(side=RIGHT)
    klucz_autoryzacyjny.get()
    klucz_autoryzacyjny.focus_set()
    przerwa = tk.Label(ramka2, text='\n', bg='seagreen')
    przerwa.pack()
    ramka3 = tk.Frame(okno_kom)
    ramka3.configure(bg='seagreen')
    ramka3.pack()
    tak = tk.Button(ramka3, text="    TAK    ", command=usun_ostatni_wpis, bg="red3")
    tak.pack(side=LEFT)
    przerwa2 = tk.Label(ramka3, text='               ', bg='seagreen')
    przerwa2.pack(side=LEFT)
    nie = tk.Button(ramka3, text="    NIE    ", command=komunikat_nie, bg="dimgray")
    nie.pack(side=RIGHT)


def zapisz():

    global ilosc_element
    global moc_element
    ilosc_element = ilosc.get()
    ilosc_element = int(ilosc_element)
    moc_element = moc.get()
    moc_element = str(moc_element)
    moc_element = moc_element.replace(',', '.')
    moc_element = float(moc_element)
    zapisz_date()
    ilosc_element = str(ilosc_element)
    moc_element = str(moc_element)
    nowy_trunek(ilosc_element, moc_element)
    zapisz_opis()
    dodaj()


def spr_zap():

    global ilosc_element
    global moc_element
    ilosc_element = ilosc.get()
    ilosc_element = int(ilosc_element)
    moc_element = moc.get()
    moc_element = str(moc_element)
    moc_element = moc_element.replace(',', '.')
    moc_element = float(moc_element)

    data_trunku = data2.get()
    if data_trunku == "":
        if ilosc_element >= 1 and moc_element >= 0.1 and ilosc_element <= 1000 and moc_element <= 100:
            if ilosc_element_baza() >= 5:
                zapisz()
            else:
                get_klucz()
    else:
        data_trunku = str(data_trunku)
        rok = data_trunku[0:4]
        rok = int(rok)
        miesiac = data_trunku[5:7]
        miesiac = int(miesiac)
        dzien = data_trunku[8:10]
        dzien = int(dzien)
        tab_data = [rok, miesiac, dzien]
        data_wpis = datetime.date(tab_data[0], tab_data[1], tab_data[2])
        today = datetime.date.today()
        interwal = today - data_wpis
        dni = int(interwal.total_seconds() / 86400)
        if 0 <= dni < 15:
            spr_wzor = re.search("[2][0][2][0-9]-[0-9][0-9]-[0-9][0-9]$", data_trunku)
            if spr_wzor:
                if ilosc_element >= 1 and moc_element >= 0.1 and ilosc_element <= 1000 and moc_element <= 100:
                    if ilosc_element_baza() >= 5:
                        zapisz()
                    else:
                        get_klucz()
            else:
                None
        else:
            None


# Sekcja uwierzytelniania użytkownika:


def get_klucz():

    global okno_getkod
    global klucz
    okno_getkod = tk.Toplevel()
    window_height = 120
    window_width = 280
    screen_width = okno_getkod.winfo_screenwidth()
    screen_height = okno_getkod.winfo_screenheight()
    x_cordinate = int(okno.winfo_x() + (screen_width / 16.5))
    y_cordinate = int(okno.winfo_y() + (screen_height / 9))
    okno_getkod.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    okno_getkod.title("Nadawanie klucza")
    okno_getkod.configure(background='seagreen')
    okno_getkod.resizable(False, False)
    okno_getkod.wm_iconbitmap('ikona.ico')
    okno_getkod.grab_set()
    ramka2 = tk.Frame(okno_getkod)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="\nNadaj nowy klucz autoryzacyjny:", bg="seagreen", fg="gold",
                     font='Helvetica 12 bold')
    info3.pack()
    klucz = Entry(ramka2)
    klucz.pack()
    klucz.focus_set()
    przerwa = tk.Label(ramka2, text="")
    przerwa.configure(bg="seagreen")
    przerwa.pack()
    zapamietaj = tk.Button(ramka2, text="ZAPAMIĘTAJ", command=zapamietaj_klucz, bg='seagreen2')
    zapamietaj.pack()


def zapamietaj_klucz():

    klucz_dostepu = klucz.get()
    klucz_dostepu = str(klucz_dostepu)
    temp = klucz_dostepu[0-5]
    baza_danych = open(sciezka, 'a')
    baza_danych.write(str(zakoduj(klucz_dostepu)) + "\n")
    baza_danych.close()
    zapisz()
    okno_getkod.destroy()
    podglad()


def uwierzytelnienie():

    wpis_bazy_do_tablicy()
    if str(odkoduj(tablica_danych[0])) == str(kl_aut):
        return 1
    else:
        return 2


def zakoduj(klucz):

    kod=''
    for znak in klucz:
        kod=kod+chr(ord(znak)+5)
    return kod


def odkoduj(klucz):

    kod=''
    for znak in klucz:
        kod=kod+chr(ord(znak)-5)
    return kod


# Sekcja główna wywołania programu:


menu_info()
okno.mainloop()
