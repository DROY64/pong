import turtle, time

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

# Score variabele
score = 0

# Lifes variable
lifes = 3

# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 Levens: 3", align="center", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {} Levens: {}".format(score, lifes), align="center", font=("Courier", 24, "normal"))
    
def game_over():
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))

while True:
    ball.setx(ball.xcor() + ball.dx) #movement
    ball.sety(ball.ycor() + ball.dy)
    
    #walls
    if (ball.xcor() > 400):
       ball.dx *= -1
    if (ball.ycor() > 300 or ball.ycor() < -300 ):
       ball.dy *= -1
       
    if (ball.dx < 0 and ball.xcor() < -350): # ball vliegt naar de linkerkant.
        if (paddle.ycor() - 60 < ball.ycor() < paddle.ycor() + 60): # bal 'raakt' de pedal
            ball.dx *= -1 # beweeg de bal de andere kant uit (horizontaal)
            while (paddle.ycor() ): #calculate which part of the paddle the ball hits, isolate the pixel it hits on the paddle by subscracting the empty vertex to find the striking location. 
                cor = #get the padle coords and get the ball coords, make a equation to pinpoint how far from the centerline of the paddle the ball hits and then make the while loop run the sequence as many times to then return a number. After the the return we run it through another math equation to then return a deicmal number to give the ball a heading after impact. This is gradually done. First, figure out how to make both coords correlate to an equation that will work with both negatives and positives, and figure out if that's done inside the loop or outside.
            # ball.dy *= -1 # beweeg de bal de andere kant uit (verticaal)
        elif (lifes == 0):
            ball.dx = 0 
            ball.dy = 0
            game_over()
        else:
            ball.goto(0, 0)
            score = score + 1
            lifes = lifes - 1
            print(score, lifes)
            update_score()
            time.sleep(3)
            ball.dx = 0.2 
            ball.dy = -0.2
    wn.update()

# input("Press any key to continue...")  # tijdelijke toevoeging t.b.v. testen