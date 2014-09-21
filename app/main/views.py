from flask import render_template, session, url_for, redirect
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from datetime import datetime

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['Known'] = False
        else:
            session['Known'] = True

        session['Name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, known=session.get('Known', False), name=session.get('Name'), current_time=datetime.utcnow())
