# ZADANIE 1
 # Wyświetl na ekranie następujący wzór:

print ("ZADANIE 1 \n")
print("      *        *")
print("      **      **")
print("      ***    ***")
print("      ****  ****")
print("      **********")
print("      ****  ****")
print("      ***    ***")
print("      **      **")
print("      *        *\n\n")


# ZADANIE 2
 # Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie
 # danych z sieci o rozmiarze 13 TB, jeżeli wiesz, że plik o rozmiarze 194 MB
 # udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.

print ("ZADANIE 2")
_terabajt = 1024*1024
a = _terabajt * 13
b = 194
print("Na pobranie danych z sieci o rozmiarze 13TB, potrzeba:", round(((((a / b) * 5) / 3600)), 0), "godzin.")
print("\n")


# ZADANIE 3
 # Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
 # następujących założeniach:
 # • własne środki 30 tys. zł,
 # • roczna lokata kapitału,
 # • kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
 # • oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
 # • pokazać salda po każdym kwartale,
 # • wyliczyć roczny zysk.

print ("ZADANIE 3")
#--------- A. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 7,5%

print("A. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 7,5%")
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.075 #oprocentowanie w skali roku
oprocentowanie_kwartalne = oprocentowanie / 4
mnoznik_kwartalny = 1 + oprocentowanie_kwartalne

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")


#--------- B. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 8,0%

print("B. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 8,0%")
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.080 #oprocentowanie w skali roku
oprocentowanie_kwartalne = oprocentowanie / 4
mnoznik_kwartalny = 1 + oprocentowanie_kwartalne

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")



#--------- C. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 8,25%

print("C. KALKULACJA DLA OPROCENTOWANIA ROCZNEGO: 8,25%")
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.0825 #oprocentowanie w skali roku
oprocentowanie_kwartalne = oprocentowanie / 4
mnoznik_kwartalny = 1 + oprocentowanie_kwartalne

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.")

deposit = deposit * (mnoznik_kwartalny)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")

