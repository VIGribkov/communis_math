import turtle as t


def go_snowy(length):
    if length < 5:
        t.forward(length)
    else:
        go_snowy(length/3)
        t.left(60)
        go_snowy(length/3)
        t.right(120) 
        go_snowy(length/3)
        t.left(60)        
        go_snowy(length/3)


t.color('red', 'yellow')
t.speed(100)
t.begin_fill()
for _ in 0, 1, 2:
    go_snowy(250)
    t.right(120)
t.end_fill()
t.exitonclick()
t.mainloop()
t.done()

