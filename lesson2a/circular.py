import turtle

window = turtle.Screen()
window.bgcolor("#2ecc71")

        
def draw_triangle(a_turtle):
    
    for i in range(1):
        a_turtle.forward(120)
        a_turtle.right(110)
        a_turtle.forward(40)

    a_turtle.right(90)
    a_turtle.forward(120)
        
def draw_flower():
    
    small_turtle = turtle.Turtle()
    small_turtle.color("black")
    small_turtle.speed(15)

    #create flower
    small_turtle.right(135)
    
    for i in range(1, 37):
        draw_triangle(small_turtle)
        small_turtle.right(15)
        
    small_turtle.right(135)
    small_turtle.forward(250)


    window.exitonclick()
    
draw_flower()
