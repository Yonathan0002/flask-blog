from flask import Flask

#creation de l'application
app= Flask( __name__ ) 

# On importe le fichier contenant 
# # la définitiondes fonctions de vue
from app import routes

