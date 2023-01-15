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
_terabajt = 1024 * 1024
a = _terabajt * 13
b = 194
print("Na pobranie danych z sieci o rozmiarze 13 TB potrzeba:", round(((a / b) * 5) / 3600), "godzin\n\n")

# print("Zysk z 3 letniej lokaty bankowej, wynosi:", round(deposit - inwestowane_srodki ,2), "zl.") # z użyciem zaokrlągenia, do dwóch miejsc po przecinku



# ZADANIE 3
 # Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
 # następujących założeniach:
 # • własne środki 30 tys. zł,
 # • roczna lokata kapitału,
 # • kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
 # • oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
 # • pokazać salda po każdym kwartale,
 # • wyliczyć roczny zysk.

print ("ZADANIE 3 \n")
      #------- A. Kalkulacje DLA OPROCENTOWANIA 7,5% w skali roku
print ('A. Kalkulacje DLA OPROCENTOWANIA 7,5% w skali roku')
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.075
oprocentowanie_kwartalne = oprocentowanie / 4

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")


#------- B. Kalkulacje DLA OPROCENTOWANIA 8,0% w skali roku
print ('B. Kalkulacje DLA OPROCENTOWANIA 8,0% w skali roku')
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.080
oprocentowanie_kwartalne = oprocentowanie / 4

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")



#------- C. Kalkulacje DLA OPROCENTOWANIA 8,25% w skali roku
print ('C. Kalkulacje DLA OPROCENTOWANIA 8,25% w skali roku')
inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.0825
oprocentowanie_kwartalne = oprocentowanie / 4

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Saldo konta z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki + inwestowane_srodki), "zl.")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")














