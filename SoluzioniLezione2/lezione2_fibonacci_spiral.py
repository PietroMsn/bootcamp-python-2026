import turtle

def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b

    return b


turtle.speed(10)
turtle.right(90)

for n in range(50):

    raggio = fib(n)
    turtle.circle(raggio, 90)
