from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Yonathor' }
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

    return render_template('index.html', title='yoyo', user=user, posts=posts)

@app.route('/apropos')
def apropos():
    return render_template('apropos.html',title='yoyo')

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Enregistrement', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash(f"Enregistrement demandé pour l’utilisateur {form.username.data} (Remember is {form.remember_me.data})")
        return redirect('/index')
    return render_template('login.html', title='Enregistrement', form=form)