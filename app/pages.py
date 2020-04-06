from flask import render_template, flash, redirect
from app import app
from app.forms import AdminLoginForm


@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html', title='')


@app.route('/admin_login.html', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('login')
        return redirect('/home.html')
    return render_template('admin_login.html', title='Admin Login - ', form=form)
