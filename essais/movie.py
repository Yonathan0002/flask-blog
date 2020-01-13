
def durationToString(minutes: int) -> str: 
    """ 
Convertit une durée exprimée en minutes en une chaîne de caractères ayant la forme HH:MM
Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
@param minutes durée en minutes
@return résultat
    """
    return f"{minutes//60:02d}:{minutes%60:02d}"

def ratingToStars(rating: int, max: int) -> str: 
    """
Convertit une note entière comprise entre 0 et $max en une chaîne de caractères composée d'étoiles.
@param rating note comprise entre 0 et $max
@param max valeur maximale de la note*
@return chaîne de caractères composée d'étoiles
    """
    if max < rating:
        raise ValueError("rating est superieur a max")
    retour = ""

    for i in range(0, rating):
        retour += "\u2605"

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
        self.title = title
        self.duration = duration
        if rating < 0 or rating > 10:
            raise ValueError("rating doit etre entre 0 et 10")
        self.rating = rating
        
    def getTitle(self: object) -> str:
        """
        Retourne le titre du film.
        @returntitre du film
        """
        return self.title

    def getduration()