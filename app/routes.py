from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Abolade'}
    posts = [
        {
            'author': {'username': 'Bola'},
            'body': 'Beautiful day in Minneapolis'
        },
        {
            'author': {'username': 'Baba'},
            'body': 'Drama series Suits is super cool'
        }
    ]
    return render_template('index.html', user=user, posts=posts)