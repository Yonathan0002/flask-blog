from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import User, Post
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from flask_login import current_user,login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():    
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Votre message est maintenant en ligne !")
        return redirect(url_for('index'))
    posts = current_user.post_abonnes().all()
    return render_template('index.html', title='Accueil', form=form, posts=posts)

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

@app.route('/register', methods=['GET', 'POST'])
def register() -> str:
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bravo ! Vous devenez un nouvel utilisateur !')
        return redirect(url_for('login'))
    return render_template('register.html', title="S'enregistrer", form=form)

@app.route('/user/<username>')
@login_required
def user(username: str) -> str:
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        { 'author' : user, 'body': 'Test post #1' },
        { 'author' : user, 'body': 'Test post #2' }
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile() -> str:
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Vos modification ont été enregistrées.')
        return redirect(url_for('edit_profile'))
    elif request.method== 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@app.route('/abonner/<username>')
@login_required
def abonner(username : str) -> str:
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(f"L'utilisateur {username} n'a pas été trouvé.")
        return redirect(url_for('index'))
    if user == current_user:
        flash('Vous ne pouvez pas vous abonner à vous-même.')
        return redirect(url_for('index'))
    current_user.abonner(user)
    db.session.commit()
    flash(f"Vous êtes maintenant abonné aux messages de {username}.")
    return redirect(url_for('user', username=username))

@app.route('/desabonner/<username>')
@login_required
def desabonner(username: str) -> str:
    user =User.query.filter_by(username=username).first()
    if user is None:
        flash(f"L'utilisateur {username} n'a pas été trouvé.")
        return redirect(url_for('index'))
    if user == current_user:
        flash("Vous ne pouvez pas vous désabonner de vous-même.")
        return redirect(url_for('user'))
    current_user.desabonner(user)
    db.session.commit()
    flash(f"Vous êtes maintenant désabonner des messages de {username}.")
    return redirect(url_for('user', username=username))
    
