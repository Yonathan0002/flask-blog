class Shape:

    def draw(self: object) -> None:
        pass

    # Préparation de la propriété "perimeter"
    def _getPerimeter(self: object) -> float:
        pass

    @property 
    def perimeter(self: object) -> float:
        return self._getPerimeter()

    # Préparation de la propriété "surface"
    def _getSurface(self: object) -> float:
        pass

    @property
    def surface(self: object) -> float:
        return self._getSurface()

    def _getPen(self: object) -> str:
        return self._pen
    
    @property
    def pen(self: object) -> str:
        return self._getPen()

    def __init__(self: object, pen: str) -> None:
        self._pen = pen
    
    