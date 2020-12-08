from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app

from app.app_comm.models import *
from app.app_comm.forms import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/comm', methods=['GET', 'POST'])
def comm():

    return render_template('app_comm/comm.html', title='Community')