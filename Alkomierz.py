import time
import datetime
import tkinter as tk
from tkinter import *
from pathlib import Path
import re
import os

sciezka = str('baza_wypitych_trunkow.txt')

baza_danych = open(sciezka, 'a')
baza_danych.close()

tablica_danych = []
data = datetime.date.today()

okno = tk.Tk()
window_height = 352
window_width = 515
screen_width = okno.winfo_screenwidth()
screen_height = okno.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
okno.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

okno.title("Alkomierz 3.1G Beta")
okno.configure(background='seagreen')
okno.resizable(False, False)
okno.wm_iconbitmap('ikona.ico')


# Sekcja opcji z menubar w programie:


def menu_dodaj():

    global ilosc
    global moc
    global opis
    global data2
    wyczysc_ramke()

    lewa = tk.Frame(okno)
    lewa.pack(side=LEFT)
    lewa.configure(bg='seagreen')
    gora = tk.Label(lewa, text="    WYBIERZ TRUNEK:     ", bg='seagreen', fg="silver", font='Helvetica 12 bold')
    gora.pack()
    wzor0 = tk.Button(lewa, text='Tyskie Gronie', command=lambda: trunekwzor(500, 5.2, "Tyskie Gronie"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor0.pack()
    wzor1 = tk.Button(lewa, text='Żywiec', command=lambda: trunekwzor(500, 5.6, "Żywiec"), bg='silver', fg="brown",
                       font='Helvetica 10 bold', width=22)
    wzor1.pack()
    wzor2 = tk.Button(lewa, text='Perła Chmielowa', command=lambda: trunekwzor(500, 6, "Perła Chmielowa"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor2.pack()
    wzor3 = tk.Button(lewa, text='Amber Koźlak', command=lambda: trunekwzor(500, 6.5, "Amber Koźlak"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor3.pack()
    wzor4 = tk.Button(lewa, text='Namysłów Pils', command=lambda: trunekwzor(500, 6, "Namysłów Pils"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor4.pack()
    wzor5 = tk.Button(lewa, text='Kasztelan Niepasteryzowane', command=lambda: trunekwzor(500, 5,
                      "Kasztelan Niepasteryzowane"), bg='silver', fg="brown", font='Helvetica 10 bold', width=22)
    wzor5.pack()
    wzor6 = tk.Button(lewa, text='Amber APA', command=lambda: trunekwzor(500, 5.2, "Amber APA"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor6.pack()
    wzor7 = tk.Button(lewa, text='Trybunał Pils', command=lambda: trunekwzor(500, 6, "Trybunał Pils"), bg='silver',
                      fg="brown", font='Helvetica 10 bold', width=22)
    wzor7.pack()
    wzor8 = tk.Button(lewa, text='Wino 250ml', command=lambda: trunekwzor(250, 12, "Wino"), bg='silver', fg="brown",
                       font='Helvetica 10 bold', width=22)
    wzor8.pack()
    wzor9 = tk.Button(lewa, text='Whisky 100ml', command=lambda: trunekwzor(100, 40, "Whisky"), bg='silver', fg="brown",
                       font='Helvetica 10 bold', width=22)
    wzor9.pack()
    wzor10 = tk.Button(lewa, text='Wódka 100ml', command=lambda: trunekwzor(100, 40, "Wódka"), bg='silver', fg="brown",
                       font='Helvetica 10 bold', width=22)
    wzor10.pack()

    menu_gorna = tk.Frame(okno)
    menu_gorna.pack(side=LEFT)
    menu_gorna.configure(background='darkseagreen')
    menu = tk.Menu(okno)
    okno.config(menu=menu)
    menu.add_command(label="    DODAJ    ", command=menu_dodaj)
    menu.add_command(label="    WYPITE TRUNKI   ", command=menu_podglad)
    menu.add_command(label="  O PROGRAMIE  ", command=menu_info)
    if ilosc_element_baza() >= 5:
        menu.add_command(label="  ZMIEŃ KLUCZ  ", command=zmiana_hasla_uwierzytelnianie)
    else:
        None
    menu.add_command(label="  WYJŚCIE  ", command=zamykanie)
    kolejnosc = tk.Label(menu_gorna, text="WPISUJESZ " + str(ilosc_dawek()) + ". TRUNEK!",
                         bg="darkseagreen", fg="brown4",
                         font='Helvetica 14 bold')
    kolejnosc.pack()
    ilosc_tekst = tk.Label(menu_gorna, text="ILOŚĆ:", bg='darkseagreen',
                           fg="gold",
                           font='Helvetica 11 bold')
    ilosc_tekst.pack()
    ilosc = Entry(menu_gorna, width=10)
    ilosc.pack()
    ilosc.insert(0, 'ml')
    ilosc.get()
    moc_tekst = tk.Label(menu_gorna, text="\nZAWARTOŚĆ ALKOHOLU:", bg='darkseagreen',
                         fg="gold", font='Helvetica 11 bold')
    moc_tekst.pack()
    moc = Entry(menu_gorna, width=10)
    moc.pack()
    moc.insert(0, '%')
    opis_tekst = tk.Label(menu_gorna, text="\nOPIS TRUNKU:", bg="darkseagreen", fg="gold", font="Helvetica 11 bold")
    opis_tekst.pack()
    opis = Entry(menu_gorna, width=30)
    opis.pack()
    opis.get()
    opis.bind("<Return>", (lambda event: spr_zap()))
    data_tekst = tk.Label(menu_gorna, text="\nDATA SPOŻYCIA:", bg="darkseagreen", fg="gold",
                          font="Helvetica 12 bold")
    data_format_tekst = tk.Label(menu_gorna, text="RRRR-MM-DD", bg="darkseagreen", fg="red",
                          font="Helvetica 8 bold")
    data_tekst.pack()
    data_format_tekst.pack()
    data2 = Entry(menu_gorna, width=10)
    data2.pack()
    data2.insert(0, data)
    data2.get()
    przerwa = tk.Label(menu_gorna, text="", bg="darkseagreen")
    przerwa.pack()
    przycisk_dodaj = tk.Button(menu_gorna, text="          DODAJ TRUNEK!          ", bg="seagreen2", command=spr_zap)
    przycisk_dodaj.pack(side=LEFT)
    przycisk_dodaj.bind("<Return>", (lambda event: spr_zap()))
    przycisk_tosamo = tk.Button(menu_gorna, text="         TO CO OSTATNIO!         ", bg="seagreen2",
                                command=to_co_ostatnio)
    przycisk_tosamo.pack(side=RIGHT)
    przycisk_tosamo.bind("<Return>", (lambda event: to_co_ostatnio()))


def menu_podglad():

    if os.path.isfile("temp.txt"):
        os.unlink("temp.txt")

    if ilosc_element_baza() >= 5:
        try:
            wyczysc_ramke()
            menu_gorna = tk.Frame(okno)
            menu_gorna.pack(side=TOP, fill=X)
            menu_gorna.configure(background='seagreen')
            menu = tk.Menu(okno)
            okno.config(menu=menu)
            menu.add_command(label="    DODAJ    ", command=menu_dodaj)
            menu.add_command(label="    WYPITE TRUNKI   ", command=menu_podglad)
            menu.add_command(label="  O PROGRAMIE  ", command=menu_info)
            if ilosc_element_baza() >= 5:
                menu.add_command(label="  ZMIEŃ KLUCZ  ", command=zmiana_hasla_uwierzytelnianie)
            else:
                None
            menu.add_command(label="  WYJŚCIE  ", command=zamykanie)
            scrollbar = Scrollbar(okno)
            lista_trun = Listbox(menu_gorna, yscrollcommand=scrollbar.set, bg="darkgreen", fg="gold",
                                 font='Helvetica 10 bold')
            scrollbar = Scrollbar(lista_trun)
            lista_trun.pack(side=TOP)
            scrollbar.config(command=lista_trun.yview)
            lista_trun.config(height=12, width=85)

            alkoholomierz()

            pozycja = 0
            pozycja = int(pozycja)
            a, b, c, d = 2, 3, 4, 1
            id_trunku = 0
            try:
                lista_trun.insert(END, "--------------------------------------------------    " +
                                  str(tablica_danych[pozycja + d]) + "    --------------------------------"
                                                                     "---------------------")
                lista_trun.insert(END,  "")
                for lista_trunek, pozycja_trunek in enumerate(tablica_danych):

                    lista_trun.insert(END, str(pozycja + 1) + ".  Wypiłeś " + str(tablica_danych[pozycja + a]) + "ml " +
                                          str(tablica_danych[pozycja + b]) + "% (" + str(ile_alko_wtrunku(id_trunku)) +
                                          "g): " + str(tablica_danych[pozycja + c]))
                    lista_trun.see(tk.END)
                    if pozycja + d + 4 <= ilosc_element_baza() - 1:
                        if str(tablica_danych[pozycja + d]) != str(tablica_danych[pozycja + d + 4]):
                            lista_trun.insert(END, "")
                            lista_trun.insert(END, "--------------------------------------------------    " +
                                              str(tablica_danych[pozycja + d + 4]) + "   ---------------------------"
                                                                                    "---------------------------")
                            lista_trun.insert(END, "")
                    else:
                        break
                    pozycja = pozycja + 1
                    a = a + 3
                    b = b + 3
                    c = c + 3
                    d = d + 3
                    id_trunku += 4
            except IndexError:
                error_uszkodzona()
            przycisk_edytuj_trunek = tk.Button(menu_gorna, text="       EDYTUJ TRUNEK       ", bg="seagreen2",
                                               font='Helvetica 10 ', command=komunikat_edytuj_trunek)
            przycisk_usun_trunek = tk.Button(menu_gorna, text="         USUŃ TRUNEK         ", bg="seagreen2",
                                             font='Helvetica 10 ', command=komunikat_usun_trunek)
            przycisk_usun_baze = tk.Button(menu_gorna, text="  USUŃ BAZĘ DANYCH    ", bg="seagreen2", fg="red",
                                               font='Helvetica 10 bold', command=pewien_usun_baze)
            przycisk_edytuj_trunek.pack(side=LEFT)
            przycisk_usun_trunek.pack(side=LEFT)
            przycisk_usun_baze.pack(side=LEFT)

            menu_dolna = tk.Frame(okno)
            menu_dolna.pack(side=TOP, fill=X)
            menu_dolna.configure(background='seagreen')
            wyliczenia1 = Label(menu_dolna, text="OD " + dat + " (" + str(podglad_ile_dni()) + ") WYPIŁEŚ " +
                                                     str(ilosc_plynu()) + "L TRUNKÓW,\n W KTÓRYCH ZNAJDOWAŁO SIĘ "
                                                     + str(alkoholomierz()) + "g CZYSTEGO ALKOHOLU.",
                                    bg="seagreen", fg="gold",
                                    font='Helvetica 9 bold')
            wyliczenia2 = Label(menu_dolna, text=ostatni_tydzien(),
                                    bg="seagreen", fg="red4",
                                    font='Helvetica 11 bold')
            wyliczenia3 = Label(menu_dolna, text="ŚREDNIO W DNIU, W KTÓRYM PIJESZ, SPOŻYWASZ " +
                                                     str(srednia_posiadowy())
                                                     + "g CZYSTEGO ALKOHOLU.", bg="seagreen", fg="gold",
                                    font='Helvetica 9 bold')
            wyliczenia1.pack()
            wyliczenia3.pack()
            wyliczenia2.pack()
        except ValueError:
           error_uszkodzona()
    else:
        menu_podglad_pusta()


def menu_podglad_pusta():

    wyczysc_ramke()
    menu_gorna = tk.Frame(okno)
    menu_gorna.pack()
    menu_gorna.configure(background='gray')
    menu = tk.Menu(okno)
    okno.config(menu=menu)
    menu.add_command(label="    DODAJ    ", command=menu_dodaj)
    menu.add_command(label="    WYPITE TRUNKI   ", command=menu_podglad)
    menu.add_command(label="  O PROGRAMIE  ", command=menu_info)
    if ilosc_element_baza() >= 5:
        menu.add_command(label="  ZMIEŃ KLUCZ  ", command=zmiana_hasla_uwierzytelnianie)
    else:
        None
    menu.add_command(label="  WYJŚCIE  ", command=zamykanie)
    opis = tk.Label(okno, text="\nWitaj w programie\n\n\n\n\n", fg="lightskyblue", bg="seagreen",
                    font='Helvetica 12 bold')
    informacja = tk.Label(okno, text="BAZA JEST PUSTA!", fg="red2", bg="seagreen",
                          font='Helvetica 21 bold')
    informacja2 = tk.Label(okno, text="Dodaj pierwszy trunek", fg="red2", bg="seagreen",
                           font='Helvetica 10 bold')
    opis2 = tk.Label(okno, text="A L K O M I E R Z\n", fg="brown", bg="seagreen", font='gothic 26 bold')
    opis3 = tk.Label(okno,
                     text="\n\nTomek Kasperek                                                      "
                          "             Wersja: 3.1G Beta",
                     fg="lightskyblue", bg="seagreen", font='Helvetica 10 bold')
    opis.pack()
    opis2.pack()
    informacja.pack()
    informacja2.pack()
    opis3.pack()


def menu_info():

    if os.path.isfile("temp.txt"):
        os.unlink("temp.txt")

    wyczysc_ramke()
    menu_gorna = tk.Frame(okno)
    menu_gorna.pack()
    menu_gorna.configure(background='gray')
    menu = tk.Menu(okno)
    okno.config(menu=menu)
    menu.add_command(label="    DODAJ    ", command=menu_dodaj)
    menu.add_command(label="    WYPITE TRUNKI   ", command=menu_podglad)
    menu.add_command(label="  O PROGRAMIE  ", command=menu_info)
    if ilosc_element_baza() >= 5:
        menu.add_command(label="  ZMIEŃ KLUCZ  ", command=zmiana_hasla_uwierzytelnianie)
    else:
        None
    menu.add_command(label="  WYJŚCIE  ", command=zamykanie)
    opis = tk.Label(okno, text="\nWitaj w programie\n\n\n\n\n", fg="lightskyblue", bg="seagreen",
                    font='Helvetica 12 bold')
    informacja = tk.Label(okno, text="BAZA JEST PUSTA!", fg="red2", bg="seagreen",
                          font='Helvetica 21 bold')
    informacja2 = tk.Label(okno, text="Dodaj pierwszy trunek", fg="red2", bg="seagreen",
                           font='Helvetica 10 bold')
    opis2 = tk.Label(okno, text="A L K O M I E R Z\n", fg="brown", bg="seagreen", font='gothic 26 bold')
    opis3 = tk.Label(okno,
                     text="\n\n\n\n\n\nTomek Kasperek                                                      "
                          "             Wersja: 3.1G Beta",
                     fg="lightskyblue", bg="seagreen", font='Helvetica 10 bold')
    opis.pack()
    opis2.pack()
    opis3.pack()


def zamykanie():

    time.sleep(0.1)
    if os.path.isfile("temp.txt"):
        os.unlink("temp.txt")
    baza_danych.close()
    sys.exit()


# Sekcja operacji GUI:


def wyczysc_ramke():

    for obiekty in okno.winfo_children():
        obiekty.destroy()


def komunikat_nie():

    okno_kom.destroy()
    menu_podglad()


def error(komunikat):

    global okno_error
    okno_error = tk.Toplevel()
    window_height = 120
    window_width = 280
    screen_width = okno_error.winfo_screenwidth()
    screen_height = okno_error.winfo_screenheight()
    x_cordinate = int(okno.winfo_x() + (screen_width / 16.5))
    y_cordinate = int(okno.winfo_y() + (screen_height / 9))
    okno_error.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    okno_error.title("Komunikat")
    okno_error.configure(background='seagreen')
    okno_error.resizable(False, False)
    okno_error.wm_iconbitmap('ikona.ico')
    okno_error.grab_set()
    ramka2 = tk.Frame(okno_error)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="" + komunikat, bg="seagreen", fg="gold", font='Helvetica 12 bold')
    info3.pack()
    info4 = tk.Label(ramka2, text="", bg="seagreen", fg="red2", font='Helvetica 12 bold')
    info4.pack()
    ok = tk.Button(ramka2, text="   ROZUMIEM   ", command=error_del, bg='seagreen2')
    ok.pack()
    okno_error.focus_set()


def error_del():

    okno_error.destroy()


def error_uszkodzona():

    global klucz_autoryzacyjny
    global okno_kom
    okno_kom = tk.Toplevel()
    window_height = 140
    window_width = 280
    screen_width = okno_kom.winfo_screenwidth()
    screen_height = okno_kom.winfo_screenheight()
    x_cordinate = int(okno.winfo_x() + (screen_width / 16.5))
    y_cordinate = int(okno.winfo_y() + (screen_height / 9))
    okno_kom.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    okno_kom.title("Baza uszkodzona")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="BAZA JEST USZKODZONA,\nBRAK MOŻLIWOŚCI NAPRAWY.\n Usunąć bazę?", bg="seagreen",
                     fg="red4", font='Helvetica 12 bold')
    info3.pack()
    autoryzacja = tk.Label(ramka2, text="Klucz autoryzacyjny:", bg='seagreen', fg='red4', font='Helvetica 9 bold')
    autoryzacja.pack(side=LEFT)
    klucz_autoryzacyjny = Entry(ramka2, show="*")
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
    nie = tk.Button(ramka3, text="    NIE    ", command=menu_info, bg="dimgray")
    nie.pack(side=RIGHT)


# Sekcja  obsługi bazy danych:


def wpis_bazy_do_tablicy():

    tablica_danych.clear()
    with open(sciezka, 'r') as zawartosc:
        for linia in zawartosc:
            linia = linia.replace("\n", "")
            linia = str(linia)
            tablica_danych.append(linia)
    baza_danych.close()


def wpis_tablicy_do_bazy():

    poz = 0
    poz = int(poz)
    while len(tablica_danych) > poz:
        baza_danych = open(sciezka, 'a')
        baza_danych.write(str(tablica_danych[poz]) + "\n")
        baza_danych.close()
        poz = poz + 1
        baza_danych.close()


# Usuwanie bazy danych:


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
    klucz_autoryzacyjny = Entry(ramka2, show="*")
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


def usun_baze():

    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    if uwierzytelnienie() == 1:
        okno_kom.destroy()
        baza_danych = open(sciezka, 'w')
        baza_danych = open(sciezka, 'a')
        baza_danych.close()
        menu_podglad_pusta()
    else:
        error("\nBłędny klucz!")


# Usuwanie trunku:


def komunikat_usun_trunek():

    global id_usun
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
    okno_kom.title("Usuwanie trunku")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="Wybierz ID trunku:", bg="seagreen", fg="red4", font='Helvetica 12 bold')
    info3.pack()
    id_usun = Entry(ramka2, width=3)
    id_usun.pack()
    id_usun.get()
    id_usun.focus_set()
    autoryzacja = tk.Label(ramka2, text="Klucz autoryzacyjny:", bg='seagreen', fg='red4', font='Helvetica 9 bold')
    autoryzacja.pack(side=LEFT)
    klucz_autoryzacyjny = Entry(ramka2, show="*")
    klucz_autoryzacyjny.pack(side=RIGHT)
    klucz_autoryzacyjny.get()
    przerwa = tk.Label(ramka2, text='\n', bg='seagreen')
    przerwa.pack()
    ramka3 = tk.Frame(okno_kom)
    ramka3.configure(bg='seagreen')
    ramka3.pack()
    tak = tk.Button(ramka3, text="    USUŃ    ", command=usuwanie_trunku, bg="red3")
    tak.pack(side=LEFT)
    przerwa2 = tk.Label(ramka3, text='               ', bg='seagreen')
    przerwa2.pack(side=LEFT)
    nie = tk.Button(ramka3, text="    POWRÓT   ", command=komunikat_nie, bg="dimgray")
    nie.pack(side=RIGHT)


def usuwanie_trunku():

    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    try:
        id = id_usun.get()
        id = int(id)
        if uwierzytelnienie() == 1:
            if int((ilosc_element_baza() - 1) / 4) >= id >= 1:
                okno_kom.destroy()
                usuwanie(id)
            else:
                error("\nBrak trunku z ID " + str(id) + "!")
        else:
            error("\nBłędny klucz!")
    except ValueError:
        error("\nWpisz poprawne ID!")


def usuwanie(id):

    wpis_bazy_do_tablicy()
    baza_danych = open(sciezka, 'w')
    tablica_danych.pop(id+3*(id-1))
    tablica_danych.pop(id+3*(id-1))
    tablica_danych.pop(id+3*(id-1))
    tablica_danych.pop(id+3*(id-1))
    if len(tablica_danych) < 5:
        tablica_danych.pop(0)
    wpis_tablicy_do_bazy()
    menu_podglad()


# Edytowanie trunku:


def komunikat_edytuj_trunek():

    global id_usun
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
    okno_kom.title("Edytowanie trunku")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="Wybierz ID trunku:", bg="seagreen", fg="red4", font='Helvetica 12 bold')
    info3.pack()
    id_usun = Entry(ramka2, width=3)
    id_usun.pack()
    id_usun.get()
    id_usun.focus_set()
    autoryzacja = tk.Label(ramka2, text="Klucz autoryzacyjny:", bg='seagreen', fg='red4', font='Helvetica 9 bold')
    autoryzacja.pack(side=LEFT)
    klucz_autoryzacyjny = Entry(ramka2, show="*")
    klucz_autoryzacyjny.pack(side=RIGHT)
    klucz_autoryzacyjny.get()
    przerwa = tk.Label(ramka2, text='\n', bg='seagreen')
    przerwa.pack()
    ramka3 = tk.Frame(okno_kom)
    ramka3.configure(bg='seagreen')
    ramka3.pack()
    tak = tk.Button(ramka3, text="    EDYTUJ    ", command=edytuj_trunku, bg="red3")
    tak.pack(side=LEFT)
    przerwa2 = tk.Label(ramka3, text='               ', bg='seagreen')
    przerwa2.pack(side=LEFT)
    nie = tk.Button(ramka3, text="    POWRÓT   ", command=komunikat_nie, bg="dimgray")
    nie.pack(side=RIGHT)


def edytuj_trunku():
    global id
    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    try:
        id = id_usun.get()
        id = int(id)
        if uwierzytelnienie() == 1:
            if int((ilosc_element_baza() - 1) / 4) >= id >= 1:
                okno_kom.destroy()
                edytuj(id)
            else:
                error("\nBrak trunku z ID " + str(id) + "!")
        else:
            error("\nBłędny klucz!")
    except ValueError:
        error("\nWpisz poprawne ID!")


def edytuj(id):

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
    menu.add_command(label="    DODAJ    ", command=menu_dodaj)
    menu.add_command(label="    WYPITE TRUNKI   ", command=menu_podglad)
    menu.add_command(label="  O PROGRAMIE  ", command=menu_info)
    if ilosc_element_baza() >= 5:
        menu.add_command(label="  ZMIEŃ KLUCZ  ", command=zmiana_hasla_uwierzytelnianie)
    else:
        None
    menu.add_command(label="  WYJŚCIE  ", command=zamykanie)
    kolejnosc = tk.Label(menu_gorna, text="EDYTUJESZ " + str(id) + ". TRUNEK!",
                         bg="darkseagreen", fg="brown4",
                         font='Helvetica 14 bold')
    kolejnosc.pack()
    ilosc_tekst = tk.Label(menu_gorna, text="ILOŚĆ(ml):", bg='darkseagreen',
                           fg="gold",
                           font='Helvetica 11 bold')
    ilosc_tekst.pack()
    ilosc = Entry(menu_gorna, width=10)
    ilosc.pack()
    ilosc.insert(0, str(tablica_danych[id + 3 * (id - 1) + 1]))
    ilosc.focus_set()
    ilosc.get()
    moc_tekst = tk.Label(menu_gorna, text="\nZAWARTOŚĆ ALKOHOLU(%):", bg='darkseagreen',
                         fg="gold", font='Helvetica 11 bold')
    moc_tekst.pack()
    moc = Entry(menu_gorna, width=10)
    moc.pack()
    moc.insert(0, str(tablica_danych[id + 3 * (id - 1) + 2]))
    opis_tekst = tk.Label(menu_gorna, text="\nOPIS TRUNKU:", bg="darkseagreen", fg="gold", font="Helvetica 11 bold")
    opis_tekst.pack()
    opis = Entry(menu_gorna, width=30)
    opis.pack()
    opis.insert(0, str(tablica_danych[id + 3 * (id - 1)+3]))
    opis.get()
    opis.bind("<Return>", (lambda event: spr_zap()))
    data2 = Entry(menu_gorna, width=10)
    data2.insert(0, tablica_danych[id+3*(id-1)])
    data2.get()
    przerwa = tk.Label(menu_gorna, text="\n\n\n\n\n\n", bg="darkseagreen")
    przerwa.pack()
    przycisk_dodaj = tk.Button(menu_gorna, text="      WPROWADŹ ZMIANY      ",
                               bg="seagreen2", command=zapisz_mod_wpis)
    przycisk_dodaj.pack(side=LEFT)
    przycisk_dodaj.bind("<Return>", (lambda event: zapisz_mod_wpis()))
    przycisk_anuluj = tk.Button(menu_gorna, text="                 ANULUJ                 ",
                               bg="seagreen2", command=menu_podglad)
    przycisk_anuluj.pack(side=RIGHT)
    przycisk_anuluj.bind("<Return>", (lambda event: menu_podglad()))


def zapisz_mod_wpis():

    global ilosc_element
    global moc_element
    try:
        ilosc_element = ilosc.get()
        ilosc_element = int(ilosc_element)
        moc_element = moc.get()
        moc_element = str(moc_element)
        moc_element = moc_element.replace(',', '.')
        moc_element = float(moc_element)
    except ValueError:
        None
    try:
        global opis
        opis_trunku = opis.get()
        opis_trunku = str(opis_trunku)
        temp = open("temp.txt", 'a')
        temp.write(opis_trunku + "\n")
        temp.close()
        opis_trunku = opis.get()
        opis_trunku = str(opis_trunku)
        try:
            if len(opis_trunku) <= 30:
                if 1 <= int(ilosc_element) <= 2000 and float(moc_element) >= 0.1 and float(moc_element) <= 100:
                    zapisz_mod()
                else:
                    error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
            else:
                error("Zbyt długi opis trunku\n(maksymalnie 30 znaków)")
        except ValueError:
            error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
    except UnicodeEncodeError:
        error("\nOpis zawiera nieobsługiwane znaki!")


def zapisz_mod():

    global ilosc_element
    global moc_element
    global opis

    ilosc_element = ilosc.get()
    ilosc_element = str(ilosc_element)

    moc_element = moc.get()
    moc_element = str(moc_element)
    moc_element = moc_element.replace(',', '.')
    moc_element = float(moc_element)
    moc_element = str(moc_element)

    opis_trunku = opis.get()
    opis_trunku = str(opis_trunku)
    opis_trunku = opis_trunku.replace("\\", "/")

    wpis_bazy_do_tablicy()
    tablica_danych[id + 3 * (id - 1) + 1] = str(ilosc_element)
    tablica_danych[id + 3 * (id - 1) + 2] = str(moc_element)
    tablica_danych[id + 3 * (id - 1) + 3] = str(opis_trunku)
    baza_danych = open(sciezka, 'w')
    wpis_tablicy_do_bazy()

    menu_podglad()


# Ilosc elementów w bazie i poprawnosc bazy:


def ilosc_element_baza():

    wpis_bazy_do_tablicy()
    sztuki = len(tablica_danych)
    return int(sztuki)


def spr_poprawnosc_bazy():

    if ilosc_element_baza() < 5:
        baza_danych = open(sciezka, 'w')
        baza_danych = open(sciezka, 'a')
        baza_danych.close()
    else:
        while not (ilosc_element_baza()-1) % 4 == 0:
            us = len(tablica_danych) - 1
            us = int(us)
            tablica_danych.pop(us)
            baza_danych = open(sciezka, 'w')
            wpis_tablicy_do_bazy()

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
    except ValueError or IndexError:
        error("Baza danych uszkodzona!!!\n Czy chcesz ją usunąć?")


# Sekcja operacji na informacjach z bazy:


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
            czysta = (float(int(tablica_danych[pozycja + a]) * (float(tablica_danych[pozycja + b]) / 100))) * 0.8
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


def ilosc_dawek():

    wpis_bazy_do_tablicy()
    enty = (len(tablica_danych)) / 4
    enty = int(enty) + 1
    if enty == 0:
        enty = 1
    return enty


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


def porownanie():

    dzielnik = dni_wpisywania()
    if dni_wpisywania() == 0:
        dzielnik = 1
    if alkoholomierz() / dzielnik < 28:
        return "WYPIJASZ UMIARKOWANE ILOŚCI ALKOHOLU ("+str(porownanie_wartosc())+"g/dzień)"
    if alkoholomierz() / dzielnik >= 28:
        return "PIJESZ RYZYKOWNIE! ("+str(porownanie_wartosc())+"g/dzień)"


def porownanie_wartosc():

    if dni_wpisywania() == 0:
        return int(alkoholomierz() / 1)
    else:
        return int(alkoholomierz() / dni_wpisywania())


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
        error("ilosc_plynu")
    return ilosc_suma


def podglad_ile_dni():

    if dni_wpisywania() == 0:
        return "DZIŚ"
    else:
        return str(dni_wpisywania()) + " DNI TEMU"


def ile_alko_wtrunku(id_trunku):

    wpis_bazy_do_tablicy()
    return int(((int(tablica_danych[id_trunku+2])*0.8) * float(tablica_danych[id_trunku+3])) / 100)


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


def dzienny_alkohol(dzien_pic):

    tab_alk = []
    id_dnia = 1
    while id_dnia <= ilosc_element_baza() - 2:
        if tablica_danych[dzien_pic] == tablica_danych[id_dnia]:
            tab_alk.append((int(((int(tablica_danych[id_dnia+1])*0.8) * float(tablica_danych[id_dnia+2])) / 100)))
        id_dnia += 4

    return sum(tab_alk)


def ostatni_tydzien():

    if ilosc_element_baza() < 5:
        return None
    else:
        ostatni_tydz = []
        kol = 4
        data_trunku = tablica_danych[ilosc_element_baza() - kol]
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

        while dni <= 6:
            if ilosc_element_baza() > kol + 4:
                try:
                    trunek = int(((int(tablica_danych[ilosc_element_baza() - kol + 1]) * 0.8) * float(
                        tablica_danych[ilosc_element_baza() - kol + 2])) / 100)
                    ostatni_tydz.append(trunek)
                    kol += 4

                    data_trunku = tablica_danych[ilosc_element_baza() - kol]
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
                except IndexError:
                    None
            else:
                trunek = int(((int(tablica_danych[ilosc_element_baza() - kol + 1]) * 0.8) * float(
                    tablica_danych[ilosc_element_baza() - kol + 2])) / 100)
                ostatni_tydz.append(trunek)
                break

    suma = int(sum(ostatni_tydz))
    return "W CIĄGU OSTATNICH 7 DNI SPOŻYŁEŚ " + str(suma) + "g CZYSTEGO ALKOHOLU!"


# Sekcja zapisu nowego trunku:


def trunekwzor(il,mo,op):

    global ilosc
    global moc
    global opis
    ilosc.delete(0, END)
    ilosc.insert(0, int(il))
    moc.delete(0, END)
    moc.insert(0, float(mo))
    opis.delete(0, END)
    opis.insert(0, op)


def spr_zap():

    global ilosc_element
    global moc_element
    try:
        ilosc_element = ilosc.get()
        ilosc_element = ilosc_element.replace("ml", "")
        ilosc_element = int(ilosc_element)
        moc_element = moc.get()
        moc_element = str(moc_element)
        moc_element = moc_element.replace(',', '.')
        moc_element = moc_element.replace('%', '')
        moc_element = float(moc_element)
    except ValueError:
        None

    try:
        global opis
        opis_trunku = opis.get()
        opis_trunku = str(opis_trunku)
        temp = open("temp.txt", 'a')
        temp.write(opis_trunku + "\n")
        temp.close()
        try:
            data_trunku = data2.get()
            if data_trunku == "":
                opis_trunku = opis.get()
                opis_trunku = str(opis_trunku)
                if len(opis_trunku) <= 30:
                    if 1 <= ilosc_element <= 2000 and moc_element >= 0.1 and moc_element <= 100:
                        if ilosc_element_baza() >= 5:
                            zapisz()
                        else:
                            get_klucz(zapamietaj_klucz)
                    else:
                        error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
                else:
                    error("Zbyt długi opis trunku\n(maksymalnie 30 znaków)")
            else:
                opis_trunku = opis.get()
                opis_trunku = str(opis_trunku)
                try:
                    if len(opis_trunku) <= 30:
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
                        spr_wzor = re.search("[2][0][2][0-9]-[0-9][0-9]-[0-9][0-9]$", data_trunku)
                        if 0 <= dni:
                            if spr_wzor:
                                if ilosc_element_baza() >= 5:
                                    if dni <= kolejnosc_wpisu():
                                        if 1 <= ilosc_element <= 2000 and 0.1 <= moc_element <= 100:
                                            if ilosc_element_baza() >= 5:
                                                zapisz()
                                            else:
                                                get_klucz(zapamietaj_klucz)
                                        else:
                                            error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
                                    else:
                                        error("Baza musi być\n uzupełniana chronologicznie!")
                                else:
                                    if 1 <= ilosc_element <= 2000 and moc_element >= 0.1 and moc_element <= 100:
                                        if ilosc_element_baza() >= 5:
                                            zapisz()
                                        else:
                                            get_klucz(zapamietaj_klucz)
                                    else:
                                        error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
                            else:
                                error("\nBłędna data wypicia trunku!")
                        else:
                            error("Nie możesz wpisać trunku\n którego nie wypiłeś!")
                    else:
                        error("Zbyt długi opis trunku\n(maksymalnie 30 znaków)")
                except ValueError:
                    error("\nBłędna data wypicia trunku!")
        except TypeError:
            error("Ilość wyraź w wartości\n całkowitej 1-2000,\nmoc 0,1-100!")
    except UnicodeEncodeError:
        error("\nOpis zawiera nieobsługiwane znaki!")


def kolejnosc_wpisu():

    data_trunku = tablica_danych[ilosc_element_baza()-4]
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
    return dni


def zapisz():

    global ilosc_element
    global moc_element
    ilosc_element = ilosc.get()
    ilosc_element = ilosc_element.replace("ml","")
    ilosc_element = int(ilosc_element)
    moc_element = moc.get()
    moc_element = str(moc_element)
    moc_element = moc_element.replace(',', '.')
    moc_element = moc_element.replace('%', '')
    moc_element = float(moc_element)
    zapisz_date()
    ilosc_element = str(ilosc_element)
    moc_element = str(moc_element)
    nowy_trunek(ilosc_element, moc_element)
    zapisz_opis()
    menu_podglad()


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


def zapisz_date_dzisiejsza():

    wpis_bazy_do_tablicy()
    baza_danych = open(sciezka, 'a')
    baza_danych.write(str(data) + "\n")
    baza_danych.close()


def nowy_trunek(ilosc, moc):

    baza_danych = open(sciezka, 'a')
    baza_danych.write(ilosc_element + "\n")
    baza_danych.write(moc_element + "\n")
    baza_danych.close()


def zapisz_opis():

    global opis
    opis_trunku = opis.get()
    opis_trunku = str(opis_trunku)
    opis_trunku = opis_trunku.replace("\\", "/")
    baza_danych = open(sciezka, 'a')
    baza_danych.write(opis_trunku + "\n")
    baza_danych.close()


def to_co_ostatnio():

    if ilosc_element_baza() >= 5:
        zapisz_date_dzisiejsza()
        wpis_bazy_do_tablicy()
        global ilosc_element
        global moc_element
        ilosc_element = tablica_danych[ilosc_element_baza()-4]
        ilosc_element = int(ilosc_element)
        moc_element = tablica_danych[ilosc_element_baza()-3]
        moc_element = float(moc_element)
        if ilosc_element >= 1 and moc_element >= 0.1 and ilosc_element <= 2000 and moc_element <= 100:
            ilosc_element = str(ilosc_element)
            moc_element = str(moc_element)
            nowy_trunek(ilosc_element, moc_element)
            opis_trunku = str(tablica_danych[ilosc_element_baza()-4])
            opis_trunku = str(opis_trunku)
            baza_danych = open(sciezka, 'a')
            baza_danych.write(opis_trunku + "\n")
            baza_danych.close()
            menu_podglad()
        else:
            menu_podglad()
    else:
        error("\nBrak wpisów w bazie danych!")


# Sekcja uwierzytelniania użytkownika:


def get_klucz(czynnosc):

    if ilosc_element_baza() < 5 and czynnosc == zmiana_hasla:
        None
    else:
        global okno_getkod
        global klucz
        global klucz_repeat
        okno_getkod = tk.Toplevel()
        window_height = 170
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
        info3 = tk.Label(ramka2, text="Nadaj nowy klucz autoryzacyjny:", bg="seagreen", fg="gold",
                         font='Helvetica 12 bold')
        info4 = tk.Label(ramka2, text="Minimum 5 znaków", bg="seagreen", fg='red2', font='Helvetica 9 bold')
        info3.pack()
        info4.pack()
        klucz = Entry(ramka2, show="*")
        klucz.pack()
        klucz.focus_set()
        info5 = tk.Label(ramka2, text="Powtórz klucz:", bg="seagreen", fg='red2', font='Helvetica 9 bold')
        info5.pack()
        klucz_repeat = Entry(ramka2, show="*")
        klucz_repeat.pack()
        przerwa = tk.Label(ramka2, text="")
        przerwa.configure(bg="seagreen")
        przerwa.pack()
        zapamietaj = tk.Button(ramka2, text="ZAPAMIĘTAJ", command=czynnosc, bg='seagreen2')
        zapamietaj.pack()


def zapamietaj_klucz():

    klucz_dostepu = klucz.get()
    klucz_dostepu = str(klucz_dostepu)
    klucz_dostepu2 = klucz_repeat.get()
    klucz_dostepu2 = str(klucz_dostepu2)
    try:
        temp = open("temp.txt", 'a')
        temp.write(klucz_dostepu + "\n")
        temp.close()

        if len(klucz_dostepu) >= 5:
            if klucz_dostepu == klucz_dostepu2:
                wpis_bazy_do_tablicy()
                if ilosc_element_baza() > 0:
                    tablica_danych[0] = klucz_dostepu
                    wpis_tablicy_do_bazy()
                else:
                    baza_danych = open(sciezka, 'a')
                    baza_danych.write(str(zakoduj(klucz_dostepu)) + "\n")
                    baza_danych.close()
                zapisz()
                okno_getkod.destroy()
                menu_podglad()
            else:
                error("Wpisane klucze są różne!")
        else:
            error("Wpisany klucz jest zbyt krótki!")
    except UnicodeEncodeError:
        error("\nKlucz zawiera nieobsługiwane znaki!")


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


def uwierzytelnienie():

    wpis_bazy_do_tablicy()
    if str(odkoduj(tablica_danych[0])) == str(kl_aut):
        return 1
    else:
        return 2


def zmiana_hasla_uwierzytelnianie():

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
    okno_kom.title("Zmiana klucza")
    okno_kom.configure(background='seagreen')
    okno_kom.resizable(False, False)
    okno_kom.wm_iconbitmap('ikona.ico')
    okno_kom.grab_set()
    ramka2 = tk.Frame(okno_kom)
    ramka2.configure(bg='seagreen')
    ramka2.pack()
    info3 = tk.Label(ramka2, text="\nPodaj klucz autoryzacyjny:", bg="seagreen", fg="red4", font='Helvetica 12 bold')
    info3.pack()
    klucz_autoryzacyjny = Entry(ramka2, show="*")
    klucz_autoryzacyjny.pack()
    klucz_autoryzacyjny.get()
    klucz_autoryzacyjny.focus_set()
    przerwa = tk.Label(ramka2, text='', bg='seagreen')
    przerwa.pack()
    ramka3 = tk.Frame(okno_kom)
    ramka3.configure(bg='seagreen')
    ramka3.pack()
    ok = tk.Button(ramka3, text="    DALEJ     ", command=zmiana_dalej, bg="red3")
    ok.pack(side=LEFT)


def zmiana_hasla():

        klucz_dostepu = klucz.get()
        klucz_dostepu = str(klucz_dostepu)
        klucz_dostepu2 = klucz_repeat.get()
        klucz_dostepu2 = str(klucz_dostepu2)

        try:
            temp = open("temp.txt", 'a')
            temp.write(klucz_dostepu + "\n")
            temp.close()
            if len(klucz_dostepu) >= 5:
                if klucz_dostepu == klucz_dostepu2:
                    wpis_bazy_do_tablicy()
                    if ilosc_element_baza() > 0:
                        tablica_danych[0] = str(zakoduj(klucz_dostepu))
                        baza_danych = open(sciezka, 'w')
                        wpis_tablicy_do_bazy()
                    else:
                        baza_danych = open(sciezka, 'a')
                        baza_danych.write(str(zakoduj(klucz_dostepu)) + "\n")
                        baza_danych.close()
                    okno_getkod.destroy()
                else:
                    error("Wpisane klucze są różne!")
            else:
                error("Wpisany klucz jest zbyt krótki!")
        except UnicodeEncodeError:
            error("\nKlucz zawiera nieobsługiwane znaki!")


def zmiana_dalej():

    global kl_aut
    kl_aut = klucz_autoryzacyjny.get()
    kl_aut = str(kl_aut)
    if uwierzytelnienie() == 1:
        okno_kom.destroy()
        get_klucz(zmiana_hasla)
    else:
        error("\nBłędny klucz!")


# Sekcja główna wywołania programu:


menu_podglad()
okno.mainloop()
