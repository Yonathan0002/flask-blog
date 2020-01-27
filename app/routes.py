from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Philippe' }
    #return render_template('index.html', user=user)

    posts = [
        {
            'author': {'username' : 'John'},
            'body' : "coucou"
        },
        {
            'author': {'username': 'suzan'},
            'body': "salut"
        }
    ]

    return render_template('index.html', title='Accueil',user=user,posts=posts)