from turtle import Turtle, Screen
import random
import time

# Setup screen
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to Turtle Race")

# Get user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "Choose a color (red, orange,  yellow, green, blue, purple):")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Draw finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(x=230, y=-100)
finish_line.left(90)
finish_line.pendown()
finish_line.forward(200)

# Create turtles
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# Countdown
countdown_turtle = Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.goto(0, 150)
for count in ["3", "2", "1", "Go!"]:
    countdown_turtle.clear()
    countdown_turtle.write(count, align="center", font=("Arial", 24, "bold"))
    time.sleep(1)
countdown_turtle.clear()

# Start race
is_race_on = bool(user_bet)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            winner_turtle = turtle

            announce = Turtle()
            announce.hideturtle()
            announce.penup()
            announce.goto(0, 0)
            if winning_color == user_bet:
                announce.write(f"You've WON! \n{winning_color.title()} turtle is the winner!", align="center",
                               font=("Arial", 18, "bold"))
            else:
                announce.write(f"You've lost. \n{winning_color.title()} turtle is the winner!", align="center",
                               font=("Arial", 18, "bold"))
            break

        # Move turtle forward randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
