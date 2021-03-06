from flask import render_template, session, url_for, redirect, abort
from . import main
from .. import db
from ..models import User
from datetime import datetime


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)