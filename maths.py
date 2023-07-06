def addition(a, b):
    return a + b

def soustraction(a,b):
    return a-b


def division(a, b):
    if (b != 0):
        return a / b
    else:
        print("erreur: division par 0")

def multiplication(a,b):
    return a*b

def saisir_nombre():
    while True:
        try:
            n = float(input("Saisir le nombre \n"))
            return n
        except ValueError:
            print("saisir un nombre valide")
