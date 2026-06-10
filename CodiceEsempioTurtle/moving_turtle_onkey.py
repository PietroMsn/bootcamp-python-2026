import turtle

sc = turtle.Screen()


my_turtle = turtle.Turtle()
my_turtle.speed(5)
my_turtle.shape("circle")
my_turtle.color("blue")
my_turtle.penup()
my_turtle.dx = 1


def giraSinistra():
    my_turtle.dx = -1

def giraDestra():
    my_turtle.dx = 1


    
sc.listen()
sc.onkeypress(giraSinistra, 'Left')
sc.onkeypress(giraDestra, 'Right')

while True:
	sc.update()

	my_turtle.setx(my_turtle.xcor() + my_turtle.dx)
