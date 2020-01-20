from shape import Shape

class Rectangle(Shape):
    
    def __init__(self: object, width: int, height: int, pen: str) -> None:
        """
        Constructeur

        Paramètres:
            w: largeur du rectangle
            h: hauteur du rectangle
            pen: motif pour remplir le rectangle
        """
        Shape.__init__(self, pen) # Appel du constructeur de Shape
        self._width = width
        self._height = height
    
    def draw(self: object) -> None:
        for i in range(self._height):
            print(self._pen * self._width)
    
    def getPerimeter(self: object) -> float:
        return (self._width + self._height) * 2
    
    def getSurface(self: object) -> float:
        return self._width * self._height
    

