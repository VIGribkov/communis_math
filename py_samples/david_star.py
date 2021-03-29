import turtle


def david(n, m, fwd):
    for step in range(n):
        turtle.begin_fill()
        for _ in range(m):
            turtle.forward(fwd)
            turtle.left(360 // m)
        turtle.end_fill()

        turtle.forward(fwd)
        turtle.right(360 // n)


#turtle.shape('turtle')
turtle.shape('classic')
turtle.color('green', 'blue')
turtle.shapesize(2)
turtle.speed(2)

david(5, 3, 70)
