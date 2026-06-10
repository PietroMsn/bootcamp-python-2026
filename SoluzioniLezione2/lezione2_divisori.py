div = input('inserisci un numero: ')

div = int(div)

for i in range(2, div):
    if div % i == 0:
        print('un divisore è: ', i)
