import turtle

sc = turtle.Screen()
sc.setup(width=1000, height=600)


def mia_funzione():
    sc.bye()



sc.listen()
sc.onkeypress(mia_funzione, 'e')
