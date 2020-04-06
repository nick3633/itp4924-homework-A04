from flask import Flask, render_template, flash, redirect
from config import Config
from forms import AdminLoginForm

app = Flask(__name__)

app.config.from_object(Config)


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


if __name__ == '__main__':
    app.run()
