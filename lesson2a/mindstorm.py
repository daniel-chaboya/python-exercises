import turtle

window = turtle.Screen()
window.bgcolor("#2ecc71")

def draw_square(a_turtle):
    
    for i in range(4):
        a_turtle.forward(100)
        a_turtle.right(90)
        
def draw_triangle(a_turtle):
    
    for i in range(3):
        a_turtle.forward(100)
        a_turtle.right(120)
    
def draw_art():
    
    #create a square turtle
    square = turtle.Turtle()
    square.color("#9b59b" + "9")
    square.speed(10)
    #draw a circle from squares
    for i in range(1, 37):
        draw_square(square)
        #reposition by 10 degrees for start of next square 
        square.right(10)
    
    #create the triangle turtle
    triangle = turtle.Turtle()
    triangle.color("#e74c3c")
    draw_triangle(triangle)

    #create a circle turtle
    circle = turtle.Turtle()
    circle.color("#f1c40f")
    circle.circle(50)

    window.exitonclick()
    
draw_art()
