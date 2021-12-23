# import turtle module
import turtle

wind = turtle.Screen()  # intialize screen
wind.title("Ping Pong")  # set the title of the window
wind.bgcolor("black")  # set the background Color of the window
wind.setup(width=800, height=600)  # set the width and height of the window
wind.tracer(0)  # stop the window from updating automatically

# player1
player1 = turtle.Turtle()  # intialize turtle object(shape)
player1.speed(0)  # set the spped of animation
player1.shape("square")  # set the shape of object
player1.color("blue")  # set the color of object
player1.shapesize(stretch_wid=5, stretch_len=1)  # stretches the sahpe to meet the size
player1.penup()  # stop object from drawing lines
player1.goto(-350, 0)  # set the position of object

# player2
player2 = turtle.Turtle()  # intialize turtle object(shape)
player2.speed(0)  # set the spped of animation
player2.shape("square")  # set the shape of object
player2.color("red")  # set the color of object
player2.shapesize(stretch_wid=5, stretch_len=1)  # stretches the sahpe to meet the size
player2.penup()  # stop object from drawing lines
player2.goto(350, 0)  # set the position of object

# ball
ball = turtle.Turtle()  # intialize turtle object(shape)
ball.speed(0)  # set the spped of animation
ball.shape("circle")  # set the shape of object
ball.color("white")  # set the color of object
ball.penup()  # stop object from drawing lines
ball.goto(0, 0)  # set the position of object
ball.dx = 0.5
ball.dy = 0.5

# score
score1 = 0  # set score of player1
score2 = 0  # set score of player1
Score = turtle.Turtle()  # intialize turtle object(shape)
Score.speed(0)  # set the spped of animation
Score.color("white")  # set the color of object
Score.penup()  # stop object from drawing lines
Score.hideturtle()
Score.goto(0, 260)  # set the position of object
# write of window
Score.write(f"Player1 : {score1}    Player2: {score2}", align="center", font=("Courier", 24, "normal"))


# functions
def player1_up():
    player1.sety(player1.ycor() + 20)  # move up by 20 unit for player1


def player1_down():
    player1.sety(player1.ycor() - 20)  # move down by 20 unit for player1


def player2_up():
    player2.sety(player2.ycor() + 20)  # move up by 20 unit for player2


def player2_down():
    player2.sety(player2.ycor() - 20)  # move down by 20 unit for player2


# keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(player1_up, "w")  # when press w the function of player1 invoked
wind.onkeypress(player1_down, "s")  # when press s the function of player1 invoked
wind.onkeypress(player2_up, "Up")  # when press up Arrow the function of player2 invoked
wind.onkeypress(player2_down, "Down")  # when press down Arrow function of player2 invoked

# main game loop
while True:
    wind.update()  # updates the screen everytime loop run

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 and everytime loop run +0.3 unit x axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and everytime loop run +0.3 unit y axis

    # border check , top border +300 , bottom border -300, ball is 20
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate
        ball.dy *= -1  # reverse direction, making 0.5 --> -0.5

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)  # set y coordinate
        ball.dy *= -1  # reverse direction, making -0.5 --> 0.5

    if ball.xcor() > 390:  # if ball is right bottom border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse direction, making 0.5 --> -0.5
        score1 += 1
        Score.clear()
        Score.write(f"Player1 : {score1}    Player2: {score2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse direction, making -0.5 --> 0.5
        score2 += 1
        Score.clear()
        Score.write(f"Player1 : {score1}    Player2: {score2}", align="center", font=("Courier", 24, "normal"))

    # touch on player2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    # touch on player1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
