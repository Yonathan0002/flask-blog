from triangle import Triangle

t = Triangle(4,"*")
t2 = Triangle(3, "#")

t2.draw()
t.draw()


print(t.getPerimeter(), t.getSurface())
