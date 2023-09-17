import turtle
from multiprocessing import Process

# this function is for drawing a circle
def draw_circle():
    t = turtle.Turtle()
    t.shape("circle")
    t.color("red")
    # draw the circle with a radius of 50
    t.circle(50)
    # exit the turtle graphics window
    turtle.done()



def draw_rectangle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    #the rectangle with a length of 100 and width of 50
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    # exit the turtle graphics window
    turtle.done()


if __name__ == "__main__":

    #to see the full drawing you will find that both screens are above each other so move one of them aside
    circle_process = Process(target=draw_circle)
    rectangle_process = Process(target=draw_rectangle)
    circle_process.start()
    rectangle_process.start()
    circle_process.join()
    rectangle_process.join()
