from flask import Blueprint, render_template, redirect, url_for, flash, request, session

from project.admin.models import check_user

admin_index = Blueprint('admin_index', __name__, template_folder='templates')

from project.admin.forms import LoginForm


@admin_index.route('/')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")


@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'user_session' in session:
        return redirect(url_for('admin_index.dashboard'))
        #return "Logged in"

    if form.validate_on_submit():
        user_name = request.form['username']
        password = request.form['password']

        if check_user(user_name, password):
            session['user_session'] = request.form['username']
            return redirect(url_for('admin_index.dashboard'))

    return render_template('login.html', title="Login", form=form)


@admin_index.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_session', None)
    return "<h1> You are Logged Out! </h1>"
