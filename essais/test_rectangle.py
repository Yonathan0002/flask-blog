from rectangle import Rectangle

r = Rectangle(30, 10, '*')
print("Instanciation avec initialisation :", vars(r))

r.draw()

print(r.getPerimeter(), r.getSurface())
