import pathlib
import uuid

from flask import render_template, request, redirect, url_for, session, flash, make_response
from marshmallow import ValidationError

from . import app
from .repository import users


@app.route('/healthcheck', strict_slashes=False)
def healthcheck():
    return 'I am working'


@app.route('/', strict_slashes=False)
def index():
    auth = True if 'username' in session else False
    return render_template('pages/index.html', title='Cloud Pictures!', auth=auth)


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    auth = True if 'username' in session else False
    if auth:
        return redirect(url_for('index'))

    if request.method == 'POST':
        # try:
        #     RegistrationSchema().load(request.form)
        # except ValidationError as err:
        #     return render_template('pages/registration.html', messages=err.messages)
        email = request.form.get('email')
        password = request.form.get('password')
        nick = request.form.get('nick')
        user = users.create_user(email, password, nick)
        print(user)
        return redirect(url_for('login'))

    return render_template('pages/registration.html')
