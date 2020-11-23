from turtleLib import Turtle

x = Turtle()
nLati = (int) (input("Inserire il numero di lati: "))
x.color('blue', 'green')
x.begin_fill()
while True:
    x.forward(60)
    x.left(360/nLati)
    if abs(x.pos()) < 1:
        break
x.end_fill()
x.done()