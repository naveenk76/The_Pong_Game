from turtle import Screen
from pedal import Pedal
from ball import Ball
import time
from score_board import ScoreBoard


screen=Screen()
screen.title("PONG")
screen.setup(height=600,width=800)
screen.bgcolor('black')
screen.tracer(0)

r_pedal=Pedal((380,0))
l_pedal=Pedal((-387,0))
ball=Ball()
score_board=ScoreBoard()

screen.listen()
screen.onkey(r_pedal.go_up,"Up")
screen.onkey(r_pedal.go_down,"Down")

screen.onkey(l_pedal.go_up,"w")
screen.onkey(l_pedal.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
       ball.bounce_y()
    #Detect collision with ball
    if ball.distance(r_pedal)<50 and ball.xcor()>340 or ball.distance(l_pedal)<50 and ball.xcor()<-340:
       ball.bounce_x()
    #Detect r_pedal misses
    if ball.xcor()>380:
        score_board.l_point()
        ball.reset_position()
    #Detect l_pedal misses
    if ball.xcor()<-380:
        score_board.r_point()
        ball.reset_position()



screen.exitonclick()