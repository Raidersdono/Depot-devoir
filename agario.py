import turtle, math, random

t1 = turtle.Turtle()

def move_forward():
    t1.forward(10)

def move_left():
    t1.left(90)
    t1.forward(10)

def move_right():
    t1.right(90)
    t1.forward(10)

def move_backward():
    t1.backward(10)

turtle.onkey(move_forward,'z')
turtle.onkey(move_backward,'s')
turtle.onkey(move_left,'q')
turtle.onkey(move_right,'d')

turtle.listen

t1.speed(0)

def tortue_aleatoire(tor,size):
    tor.shapesize(size*0.1)
    tor.forward(random.randint(0,50))
    tor.left(random.randint(-100,100))
    position = [tor.xcor(),tor.ycor()]
    position = [max(min(position[0], 300), -300),max(min(position[1], 300), -300)]
    tor.goto(position)


def check_collision(listtor,sizen,n):
    global listeTortue
    global listeTaille
    position = []
    for tor in listtor:
        position.append((math.floor(tor.xcor()),math.floor(tor.ycor())))
    for i in range(len(position)):
        if i != n:
            if distance(position[n],position[i]) < sizen + 10:
                if sizen <= listeTaille[i]:
                    listeTaille[i] += listeTaille[n]
                    listeTaille.pop(n)
                    listeTortue[n].hideturtle()
                    listeTortue[n].clear()
                    listeTortue.pop(n)
                    

def distance(pos1,pos2):
    deltax = pos1[0] - pos2[0]
    deltay = pos1[1] - pos2[1]
    distance = deltax**2 + deltay**2
    
    return(math.sqrt(float(distance)))

listeTortue = []
listeTaille = []
for i in range(50):
    listeTortue.append(turtle.Turtle())
    listeTaille.append(1)
for i in listeTortue:
    i.penup()
    i.pencolor((random.random(),random.random(),random.random()))
    i.fillcolor((random.random(),random.random(),random.random()))
    i.goto(random.randint(-300,300),random.randint(-300,300))
    i.shapesize(1*0.1)
    i.speed(0)
    i.shape("circle")

while 1==1:
    l = len(listeTortue)
    for i in range(l):

        if  len(listeTortue) == l:
            tortue_aleatoire(listeTortue[i],listeTaille[i])
            check_collision(listeTortue,listeTaille[i],i)