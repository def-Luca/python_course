## Exceptii
# evenimente care apar in cod si intrerup functionarea, practic erorile

#NameError
# print(some variable_that_i_never_declared) # asta e o eroare, da syntax error

#Zero Division Error
# print(3/0)

# Index Error:
# lista = [1, 2, 3, 4]
# print(lsita[9])

# si multe alte erori
#in cod putem anticipa cand apar si sa le handluim
# try - except - else - finally
# raise

#try:
#   executie normala, fara erori
# except:
#   executie cu erori
#   se face handling la eventuale erori
#else:
#   in continuarea lui try daca nu da eroare
#finally:
#   cod care se executa mereu indiferent



try:   #aici codez ce cred ca o sa mearga prost
   if aha: # aici fals
       print("a mers")
except NameError:  # aici codez ce ma astept sa se int e bine sa pun si numele erorri specific
    print("except")   # daca pun alta eroare da tot eroare
else:
    print("else dupa try")  # daca nu da try eroare
finally:
    print("finally vine mereu") # asta se executa mereu chiar si daca pui eroare gresita la except
print("de aici continua")  # daca nu mere try, ia pe except si continua, cu exceptia erori gresite la except

# cazul 2:
aha = 1     # acum aha e definit, ia try, else si except, daca era 0 era bool false si nu lua try, dar lua else
try:
    if aha:
        print("try")
except:
    print("except")
else:
    print("else")
finally:
    print("finally")