import turtle as tt

tt.penup()
tt.goto(-200, -200)
tt.pendown()

row = 5
col = 5

while (row > 0):
    tt.forward(500)
    tt.right(180)
    tt.forward(500)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    row -= 1

tt.forward(500)
tt.right(180)
tt.forward(400)
tt.left(90)

while (col > 1):
    tt.forward(500)
    tt.right(180)
    tt.forward(500)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    col -= 1

tt.forward(500)

tt.exitonclick()
