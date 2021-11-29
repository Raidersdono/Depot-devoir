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
        a=random.randint(1,3)
        
        if a == 1:
            i.left(90)

        elif a==2:
            i.forward(0)

        else :
            i.right(90)
