from .notice import *

def plus(a, b): 
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Wynik Dodawania to: {a + b}")

def minus(a, b):
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Wynik odejmowania to: {a + b}")

def razy(a, b):
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Wynik mnozenia to: {a * b}")

def przez(a, b):
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Wynik dzielenia to: {a / b}")

def reszta(a, b):
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Reszta z dzielenia to: {a % b}")

def kwadrat(a):
    if type(a) != int:
        BadNotice()
    else:
        print(f"Wynik potegowania: {a * a}")

def dzieleniebez(a, b):
    if type(a) and type(b) != int:
        BadNotice()
    else:
        print(f"Wynik dzielenia bez reszty to: {a // b}")           