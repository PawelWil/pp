# DANE:
inwestowane_srodki = 46_567.
deposit = inwestowane_srodki
oprocentowanie = 1.075

#inwestowane_srodki = inwestowane_srodki * oprocentowanie # --> 1 rok
#inwestowane_srodki = inwestowane_srodki * oprocentowanie # --> 2 rok
#inwestowane_srodki = inwestowane_srodki * oprocentowanie # --> 3 rok

# obliczenie kapitalizacji odsetek/zysku z użyciem złożonego operatora przypisania
deposit *= oprocentowanie #tu mamy kapitalizacje odsetek/zysk po pierwszym roku
deposit *= oprocentowanie #tu mamy kapitalizacje odsetek/zysk po drugim roku, powiększonym o kapitalizacje po pierwszym roku
deposit *= oprocentowanie #tu mamy kapitalizacje odsetek/zysk po trzecim roku, powiększonym o kapitalizacje po drugim roku

# Finalny zysk z 3 letniej lokaty bankowej
print("Zysk z 3 letniej lokaty bankowej, wynosi:", round(deposit - inwestowane_srodki ,2), "zl.") # z użyciem zaokrlągenia, do dwóch miejsc po przecinku
