from turtle import *

# settings
width(6)
speed(10)
# shape(turtle)

# set_bg_color
color("green")
penup()
goto(-500, 400)
pendown()
begin_fill()
forward(970)
right(90)
forward(800)
right(90)
forward(970)
right(90)
forward(800)
end_fill()
# tp
penup()
goto(0, 0)
pendown()

# buildHouse

# square
color("lightgray")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

# door
left(180)
forward(120)
color("brown")
begin_fill()
right(90)
forward(80)
left(90)
forward(40)
left(90)
forward(80)
left(90)
forward(40)
end_fill()

# roof_triangle
# tp
penup()
goto(0, 200)
pendown()
# buildTriangle
color("red")
begin_fill()
left(130)
forward(150)
left(95)
forward(160)
left(135)
forward(210)
end_fill()

# windows
# tp
penup()
goto(-70, 40)
pendown()
# buildWindow
color("white")
begin_fill()
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
# buildWindow2
# tp
penup()
goto(-120, 140)
pendown()
# buildWindow2
begin_fill()
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

# floorLine
# tp
penup()
goto(0, 110)
pendown()
# buildLine
color("gray")
right(90)
forward(200)

exitonclick()