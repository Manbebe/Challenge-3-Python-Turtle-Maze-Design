import turtle
t = turtle.Turtle()
t.speed(0) #1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.pencolor("indigo")
t.fillcolor("black")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.right(90)
t.forward(75)
t.left(90)
t.forward(40)
t.left(90)
t.forward(125)
t.left(90)
t.forward(65)
t.right(90)
t.forward(89)
t.right(90)	
t.forward(43)
t.right(90)
t.forward(64)
t.left(90)
t.forward(75)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(40)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(250)
t.left(90)
t.forward(250)
t.left(90)
t.forward(90)
t.right(90)
t.forward(100)
t.right(90)
t.forward(40)
t.left(90)
t.forward(50)
t.right(90)
t.forward(40)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(80)
t.left(90)
t.forward(200)
t.left(90)
t.forward(120)
t.right(90)
t.forward(70)
t.left(90)
t.forward(150)
t.left(90)
t.forward(40)
t.left(90)
t.forward(110)
t.right(90)
t.forward(80)
t.left(90)
t.forward(120)
t.right(90)
t.forward(100)
t.right(90)
t.forward(40)
t.right(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.right(90)
t.forward(75)
t.right(90)
t.forward(85)
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.right(90)
t.forward(90)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.pencolor("white")
t.forward(30)
t.pencolor("indigo")
t.left(90)
t.forward(80)
t.left(90)
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.forward(10)
t.left(90)
t.forward(55)
t.right(90)
t.forward(80)
t.left(90)
t.forward(100)
t.right(90)
t.forward(105)
t.right(90)
t.forward(85)
t.right(90)
t.forward(85)
t.pencolor("red")
t.penup()
t.setpos(150,65)
t.speed(3) 
t.left(90)
t.pendown()
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(225)
t.left(90)
t.forward(80)
t.right(90)
t.forward(75)
t.left(90)
t.forward(230)
t.left(90)
t.forward(110)
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.right(90)
t.forward(90)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.shape(name="turtle")
t.setpos(0,0)


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'teal', 'purple', 'black']


for i in range(5000):
  t.forward(i)
  t.color(colors[i % len(colors)])
  t.left(500)
