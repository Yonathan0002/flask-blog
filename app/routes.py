from flask import render_template
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Philippe' }
    return render_template('index.html', title='Page principale', user=user)