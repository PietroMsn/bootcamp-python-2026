import turtle as t
colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']

for x in range(100):
    t.pencolor(colors[x % 6])
    t.width(5)
    t.forward(x)
    t.left(20)
