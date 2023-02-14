import colorama
from colorama import Cursor, Fore
import os

# SE NON INIZIALIZZIAMO IL COMANDO INIT() CON 'AUTOSIZE=TRUE'
# DOBBIAMO RESETTARE I COLORI CON Fore.RESET , IN QUESTO MODO
# print(Fore.RED + Cursor.POS(3, 14) + "@" + Fore.RESET)
# ritorna alla combinazione di colore base
colorama.init(autoreset=True)

# DISEGNA UNA GRIGLIA CON LE DIMENSIONI PASSATE
def griglia(ncol, nrig):
    coln = ncol - 1

    # ELENCO SIMBOLI GRAFICI
    base = 9400
    base1 = 9500
    ang_sup_sx = chr(base + 84)  # ┌
    ang_inf_sx = chr(base + 92)  # └
    ang_sup_dx = chr(base + 88)  # ┐
    ang_inf_dx = chr(base + 96)  # ┘
    linea_oriz = chr(base + 72)  # ─
    linea_vert = chr(base + 74)  # │
    sep_sup = chr(base1 + 16)    # ┬
    sep_inf = chr(base1 + 24)    # ┴
    sep_sx = chr(base1 + 0)      # ├
    sep_dx = chr(base1 + 8)      # ┤
    sep_cross = chr(base1 + 32)  # ┼
    spazio = chr(32)

    # LINEA E SPAZI DI 3 CARATTERI
    linea3 = linea_oriz * 3
    spazio3 = spazio * 3

    step_sup = sep_sup + linea3      # ┬───
    step_med = linea_vert + spazio3  # │
    step_inf = sep_inf + linea3      # ┴───
    step_cross = sep_cross + linea3

    # GESTIONE COLONNE
    riga_div = sep_sx + linea3 + step_cross * coln + sep_dx
    riga_sup = ang_sup_sx + linea3 + step_sup * coln + ang_sup_dx
    riga_med = linea_vert + spazio3 + step_med * coln + linea_vert
    riga_inf = ang_inf_sx + linea3 + step_inf * coln + ang_inf_dx

    # GESTIONE RIGHE
    print(riga_sup)
    print(riga_med)
    for i in range(nrig - 1):
        print(riga_div)
        print(riga_med)
    print(riga_inf)

 
# GESTISCE L'INSERIMENTO DI UN CARATTERE NELLA GRIGLIA
# 'COLONNA' E 'RIGA' SONO LE COORDINATE RELATIVE ALLA GRIGLIA
def print_xy(colonna, riga, char, color):
    colbase = 3
    rigbase = 2
    stepcol = 4
    steprig = 2
    print(color + Cursor.POS(colbase + stepcol * colonna, rigbase + steprig * riga) + char)

# CANCELLA IL TERMINALE
# FUNZIONA SOLO SU WINDOWS
# SU LINUX UTILIZZARE 'clear'.
os.system('cls')

# CREA UNA GRIGLIA 
col = 8
rig = 5
griglia(col, rig)


# ========================== 
#      ESEMPI D'USO 
# ==========================

# DISEGNA UN ROMBO
print_xy(2, 0, '+', Fore.GREEN)
print_xy(3, 1, '+', Fore.GREEN)
print_xy(1, 1, '+', Fore.GREEN)
print_xy(1, 2, '+', Fore.GREEN)
print_xy(3, 2, '+', Fore.GREEN)
print_xy(2, 3, '+', Fore.GREEN)

# TRACCIA LA COLONNA 6
column = 6
for riga in range(rig):
    print_xy(column, riga, '+', Fore.RED)

# TRACCIA LA RIGA 4
row = 4
for colonna in range(col):
    print_xy(colonna,row,'-',Fore.YELLOW)

# SPOSTA IL CURSORE NELL'ULTIMA RIGA DELLO SCHERMO
print(Cursor.POS(3, 25))
