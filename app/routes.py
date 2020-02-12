from flask import render_template
from app import app
from app.models import User
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user,login_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():    
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

    return render_template('index.html', title='Accueil', posts=posts)

@app.route('/apropos')
def apropos():
    return render_template('apropos.html',title='yoyo')

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Enregistrement', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form= LoginForm()
#     if form.validate_on_submit():
#         flash(f"Enregistrement demandé pour l’utilisateur {form.username.data} (Remember is {form.remember_me.data})")
#         return redirect('/index')
#     return render_template('login.html', title='Enregistrement', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Utilisateur ou mot de passe non valide.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Enregistrement', form=form)

from flask_login import current_user, login_user, logout_user
@app.route('/logout')
def logout() -> str:
    logout_user()
    return redirect(url_for('index'))