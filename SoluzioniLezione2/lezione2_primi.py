numero = input('Inserire un numero: ')

numero = int(numero)

isPrime = True
for i in range(2, numero):
    if numero % i == 0:
        isPrime = False

    
if isPrime:
    print('Il numero inserito è primo')
else:
    print('il numero inserito non è primo')
