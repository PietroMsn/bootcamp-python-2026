import turtle

sc = turtle.Screen()


my_turtle = turtle.Turtle()
my_turtle.speed(5)
my_turtle.shape("circle")
my_turtle.color("blue")
my_turtle.penup()
my_turtle.dx = 1


while True:
	sc.update()

	my_turtle.setx(my_turtle.xcor() + my_turtle.dx)


