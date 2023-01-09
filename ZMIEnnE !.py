# !!! ZMIEnnE !!!
# ważna uwaga: zmienne w kodzie zawsze wpisuje bez apostrofów, czy cudzysłowów + z małych liter +
# łącze je za pomocą podkreślników + nie mogą być za długie !!

# 1. NAZWY ZMIENNYCH
# zmienne piszemy zawsze malymi literami + pomiędzy dwoma słowami zmiennej zawsze dajemy '_' +

#var = 1 # to jest zmienna o nazwie var, ktra ma wartość 1
#print(var) # tu wyswietlamy warość zmiennej var

# account_balance = 1000. # zmienna o nazwie accout_balance - zmienna typu float
# user = "Jan Kowalski" # zmienna typu ciąg znaków=string
# print(user,", ma na koncie:", account_balance)

# RÓŻnE spososoby zapisu zmiennych:
#my_var = 345 # zmienna o nazwie my_var
#number_of_days = 300 # zmienna o nazwie number_of_days: 1 sposób, za pomocą podkreślnikow
#total_years = 4 # zmienna o nazwie total_years

#numberOfDays = 300 # zmienna o nazwie numberOfDays: 2 sposób, za pomocą dużych liter, ale raczej tego unikać
#totalYears = 4 # zmienna o nazwie totalYears


# 2. Dynamiczne typowanie -- jak się to stosuje to poprzednia wartość po prostu jest zastąpiona tą ostatnią, czyli w poniższym przypadku ostatnią wartością, która się wyswietli to kokarda

# jak widać dodaliśmy do zmiennej 'a' liczbę(int) + słowo(string) i powinna się wyświtlić kokarda, bo nadpisała 4
# a = 4
# print(a)
# a ="kokarda"
# print(a)

# 3. Złożone operatory przypisania

# a. operator przypisania dla '+' i '-'
# x = 1 # chce podnieś tej zmiennej wartość o 1, czyli jest to inkrementacja, przeciwieństwiem jest dekrementacja, czyli zmniejsznie. Może to być o 1 lub inną wartość
# x = x + 1
# x += 1
# print(x)

# b. operator złożonego przypisania dla potęgowania '**'
# e = 2
# x = 2
# e = e ** x
# e **= x
# print(e)

