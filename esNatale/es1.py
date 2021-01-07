'''
Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri qualora
l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.
'''


import random

dictCar = {"1": [48,57], "2": [65,90], "3": [97,122]}

def generaPassword(dim):
    pw = ""
    cnt = 0
    while cnt != dim:
        rand = random.randint(1, 3)
        if rand == 1:
            pw = pw + chr(random.randint(dictCar["1"][0], dictCar["1"][1]))
        elif rand == 2:
            pw = pw + chr(random.randint(dictCar["2"][0], dictCar["2"][1]))
        elif rand == 3:
            pw = pw + chr(random.randint(dictCar["3"][0], dictCar["3"][1]))
        cnt = cnt + 1
    print(f"La password è {pw}")



def main():
    scelta = int(input("1 per password semplice, 2 per password complessa\n"))
    if scelta == 1:
        dim = 8
    elif scelta == 2:
        dim = 20
    elif scelta != 1 or scelta != 0:
        raise Exception("ERRORE: scelta errata")    
    generaPassword(dim)
       

if __name__ == "__main__":
    main()
