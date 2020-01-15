from movie import durationToString
from movie import ratingToStars
from movie import Movie



print(durationToString(512))
print(durationToString(4096))
print(durationToString(32768))


print(ratingToStars(0,8))
print(ratingToStars(2,8))
print(ratingToStars(4,8))
print(ratingToStars(8,8))

m1 = Movie('Les évadés')

print(vars(m1))
print(dir(m1))

try:
    m2: Movie = Movie('Les évadés', 122, 5.5)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')

try:
    m2 = Movie('Les évadés', 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\"a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

try:
    m2 = Movie('Les évadés', 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\"a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")


m2: Movie = Movie('Les évadés', 122, 5.5)
print(m2.getTitle() ,m2.getDuration(),m2.getRating())

try:
    m2.setRating(22.2)
except ValueError as e:
    print(f"L’exception \"{e}\"a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

try:
    m2.setRating(-22.2)
except ValueError as e:
    print(f"L’exception \"{e}\"a bien été lancée.") 
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

try:
    m2.setRating(6.2)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')

m3 = Movie('Les évadés', 122, 9.0)
print(m3)