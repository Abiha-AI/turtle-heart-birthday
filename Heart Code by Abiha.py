import math
import turtle

# new window setup
window = turtle.Screen()
window.bgcolor("Pink")
window.title("Happy Birthday")

pen = turtle.Turtle()     # Fixed: removed the 0
pen.speed(0)              # Speed goes here, not above
pen.hideturtle()
pen.penup()

# Color Choice
pen.color("#864104")

# draw the heart
points = 100
for i in range(points):
    angle = (2 * math.pi * i) / points
    
    # heart formula
    x = 16 * (math.sin(angle) ** 3)
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle))
    pen.goto(x * 12, y * 12)
    pen.write("Your Name", align="center", font=("Times New Roman", 7, "bold"))

window.mainloop()