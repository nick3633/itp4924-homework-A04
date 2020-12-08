from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app

@app.route('/learn', methods=['GET', 'POST'])
def learn():
    return render_template('app_learn/learn.html', title='Learn',)