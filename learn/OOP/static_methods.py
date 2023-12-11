# static method folosesti cand vrei sa grupezi diferite functii intr o clasa!
#practic definesti niste functii pe care le folosesti mai incolo

class Mate:
    @staticmethod #nu are acces la instantele clasei, doar fac ceva fara sa schimbe ceva
    def add5(x):  # nu ai nevoie de cls sau self!! e doar o fnctie pe care o organizezi undeva
        return x + 5

print(Mate.add5(5))
