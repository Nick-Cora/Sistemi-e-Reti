'''
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella
posta 15 posizioni più avanti nell'alfabeto. Scrivi una semplice funzione in grado di criptare una stringa passata,
o decriptarla se la stringa è già stata precedentemente codificata.

'''


def cript(string):
    temp = ""
    for car in string:
        car = ord(car) + 15
        car = chr(car)
        temp = temp + car
    print(f"Stringa criptata: {temp}")

def decript(string):
    temp = ""
    for car in string:
        car = ord(car) - 15
        car = chr(car)
        temp = temp + car
    print(f"Stringa decriptata: {temp}")


def main():
    scelta = int(input("1 per criptare la stringa, 2 per decriptare la stringa\n"))
    stringa = str(input("Inserire la stringa:\n"))
    if scelta == 1:
        cript(stringa)
    elif scelta == 2:
        decript(stringa)
    
    

if __name__ == "__main__":
    main()