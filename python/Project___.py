import turtle

wind = turtle.Screen()

wind.title("ping Pong by Mo'men")

wind.bgcolor("black")

wind.tracer(0)

wind.setup(width=800 , height=600)


#madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=6 , stretch_len=2)   


#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=6 , stretch_len=2)   

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

#score
score =turtle.Turtle
score.speed(0)
score.color("white")
score.goto(0, 260)

  

#functions
def madrab1_up():
    y = madrab1.ycor()
    y+= 20
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor()
    y-= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y+= 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y-= 20
    madrab2.sety(y)



#keyboard
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.listen()
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")



#maingameLoop
while True:
    wind.update()
#move the ball
    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)
      
#Movement

    if ball.ycor() >290 :

      ball.sety(290)
      ball.dy *= -1

    if ball.ycor() <-290 :

      ball.sety(-290)
      ball.dy *= -1


    if ball.xcor() >390 :

      ball.goto(0, 0)
      ball.dx *= -1

    if ball.xcor() <-390 :

    ball.goto(0, 0)
    ball.dx *= -1

    
   



   


   
    