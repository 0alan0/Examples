import turtle

r = 400	#半径
a =50	#边距
b = 14	#字体大小
x,y = 0,-r

turtle.setup(width=1200,height=1200, startx=500, starty=0)

turtle.penup()
turtle.goto(x,y)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r,-180)
turtle.circle(r/2,-180)
turtle.circle(-r/2,-180)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(-r,-180)
turtle.circle(-r/2,180)
turtle.circle(r/2,180)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y+3*r/8)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r/8)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y+11*r/8)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(r/8)
turtle.end_fill()

# =================================================

turtle.penup()
turtle.goto(x,y+3*r/8)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r/8,-180)
turtle.circle(r/16,-180)
turtle.circle(-r/16,-180)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(-r/8,-180)
turtle.circle(-r/16,180)
turtle.circle(r/16,180)
turtle.end_fill()



turtle.penup()
turtle.goto(x,y+27*r/64)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r/64)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y+35*r/64)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(r/64)
turtle.end_fill()

# =================================================

turtle.penup()
turtle.goto(x,y+11*r/8)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r/8,-180)
turtle.circle(r/16,-180)
turtle.circle(-r/16,-180)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(-r/8,-180)
turtle.circle(-r/16,180)
turtle.circle(r/16,180)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y+91*r/64)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('white')
turtle.circle(r/64)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y+99*r/64)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('black')
turtle.circle(r/64)
turtle.end_fill()

#=================================================
turtle.penup()
turtle.goto(x,y-a)
turtle.pendown()
turtle.write("冬至", font=("微软雅黑", b, "normal"))
turtle.penup()
turtle.goto(x-r-a-2*b,y+r)
turtle.pendown()
turtle.write("春分", font=("微软雅黑", b, "normal"))
turtle.penup()
turtle.goto(x,y+2*r+a-b)
turtle.pendown()
turtle.write("夏至", font=("微软雅黑", b, "normal"))
turtle.penup()
turtle.goto(x+r+a,y+r)
turtle.pendown()
turtle.write("秋分", font=("微软雅黑", b, "normal"))



turtle.hideturtle()
turtle.mainloop();
