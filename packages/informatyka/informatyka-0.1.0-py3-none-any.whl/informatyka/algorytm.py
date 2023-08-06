from .notice import *

def sprawdz(a, b):
    if type(a) and type(b) == int:
        if a > b:
            print(f"Liczba {a} jest większa!")
        elif a == b:
            print(f"Liczby {a} i {b} są równe!")
        elif b > a:
            print(f"Liczba {b} jest większa!")
    else:
        BadNotice()
        