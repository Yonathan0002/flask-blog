
def durationToString(minutes: int) -> str: 
    """ 
Convertit une durée exprimée en minutes en une chaîne de caractères ayant la forme HH:MM
Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
@param $minutes durée en minutes
@return résultat
    """
    return f"{minutes//60:02d}:{minutes%60:02d}"