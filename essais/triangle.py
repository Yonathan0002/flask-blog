from shape import Shape

class Triangle(Shape):
    
    def __init__(self: object, size: int, pen: str) -> None:
        """
        Constructeur

        Paramètres:
            s: size du triangle
        """
        Shape.__init__(self, pen) # Appel du constructeur de Shape
        self._size = size

    def draw(self: object) -> None:
        for i in range(1, self._size + 1):
            print(self._pen * i)

    def getPerimeter(self: object) -> float:
        return self._size * 2 + (self._size * 2) ** 1/2

    def getSurface(self: object) ->float:
        return self._size ** 2 / 2