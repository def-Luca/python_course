import random
while True:
    dice_roll = (random.randint(1, 6))
    numar = input("ghiciti numarul zarului")
    if numar.isdigit():
        numar = int(numar)
        if numar <1 or numar>6:
            print("false input, again")
        else:
            if numar == dice_roll:
                print(f"Corect, ai ales {numar} si zarul a fost {dice_roll}")
                break
            elif numar > dice_roll:
                print ("numarul este mai mic, mai incearca")
            else:
                print("numarul este mai mare, mai incearca")
    else:
        print("false input, again")

print("O zi buna!")