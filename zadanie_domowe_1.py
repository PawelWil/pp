# ZADANIE 1
 # Wyświetl na ekranie następujący wzór:

# print("      *        *")
# print("      **      **")
# print("      ***    ***")
# print("      ****  ****")
# print("      **********")
# print("      ****  ****")
# print("      ***    ***")
# print("      **      **")
# print("      *        *")


# ZADANIE 2
 # Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie
 # danych z sieci o rozmiarze 13 TB, jeżeli wiesz, że plik o rozmiarze 194 MB
 # udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.

# * 1 terabajt[TB] = 1_000_000 megabajtów[MB] //=1024 * 1024
# a = 13_000_000 #13 * 1024 * 1024
# b = 194
# print (round((a / b) * 5) / 3600)
# print(round(((((a / b) * 5) / 3600)), 0))


# ZADANIE 3
 # Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
 # następujących założeniach:
 # • własne środki 30 tys. zł,
 # • roczna lokata kapitału,
 # • kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
 # • oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
 # • pokazać salda po każdym kwartale,
 # • wyliczyć roczny zysk.
 
 # najlepiej użyć wzoru na procent składany: https://www.matemaks.pl/procent-skladany-kapitalizacja-odsetek.html
 # wtedy deposit(k) = deposit * (1 + oprocentowanie_kwartalne) ^ k 
 # ale można też tak jak zrobiłeś bez wzoru - też prawie poprawnie :)

inwestowane_srodki = 30_000. # własne inwestowane środki
deposit = inwestowane_srodki
oprocentowanie = 0.075 // w skali roku - poprawione :)
oprocentowanie_kwartalne = oprocentowanie / 4 

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Zysk z 1-rocznej lokaty bankowej, po I Kwartale, wynosi:", (deposit-inwestowane_srodki), "zl.\n")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Zysk z 1-rocznej lokaty bankowej, po II kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.\n")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Zysk z 1-rocznej lokaty bankowej, po III kwartale, wynosi:", (deposit - inwestowane_srodki), "zl.\n")

deposit = deposit * (1 + oprocentowanie_kwartalne)
print("Zysk z 1-rocznej lokaty bankowej, po IV kwartale wynosi:", (deposit - inwestowane_srodki), "zl.\n")

print ('Roczny zysk wynosi:', (deposit - inwestowane_srodki), "zl.\n")







