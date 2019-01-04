import turtle

Max = int(input("Please input number:"))
i = 3
j = 50

turtle.speed(10)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()

while i <= Max:
    turtle.circle(j, steps=i)
    i += 1
    j += 10
    if i > Max:
        break

turtle.exitonclick()
