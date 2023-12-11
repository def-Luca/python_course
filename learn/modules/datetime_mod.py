from datetime import date, timedelta

azi = date.today()
print(azi.year, azi.month, azi.day)  # poti sa accesezi separat componentele

zi_nastere = date(1997, 7, 18)
zi_nastere2 = date(1997, 10, 22)
gvr = date(1956, 1, 31)

# cum sa faci time difference fata de o data

dt = timedelta(14)
print(zi_nastere + dt)
print(zi_nastere)

zi_nastere_format = zi_nastere.strftime(
    "%A, %B, %d, %Y"
)  # asa rescrii formatul standard de data

print(f"sunt nascut pe {zi_nastere_format}")

mesaj = "sunt nascut pe {:%A, %B, %d, %Y}"
print(mesaj.format(zi_nastere))
# alta varianta de formatare data

import datetime  # aici importez tot modulul

data_lansare = datetime.date(2017, 3, 30)
timp_lansare = datetime.time(22, 27, 0)
timpdata_lansare = datetime.datetime(2017, 3, 30, 22, 22, 0)

print(data_lansare)
print(timp_lansare)
print(timpdata_lansare)

now = datetime.datetime.today()  # accesezi si microsecundele
print(now)

# cum convertesti un string intr un obiect datetime

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
