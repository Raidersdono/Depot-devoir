import turtle, math, random

maTortue = turtle.Turtle()
maFenetre = turtle.Screen()

maFenetre.colormode(255)
maTortue.shape("turtle")
maTortue.speed(0)
turtle.delay(0)
turtle.listen()

def goUp():
    maTortue.setheading(90)
    #maTortue.forward(playerSpeed)

def goLeft():
    maTortue.setheading(180)
    #maTortue.forward(playerSpeed)

def goDown():
    maTortue.setheading(270)
    #maTortue.forward(playerSpeed)

def goRight():
    maTortue.setheading(0)
    #maTortue.forward(playerSpeed)

turtle.onkeypress(goUp,"Up")
turtle.onkeypress(goLeft,"Left")
turtle.onkeypress(goDown,"Down")
turtle.onkeypress(goRight,"Right")


#Fonction distance
def distance(A, B):
    return(math.sqrt((float(A[0]) - float(B[0]))**2 + (float(A[1]) - float(B[1]))**2))

#Dessin d'une marche aléatoire
pas = 3
nbDeTortues = 15
startingSquareWidth = 300
listeDeTortues = []
facteurDeTaille = 12.0
playerSpeed = 5

for i in range(nbDeTortues):
    tempTortue = turtle.Turtle()
    tempTortue.shape('turtle')

    #Initialisation à une couleur aléatoire
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tempTortue.color((R, G, B))

    #Initialisation à une position aléatoire
    posX = random.random() * startingSquareWidth - startingSquareWidth//2
    posY = random.random() * startingSquareWidth - startingSquareWidth//2
    tempTortue.penup()
    tempTortue.setpos(posX, posY)
    tempTortue.pendown()
    tempTortue.speed(10)

    listeDeTortues.append(tempTortue)

while True:

    for k in listeDeTortues:
        k.forward(10)
        z=random.randint(1,300)
        k.right(z)


    maTortue.forward(playerSpeed)

    for k in listeDeTortues:
        for l in listeDeTortues:
            if (k.isvisible() and l.isvisible() and k != l and distance(k.position(), l.position()) <= facteurDeTaille * max(k.shapesize()[0], l.shapesize()[0])):
                #Si les conditions sont remplies, il y a phagocytose
                if (k.shapesize()[0] >= l.shapesize()[0]):
                    k.speed(k.speed() - 2)
                    k.shapesize(k.shapesize()[0] * 1.3, k.shapesize()[1]* 1.3)
                    l.hideturtle()
                    l.penup()
                else:
                    l.speed(l.speed() - 2)
                    l.shapesize(l.shapesize()[0]* 1.3, l.shapesize()[1]* 1.3)
                    k.hideturtle()
                    k.penup()
        
        if (k.isvisible() and maTortue.isvisible() and k != maTortue and distance(k.position(), maTortue.position()) <= facteurDeTaille * max(k.shapesize()[0], maTortue.shapesize()[0])):
                #Si les conditions sont remplies, il y a phagocytose
                if (k.shapesize()[0] > maTortue.shapesize()[0]):
                    k.shapesize(k.shapesize()[0] * 1.3, k.shapesize()[1]* 1.3)
                    maTortue.hideturtle()
                    maTortue.penup()
                else:
                    maTortue.speed(maTortue.speed() - 2)
                    playerSpeed /= 1.3
                    maTortue.shapesize(maTortue.shapesize()[0]* 1.3, maTortue.shapesize()[1]* 1.3)
                    k.hideturtle()
                    k.penup()
        

#Fin du programme

#code aidez par quentin, ne comprend pas tous pour l'instant mais essaye de son mieux.