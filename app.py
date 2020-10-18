import turtle
import os

wn = turtle.Screen()
wn.title("pong by @simonestic")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops the window from updating

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of the animation -> maximum possible
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() #do not raw line when moving 
paddle_a.goto(-350,0) # 0 0 is the middle

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of the animation -> maximum possible
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #do not raw line when moving 
paddle_b.goto(350,0) # 0 0 is the middle

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 2
ball.dy = -2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B : 0", align="center", font=("Courior", 24, "normal"))

#functions
def padd_a_up():
    y = paddle_a.ycor() #get the y position of the paddle_a
    y += 20
    paddle_a.sety(y)

def padd_a_down():
    y = paddle_a.ycor() #get the y position of the paddle_a
    y -= 20
    paddle_a.sety(y)

def padd_b_up():
    y = paddle_b.ycor() #get the y position of the paddle_a
    y += 20
    paddle_b.sety(y)

def padd_b_down():
    y = paddle_b.ycor() #get the y position of the paddle_a
    y -= 20
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(padd_a_up,'w')
wn.onkeypress(padd_a_down,'s')
wn.onkeypress(padd_b_up,"Up")
wn.onkeypress(padd_b_down,"Down")

# main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&") #runs an os command for us
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&") #runs an os command for us

    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b), align="center", font=("Courior", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b), align="center", font=("Courior", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
        os.system("afplay bounce.wav&") #runs an os command for us

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340) 
        ball.dx *= -1 
        print("ball.xcor() ->  " + str(ball.xcor()))
        os.system("afplay bounce.wav&") #runs an os command for us