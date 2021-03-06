from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app
from app.app_home.forms import home_function_block_add, home_function_block_edit, home_about_block_add, \
    home_about_block_edit, home_client_block_add, home_client_block_edit
from app.app_home.models import home_functions_block, home_about_block, home_client_block


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    home_function_block_load = home_functions_block.query
    home_about_block_load = home_about_block.query
    home_client_block_load = home_client_block.query

    return render_template('app_home/home.html', title='',
                           home_function_block=home_function_block_load, home_about_block=home_about_block_load,
                           home_client_block=home_client_block_load)


@app.route('/home/func_block/add', methods=['GET', 'POST'])
def home_func_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_home_func_block_add = home_function_block_add()

    if form_home_func_block_add.validate_on_submit():
        func_add = home_functions_block(
            title=form_home_func_block_add.title.data,
            icon=form_home_func_block_add.icon.data,
            content=form_home_func_block_add.content.data,
            editor_user_id=current_user.user_id
        )
        db.session.add(func_add)
        db.session.commit()
        flash('content added on functions block in home.html')
        return redirect(url_for('home'))

    return render_template('app_home/home_function_block_add.html', form_home_func_block_add=form_home_func_block_add)


@app.route('/home/function_block/edit/<id>', methods=['GET', 'POST'])
def home_func_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_home_func_block_edit = home_function_block_edit()

    if form_home_func_block_edit.validate_on_submit():
        if form_home_func_block_edit.editype.data == 'edit':
            func_edit = home_functions_block.query.filter_by(id=id).first()
            func_edit.title = form_home_func_block_edit.title.data
            func_edit.icon = form_home_func_block_edit.icon.data
            func_edit.content = form_home_func_block_edit.content.data
            func_edit.editor_user_id = current_user.user_id
            func_edit.edited_time = datetime.utcnow()

            db.session.commit()
            flash('edited content id: ' + id + ' on functions block in home.html')
        elif form_home_func_block_edit.editype.data == 'delete':
            home_functions_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on functions block in home.html')
            # https://stackoverflow.com/questions/27158573/how-to-delete-a-record-by-id-in-flask-sqlalchemy (4/9/2020 4:x9PM)
        return redirect(url_for('home'))
    elif request.method == 'GET':
        get_value = home_functions_block.query.filter_by(id=id).first()
        form_home_func_block_edit.title.data = get_value.title
        form_home_func_block_edit.icon.data = get_value.icon
        form_home_func_block_edit.content.data = get_value.content

    return render_template('app_home/home_function_block_edit.html', title='Editing block Functions in home.html',
                           form_home_func_block_edit=form_home_func_block_edit, id=id)


@app.route('/home/about_block/add', methods=['GET', 'POST'])
def home_about_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_home_about_block_add = home_about_block_add()

    if form_home_about_block_add.validate_on_submit():
        about_add = home_about_block(
            title=form_home_about_block_add.title.data,
            image=form_home_about_block_add.image.data,
            content=form_home_about_block_add.content.data,
            link=form_home_about_block_add.link.data,
            link_text=form_home_about_block_add.link_text.data,
            editor_user_id=current_user.user_id
        )
        db.session.add(about_add)
        db.session.commit()
        flash('content added on about block in home.html')
        return redirect(url_for('home'))

    return render_template('app_home/home_about_block_add.html', form_home_about_block_add=form_home_about_block_add)


@app.route('/home/about_block/edit/<id>', methods=['GET', 'POST'])
def home_about_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_home_about_block_edit = home_about_block_edit()

    if form_home_about_block_edit.validate_on_submit():
        if form_home_about_block_edit.editype.data == 'edit':
            about_edit = home_about_block.query.filter_by(id=id).first()
            about_edit.title = form_home_about_block_edit.title.data
            about_edit.image = form_home_about_block_edit.image.data
            about_edit.content = form_home_about_block_edit.content.data
            about_edit.link = form_home_about_block_edit.link.data
            about_edit.link_text = form_home_about_block_edit.link_text.data
            about_edit.editor_user_id = current_user.user_id
            about_edit.edited_time = datetime.utcnow()

            db.session.commit()
            flash('edited content id: ' + id + ' on about block in home.html')
        elif form_home_about_block_edit.editype.data == 'delete':
            home_about_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on about block in home.html')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        get_value = home_about_block.query.filter_by(id=id).first()
        form_home_about_block_edit.title.data = get_value.title
        form_home_about_block_edit.image.data = get_value.image
        form_home_about_block_edit.content.data = get_value.content
        form_home_about_block_edit.link.data = get_value.link
        form_home_about_block_edit.link_text.data = get_value.link_text

    return render_template('app_home/home_about_block_edit.html', title='Editing block About in home.html',
                           form_home_about_block_edit=form_home_about_block_edit, id=id)


@app.route('/home/client_block/add', methods=['GET', 'POST'])
def home_client_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_home_client_block_add = home_client_block_add()
    if form_home_client_block_add.validate_on_submit():
        client_add = home_client_block(
            client_logo=form_home_client_block_add.client_logo.data,
            editor_user_id=current_user.user_id
        )
        db.session.add(client_add)
        db.session.commit()
        flash('content added on client block in home.html')
        return redirect(url_for('home'))

    return render_template('app_home/home_client_block_add.html', form_home_client_block_add=form_home_client_block_add)


@app.route('/home/client_block/edit/<id>', methods=['GET', 'POST'])
def home_client_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_home_client_block_edit = home_client_block_edit()

    if form_home_client_block_edit.validate_on_submit():
        if form_home_client_block_edit.editype.data == 'edit':
            client_edit = home_client_block.query.filter_by(id=id).first()
            client_edit.client_logo = form_home_client_block_edit.client_logo.data
            client_edit.editor_user_id = current_user.user_id
            client_edit.edited_time = datetime.utcnow()

            db.session.commit()
            flash('edited content id: ' + id + ' on client block in home.html')
        elif form_home_client_block_edit.editype.data == 'delete':
            home_client_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on client block in home.html')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        get_value = home_client_block.query.filter_by(id=id).first()
        form_home_client_block_edit.client_logo.data = get_value.client_logo

    return render_template('app_home/home_client_block_edit.html', title='Editing block Client in home.html',
                           form_home_client_block_edit=form_home_client_block_edit, id=id)