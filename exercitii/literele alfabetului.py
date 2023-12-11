def litera_alfabet(nr):
    alfabet= "abcdefghijklmnopqrstuvwxyz"
    return alfabet.index(nr)+1
    print(f"litera {nr} este a {alfabet.index(nr) + 1}-a litera a alfabetului")

print(litera_alfabet("h"))

