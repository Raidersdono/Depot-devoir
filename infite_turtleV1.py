import turtle, random

n=5

turtle.delay(0)
tortuelist=[]
for i in range(n):

    tortue = turtle.Turtle()
    tortue.speed(0)
    tortue.color (random.random(),random.random(),random.random())
    tortuelist.append(tortue)


while True:
    for i in tortuelist:
        i.forward(5)
        a=random.randint(1,360)
        i.left(a)

    