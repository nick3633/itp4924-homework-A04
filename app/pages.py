from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from flask import render_template, url_for
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

from app.admin.pages import *
from app.app_about.pages import *
from app.app_architecture.pages import *
from app.app_home.pages import *
from app.app_learn.pages import *
from app.app_comm.pages import *