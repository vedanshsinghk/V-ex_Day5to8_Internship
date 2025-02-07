import turtle
import turtle 
 
turtle.color('purple') 
style = ('Courier', 90, 'normal') 
turtle.write('VEDANSH', font=style, align='center') 
turtle.hideturtle()

# Create a turtle for drawing letters
t = turtle.Turtle()
t.speed(3)
t.pencolor('blue')  # Changed color to blue
t.pensize(5)
t.penup()

# Start position for the text
start_x = -300
start_y = 0

# Draw 'V'
t.goto(start_x, start_y)
t.pendown()
t.left(30)
t.forward(50)
t.backward(50)
t.right(60)
t.forward(50)
t.backward(50)
t.left(30)
t.penup()

# Move to position for 'E'
t.goto(start_x + 60, start_y)
t.pendown()
t.forward(40)
t.backward(40)
t.right(90)
t.forward(25)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(25)
t.left(90)
t.forward(40)
t.penup()

# Move to position for 'D'
t.goto(start_x + 130, start_y)
t.pendown()
t.forward(30)
t.right(90)
t.circle(-25, 180)
t.right(90)
t.penup()

# Move to position for 'A'
t.goto(start_x + 200, start_y)
t.pendown()
t.left(75)
t.forward(50)
t.right(150)
t.forward(50)
t.backward(25)
t.right(105)
t.forward(20)
t.backward(20)
t.left(105)
t.backward(25)
t.left(75)
t.penup()

# Move to position for 'N'
t.goto(start_x + 270, start_y)
t.pendown()
t.forward(50)
t.right(150)
t.forward(55)
t.left(150)
t.forward(50)
t.penup()

# Move to position for 'S'
t.goto(start_x + 350, start_y)
t.pendown()
t.forward(30)
t.backward(30)
t.right(90)
t.forward(25)
t.left(90)
t.forward(30)
t.right(90)
t.forward(25)
t.right(90)
t.forward(30)
t.penup()

# Move to position for 'H'
t.goto(start_x + 420, start_y)
t.pendown()
t.forward(50)
t.backward(25)
t.right(90)
t.forward(30)
t.left(90)
t.forward(25)
t.backward(50)
t.penup()

# Hide the turtle and complete the drawing
t.hideturtle()
turtle.done()