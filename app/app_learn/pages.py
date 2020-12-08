from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app

from app.app_learn.models import *
from app.app_learn.forms import *

@app.route('/learn', methods=['GET', 'POST'])
def learn():
    learn_tutor_block_load = learn_tutor_block.query
    learn_material_block_load = learn_material_block.query
    learn_res_block_load = learn_res_block.query
    return render_template(
        'app_learn/learn.html', title='Learn',
        learn_tutor_block=learn_tutor_block_load,
        learn_material_block=learn_material_block_load,
        learn_res_block=learn_res_block_load
    )
    
@app.route('/learn/tutor_block/add', methods=['GET', 'POST'])
def learn_tutor_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_learn_tutor_block_add = learn_tutor_block_add()
    if form_learn_tutor_block_add.validate_on_submit():
        tutor_add = learn_tutor_block(
            title = form_learn_tutor_block_add.title.data,
            content = form_learn_tutor_block_add.content.data,
            link = form_learn_tutor_block_add.link.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(tutor_add)
        db.session.commit()
        flash('content added on tutor block in learn.html')
        return redirect(url_for('learn'))
    return render_template('app_learn/learn_tutor_block_add.html', form_learn_tutor_block_add=form_learn_tutor_block_add)

@app.route('/learn/tutor_block/edit/<id>', methods=['GET', 'POST'])
def learn_tutor_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_learn_tutor_block_edit = learn_tutor_block_edit()

    if form_learn_tutor_block_edit.validate_on_submit():
        if form_learn_tutor_block_edit.editype.data == 'edit':
            tutor_edit = learn_tutor_block.query.filter_by(id=id).first()
            tutor_edit.title = form_learn_tutor_block_edit.title.data
            tutor_edit.content = form_learn_tutor_block_edit.content.data
            tutor_edit.link = form_learn_tutor_block_edit.link.data
            tutor_edit.edited_time = datetime.utcnow()
            tutor_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on tutor block in learn.html')
        elif form_learn_tutor_block_edit.editype.data == 'delete':
            learn_tutor_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on tutor block in learn.html')
        return redirect(url_for('learn'))
    elif request.method == 'GET':
        get_value = learn_tutor_block.query.filter_by(id=id).first()
        form_learn_tutor_block_edit.title.data = get_value.title
        form_learn_tutor_block_edit.content.data = get_value.content
        form_learn_tutor_block_edit.link.data = get_value.link

    return render_template('app_learn/learn_tutor_block_edit.html', title='Editing block tutor in learn.html',
                           form_learn_tutor_block_edit=form_learn_tutor_block_edit, id=id)
                           
                           
@app.route('/learn/material_block/add', methods=['GET', 'POST'])
def learn_material_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_learn_material_block_add = learn_material_block_add()
    if form_learn_material_block_add.validate_on_submit():
        material_add = learn_material_block(
            title = form_learn_material_block_add.title.data,
            link = form_learn_material_block_add.link.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(material_add)
        db.session.commit()
        flash('content added on material block in learn.html')
        return redirect(url_for('learn'))
    return render_template('app_learn/learn_material_block_add.html', form_learn_material_block_add=form_learn_material_block_add)

@app.route('/learn/material_block/edit/<id>', methods=['GET', 'POST'])
def learn_material_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_learn_material_block_edit = learn_material_block_edit()

    if form_learn_material_block_edit.validate_on_submit():
        if form_learn_material_block_edit.editype.data == 'edit':
            material_edit = learn_material_block.query.filter_by(id=id).first()
            material_edit.title = form_learn_material_block_edit.title.data
            material_edit.link = form_learn_material_block_edit.link.data
            material_edit.edited_time = datetime.utcnow()
            material_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on material block in learn.html')
        elif form_learn_material_block_edit.editype.data == 'delete':
            learn_material_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on material block in learn.html')
        return redirect(url_for('learn'))
    elif request.method == 'GET':
        get_value = learn_material_block.query.filter_by(id=id).first()
        form_learn_material_block_edit.title.data = get_value.title
        form_learn_material_block_edit.link.data = get_value.link

    return render_template('app_learn/learn_material_block_edit.html', title='Editing block material in learn.html',
                           form_learn_material_block_edit=form_learn_material_block_edit, id=id)
                           
                           
@app.route('/learn/res_block/add', methods=['GET', 'POST'])
def learn_res_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_learn_res_block_add = learn_res_block_add()
    if form_learn_res_block_add.validate_on_submit():
        res_add = learn_res_block(
            title = form_learn_res_block_add.title.data,
            image = form_learn_res_block_add.image.data,
            content = form_learn_res_block_add.content.data,
            link = form_learn_res_block_add.link.data,
            link_text = form_learn_res_block_add.link_text.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(res_add)
        db.session.commit()
        flash('content added on res block in learn.html')
        return redirect(url_for('learn'))
    return render_template('app_learn/learn_res_block_add.html', form_learn_res_block_add=form_learn_res_block_add)

@app.route('/learn/res_block/edit/<id>', methods=['GET', 'POST'])
def learn_res_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_learn_res_block_edit = learn_res_block_edit()

    if form_learn_res_block_edit.validate_on_submit():
        if form_learn_res_block_edit.editype.data == 'edit':
            res_edit = learn_res_block.query.filter_by(id=id).first()
            res_edit.title = form_learn_res_block_edit.title.data
            res_edit.image = form_learn_res_block_edit.image.data
            res_edit.content = form_learn_res_block_edit.content.data
            res_edit.link = form_learn_res_block_edit.link.data
            res_edit.link_text = form_learn_res_block_edit.link_text.data
            res_edit.edited_time = datetime.utcnow()
            res_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on res block in learn.html')
        elif form_learn_res_block_edit.editype.data == 'delete':
            learn_res_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on res block in learn.html')
        return redirect(url_for('learn'))
    elif request.method == 'GET':
        get_value = learn_res_block.query.filter_by(id=id).first()
        form_learn_res_block_edit.title.data = get_value.title
        form_learn_res_block_edit.image.data = get_value.image
        form_learn_res_block_edit.content.data = get_value.content
        form_learn_res_block_edit.link.data = get_value.link
        form_learn_res_block_edit.link_text.data = get_value.link_text

    return render_template('app_learn/learn_res_block_edit.html', title='Editing block res in learn.html',
                           form_learn_res_block_edit=form_learn_res_block_edit, id=id)
