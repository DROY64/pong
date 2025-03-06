import turtle

# Venster instellen
wn = turtle.Screen()
wn.title("Pong voor Leonard")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Bal
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Beweeg de bal


# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.penup()
paddle.goto(-350, 0)

# wn.update()

def paddle_up(): 
    y = paddle.ycor() 
    if y < 240: 
        y += 20 
    paddle.sety(y)

def paddle_down(): 
    y = paddle.ycor() 
    if y > -240: 
        y -= 20 
    paddle.sety(y)

# Toetsenbordbinding
wn.listen()
wn.onkeypress(paddle_up, 'Up')
wn.onkeypress(paddle_down, 'Down')

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if (ball.xcor() > 400):
       ball.dx *= -1
    if (ball.ycor() > 300 or ball.ycor() < -300 ):
       ball.dy *= -1
    wn.update()

# input("Press any key to continue...")  # tijdelijke toevoeging t.b.v. testen