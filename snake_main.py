import turtle  
import time
import random

delay = 0.1
score = 0
highScore = 0

#ventana
wds = turtle.Screen()
wds.title("Serpiente Loca")
wds.setup(width=600, height=600)
wds.tracer(0)
wds.bgcolor("black")

#puntos
puntos = turtle.Turtle()
puntos.speed(0)
puntos.color("blue")
puntos.penup()
puntos.hideturtle()
puntos.goto(0,260)


#frutita
frutita = turtle.Turtle()
frutita.color("green")
frutita.shape("circle")
frutita.penup()
frutita.goto(0,0)

#serpiente
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
snake.color("white")
#cuerpo serpiente
cuerpo = []

#funciones
def arriba():
    snake.direction = "up"
def abajo():
    snake.direction = "down"
def derecha():
    snake.direction = "right"
def izquierda():
    snake.direction = "left"

def mov():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#Teclado
wds.listen()
wds.onkeypress(arriba, "Up")
wds.onkeypress(abajo, "Down")
wds.onkeypress(izquierda, "Left")
wds.onkeypress(derecha, "Right")

#main
while True:
    wds.update()

    #colisiones
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        wds._bgcolor("red")
        time.sleep(0.5)
        wds._bgcolor("black")
        snake.goto(0,0)
        snake.direction = "stop"
        for c in cuerpo:
            c.hideturtle()
        cuerpo.clear()
        score=0
        puntos.clear()
        puntos.write("Puntacos: {} Mejor: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
        
    if snake.distance(frutita) <= 20:
        #aumentar punto
        score += 1
        if score > highScore:
            highScore=score
        
        puntos.clear()
        puntos.write("Puntacos: {} Mejor: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

        #muevo la comida
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        frutita.goto(x,y)
        
        cuerpo_nuevo = turtle.Turtle()
        cuerpo_nuevo.speed(0)
        cuerpo_nuevo.shape("square")
        cuerpo_nuevo.color("grey")
        cuerpo_nuevo.penup()
        cuerpo.append(cuerpo_nuevo)

    #rastro del cuerpo
    totalCuerpos=len(cuerpo)
    for i in range(totalCuerpos-1,0,-1):
        x=cuerpo[i-1].xcor()
        y=cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)
    
    if totalCuerpos > 0:
        x=snake.xcor()
        y=snake.ycor()
        cuerpo[0].goto(x,y)

    mov()
    
    #colision cuerpo
    for s in cuerpo:
        if s.distance(snake) < 20:
            wds._bgcolor("red")
            time.sleep(0.5)
            wds._bgcolor("black")
            snake.goto(0,0)
            snake.direction = "stop"
            for c in cuerpo:
                c.hideturtle()
            cuerpo.clear()
            score=0
            puntos.clear()
            puntos.write("Puntacos: {} Mejor: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(delay)