
from math import *

def durationToString(minutes: int) -> str: 
    """ 
Convertit une durée exprimée en minutes en une chaîne de caractères ayant la forme HH:MM
Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
@param minutes durée en minutes
@return résultat
    """
    return f"{minutes//60:02d}:{minutes%60:02d}"

def ratingToStars(rating: float, max: int) -> str: 
    """
Convertit une note entière comprise entre 0 et $max en une chaîne de caractères composée d'étoiles.
@param rating note comprise entre 0 et $max
@param max valeur maximale de la note*
@return chaîne de caractères composée d'étoiles
    """
    rating = floor(rating)
    if max < rating:
        raise ValueError("rating est superieur a max")
    retour = ""

    for i in range(0, rating):
        retour += '\u2605'

    for i in range(rating, max):
        retour += '\u2606'
    
    return retour

class Movie:
    """
    Classe représentant un film.
    """

    def __init__(self: object, title: str, duration= 0, rating= 0.0) -> None:
        """
    Constructeur.
    @param$title    titre du film
        """
        self._title = title
        self._duration = duration
        self.rating = rating
    
    # Mise en place de la propriété “title”en lecture seule
    def getTitle(self: object) -> str:
        """
        Retourne le titre du film.
        Retour:
            Le titre du film
        """
        return self._title

    @property
    def title(self: object) -> str:
        """
        Retourne le titre du film.
        retour:
            Titre du film
        """
        return self.getTitle()
    
    @property
    def duration(self: object) -> int:
        """
        Retourne la duréedu film(exprimée en minutes).

        Retour:
            Durée du film
        """
        return self.getDuration()
    

    def getDuration(self: object) -> int:
        """
        Retourne le Duration du film.
        @return Duration du film
        """
        return self._duration

    # Mise en place de la proprité “rating”en lecture et écritur
    def getRating(self: object) -> float:
        """
        Retourne le Rating du film.
        @return Rating du film
        """
        return self._rating   

    @property
    def rating(self: object) -> float:
        """
        Retourne la note donnéeau film(comprise entre 0 et 10).

        Retour:
            Notedu film
        """
        return self.getRating()

    @rating.setter
    def rating(self: object, r: float) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10

        Paramètre:
            r: nouvelle note du film (entre 0 et 10)
        """
        self.setRating(r)

    def setRating(self: object,rating: float) -> None:
        """
        Modifie la note du film
        Paramètre:
            rating: nouvelle note du film
        Exception:
            ValueError: si la note n’est pas comprise entre 0 et 10
        """
        if not 0.0 <= rating <= 10.0:
            raise ValueError(f"La note {rating} doit être comprise entre 0 et 10")
        self._rating = rating

    
    rating = property(getRating, setRating)
    title = property(getTitle)
    def __repr__(self: object) -> str:
        return self.title + " (" + durationToString(self.duration) + ") \n" + ratingToStars(self._rating,10)
