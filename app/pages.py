from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.forms import AdminLoginForm, AddAdminForm
from app.models import Admin, home_functions_block


@app.route('/')
@app.route('/home.html')
def home():
    home_function_block = home_functions_block.query
    return render_template('home.html', title='', home_function_block=home_function_block)


@app.route('/admin_home.html')
def admin_home():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    admin_list = Admin.query
    return render_template('admin_home.html', title='Admin Home - ', admin_list=admin_list)


@app.route('/admin_login.html', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(user_id=form.user_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('User ID or password is not correct')
            return render_template('admin_login.html', title='Admin Login - ', form=form)
        login_user(user, remember=False)
        # https://stackoverflow.com/questions/37472870/login-user-fails-to-get-user-id (4/7/2020 1:15AM)
        return redirect(url_for('admin_home'))
    return render_template('admin_login.html', title='Admin Login - ', form=form)


@app.route('/admin_logout.html')
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))


@app.route('/add_admin.html', methods=['GET', 'POST'])
def add_admin():
    form = AddAdminForm()
    if form.validate_on_submit():
        check_user = Admin.query.filter_by(user_id=form.user_id.data).first()
        check_email = Admin.query.filter_by(email=form.email.data).first()
        if check_user is not None or check_email is not None:
            flash('This user ID or Email already used.')
            return render_template('add_admin.html', title='Add Admin - ', form=form)
        if form.verification_key.data != 'O8afSh2OHdqyKvJyzeS4XKXQ':
            flash('The verification key is not correct.')
            return render_template('add_admin.html', title='Add Admin - ', form=form)
        user = Admin(user_id=form.user_id.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Added a new admin.')
        return redirect(url_for('admin_home'))
    return render_template('add_admin.html', title='Add Admin - ', form=form)
