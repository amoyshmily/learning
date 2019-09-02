from . import home
from flask import render_template, url_for, redirect


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/login')
def login():
    render_template('home/login.html')


@home.route("/logout")
def logout():
    redirect(url_for('home.login'))


@home.route("/regist")
def regist():
    pass


@home.route("/user")
def user():
    pass


@home.route("/search")
def search():
    pass
