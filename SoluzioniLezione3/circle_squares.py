import turtle


sc = turtle.Screen()
sc.bgcolor('black')
colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green', 'white', 'cyan']

raggio = 100


iterazioni = 50

for i in range(iterazioni):
    turtle.pencolor(colors[i % len(colors)])
    turtle.circle(raggio, 360, 4) 
    
    turtle.left(360 / iterazioni)
