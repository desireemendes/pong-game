from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


# width = 20
# height = 100
# x_pos = 350
# y_pos = 0

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
  new_y = paddle.ycor() + 20
  paddle.goto(paddle.xcor(), new_y)

def go_down():
  new_y = paddle.ycor() - 20
  paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")

screen.exitonclick()
# setposition(350, 0)
