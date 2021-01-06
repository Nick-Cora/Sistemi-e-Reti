''''
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, composto da 6 coppie di
cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.

''''


import random

dictCar = {"1": [48,57], "2": [65,70]}

def generator():
    mac = ""
    for n in range (6):
        for x in range (2):
            rand = random.randint(1, 2)
            if rand == 1:
                mac = mac + chr(random.randint(dictCar["1"][0], dictCar["1"][1]))
            else:
                mac = mac + chr(random.randint(dictCar["2"][0], dictCar["2"][1]))
            x = x + 1
        n = n + 1
        if n != 6:
            mac = mac + ":"
        else:    
            print(f"MAC:  {mac}")

def main():
    generator()

if __name__ == "__main__":
    main()