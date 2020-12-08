from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app
from app.admin.forms import AdminLoginForm, AddAdminForm
from app.admin.models import Admin


@app.route('/admin_home')
def admin_home():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    admin_list = Admin.query
    return render_template('admin/admin_home.html', title='Admin Home - ', admin_list=admin_list)


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(user_id=form.user_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('User ID or password is not correct')
            return render_template('admin/admin_login.html', title='Admin Login - ', form=form)
        login_user(user, remember=form.keep_login_status.data)
        # https://stackoverflow.com/questions/37472870/login-user-fails-to-get-user-id (4/7/2020 1:15AM)
        return redirect(url_for('admin_home'))
    return render_template('admin/admin_login.html', title='Admin Login - ', form=form)


@app.route('/admin_logout')
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))


@app.route('/add_admin', methods=['GET', 'POST'])
def add_admin():
    form = AddAdminForm()
    if form.validate_on_submit():
        check_user = Admin.query.filter_by(user_id=form.user_id.data).first()
        check_email = Admin.query.filter_by(email=form.email.data).first()
        if check_user is not None:
            flash('This user ID already used.')
            return render_template('admin/add_admin.html', title='Add Admin - ', form=form)
        if check_email is not None:
            flash('This Email already used.')
            return render_template('admin/add_admin.html', title='Add Admin - ', form=form)
        if form.verification_key.data != 'O8afSh2OHdqyKvJyzeS4XKXQ':
            flash('The verification key is not correct.')
            return render_template('admin/add_admin.html', title='Add Admin - ', form=form)
        user = Admin(user_id=form.user_id.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Added a new admin.')
        return redirect(url_for('admin_home'))
    return render_template('admin/add_admin.html', title='Add Admin - ', form=form)