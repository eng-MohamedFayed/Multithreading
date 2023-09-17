# Mulrithreading
*** This small project is to demonstrate the multithreading concept using a python script ***
![Multithreading image](https://www.ionos.com/digitalguide/fileadmin/_processed_/6/5/csm_nvme-t_f085d58d46.webp)

<div>

  Multithreading allows a program to execute multiple tasks concurrently within a single process. This enables better performance and responsiveness, especially on multi-core processors. It's crucial for handling tasks involving a mix of computation and I/O operations. However, it introduces challenges like synchronization and 
thread safety, which need to be carefully managed. Mastering multithreading is essential for developing high-performance applications.

</div>

```python
import turtle
from multiprocessing import Process
```

<div>
  
  ### Turtle library
  The Turtle library in Python provides a simple graphics module for creating drawings and animations. It's beginner-friendly and allows users to control a turtle that moves on a drawing canvas, making it a popular choice for introductory programming exercises related to graphics.
  ### Process class from Multiprocessing
  The multiprocessing module in Python allows you to create and manage separate processes, enabling true parallelism. The Process class is used to initiate new processes. You can start a process with start(), wait for it to finish with join(), and terminate it with terminate().

</div>

```python
def draw_circle():
    t = turtle.Turtle()
    t.shape("circle")
    t.color("red")
    # draw the circle with a radius of 50
    t.circle(50)
    # exit the turtle graphics window
    turtle.done()
```

- turtle.Turtle(): Creates a new Turtle object, which is used for drawing.
- t.shape("circle"): Sets the shape of the turtle to a circle, indicating how it will appear on the screen.
- t.color("red"): Sets the color of the turtle's pen to red. This means that the subsequent drawing will be in red.
- t.circle(50): Draws a circle with a radius of 50 units.
- turtle.done(): Closes the turtle graphics window after the drawing is complete.


