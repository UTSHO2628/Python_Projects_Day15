import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Happy New Year 2025!")

# Firework burst in a star shape
def star_shaped_firework(x, y):
    colors = ["red", "blue", "yellow", "green", "purple", "orange", "white"]
    fire = turtle.Turtle()
    fire.speed(0)
    fire.hideturtle()
    fire.color(random.choice(colors))
    fire.penup()
    fire.goto(x, y)
    fire.pendown()

    # Drawing a star shape
    for _ in range(5):  # Star has 8 points
        fire.forward(30)
        fire.backward(30)
        fire.right(45)  # Angles for star points

# Realistic firework function with star shape
def realistic_fireworks():
    for _ in range(5):  # Multiple fireworks
        launcher = turtle.Turtle()
        launcher.hideturtle()
        launcher.color("white")
        launcher.penup()
        start_x = random.randint(-300, 300)
        start_y = -250  # Start near the bottom
        launcher.goto(start_x, start_y)
        launcher.showturtle()

        # Launch the firework
        launcher.speed(2)
        for _ in range(30):  # Launch to the sky
            launcher.sety(launcher.ycor() + 10)
            time.sleep(0.02)

        launcher.hideturtle()
        star_shaped_firework(launcher.xcor(), launcher.ycor())  # Burst in star shape

# Floating text with live animation and color change
def floating_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(0, -200)
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]

    # Floating and color change effect (smooth animation)
    for _ in range(150):  # Floating for a longer time
        text.clear()
        text.color(random.choice(colors))  # Random color change
        text.write("Happy New Year 2025!", align="center", font=("Arial", 40, "bold"))
        time.sleep(0.1)
        text.sety(text.ycor() + 5)  # Move up smoothly
        if text.ycor() > 250:  # Reset when it goes out of view
            text.sety(-200)

# Countdown function
def countdown():
    counter = turtle.Turtle()
    counter.color("white")
    counter.hideturtle()
    counter.penup()
    counter.goto(0, 50)
    for i in range(5, 0, -1):
        counter.clear()
        counter.write(f"{i}", align="center", font=("Arial", 48, "bold"))
        time.sleep(1)
    counter.clear()
    counter.write("Happy New Year 2025!", align="center", font=("Arial", 36, "bold"))

# Main function
def main():
    countdown()
    realistic_fireworks()
    floating_text()  # Call floating text with animation
    turtle.done()

main()
