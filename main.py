from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.listen()
screen.delay(3)
screen.tracer(0)
snake_body = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

food = Turtle()
food.shape("square")
food.penup()
food.shapesize(0.5)
food.color("white")
food.setpos(160,160)

for position in starting_positions:
    new_part = Turtle()
    new_part.speed(0)
    new_part.penup()
    new_part.shape("square")
    new_part.setpos(position)
    snake_body.append(new_part)
screen.update()
all_positions = starting_positions


def generate_random():
    while True:
        number = random.randint(-220, 220)
        if number % 20 == 0:
            break
    return number


def spawn_food():
    while True:
        x_pos = generate_random()
        y_pos = generate_random()
        temp = 0
        for position in all_positions:
            if x_pos == round(position[0]) and y_pos == round(position[1]):
                temp += 1
        if temp == 0:
            break
    food.setpos(x_pos, y_pos)


def turn_north():
    if snake_body[0].heading() == 270:
        return
    snake_body[0].setheading(90)


def turn_west():
    if snake_body[0].heading() == 0:
        return
    snake_body[0].setheading(180)


def turn_south():
    if snake_body[0].heading() == 90:
        return
    snake_body[0].setheading(270)


def turn_east():
    if snake_body[0].heading() == 180:
        return
    snake_body[0].setheading(0)


def border_check():
    height = screen.window_height()
    width = screen.window_width()

    if snake_body[0].xcor() >= (width / 2) - 10:
        return False
    if snake_body[0].ycor() >= (height/ 2) - 10:
        return False
    if snake_body[0].xcor() <= -((width / 2) - 10):
        return False
    if snake_body[0].ycor() <= -((height / 2) - 10):
        return False
    return True


def is_eaten():

    if round(snake_body[0].xcor()) == round(food.xcor()) and round(snake_body[0].ycor()) == round(food.ycor()):
        return True
    return False


def add_part():
    newest_part = Turtle()
    newest_part.speed(0)
    newest_part.penup()
    newest_part.shape("square")
    newest_part.setpos(snake_body[len(snake_body) - 1].pos())
    snake_body.append(newest_part)
    all_positions.append(newest_part.position())


def update_pos():
    for i in range(0,len(snake_body)):
        all_positions[i] = snake_body[i].pos()
        print(all_positions[i])


def part_collision():
    for i in range(1, len(all_positions)):
        if snake_body[0].heading() == 0:
            if round(all_positions[0][0]) == round(all_positions[i][0]) - 20 and round(all_positions[0][1]) == round(all_positions[i][1]):
                return True
        elif snake_body[0].heading() == 90:
            if round(all_positions[0][0]) == round(all_positions[i][0]) and round(all_positions[0][1]) == round(all_positions[i][1]) - 20:
                return True
        elif snake_body[0].heading() == 180:
            if round(all_positions[0][0]) == round(all_positions[i][0]) + 20 and round(all_positions[0][1]) == round(all_positions[i][1]):
                return True
        else:
            if round(all_positions[0][0]) == round(all_positions[i][0]) and round(all_positions[0][1]) == round(all_positions[i][1]) + 20:
                return True
    return False


count = 0

playing = True
while playing:
    if part_collision():
        playing = False
    if not border_check():
        playing = False
    screen.update()
    time.sleep(0.12)
    update_pos()
    if is_eaten():
        spawn_food()
        count += 1
        add_part()
    for j in range(len(snake_body) - 1, 0, -1):
        snake_body[j].setpos(snake_body[j-1].pos())
    snake_body[0].forward(20)
    screen.listen()
    screen.onkey(key="w", fun=turn_north)
    screen.onkey(key="a", fun=turn_west)
    screen.onkey(key="s", fun=turn_south)
    screen.onkey(key="d", fun=turn_east)

screen.exitonclick()






