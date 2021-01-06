''''
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.

''''


def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


def main():
    num=0
    while(num < 1):
        num=int(input("inserire un numero positivo (soglia per la sequenza):  "))

    for cnt in range (num):
        print(fibo(cnt))

if __name__ == "__main__":
    main()