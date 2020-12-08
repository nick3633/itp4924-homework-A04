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


@app.route('/comm', methods=['GET', 'POST'])
def comm():
    comm_method_block_load = comm_method_block.query
    return render_template(
        'app_comm/comm.html',
        title='Community',
        comm_method_block=comm_method_block_load
    )
    
    
@app.route('/comm/method_block/add', methods=['GET', 'POST'])
def comm_method_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_comm_method_block_add = comm_method_block_add()

    if form_comm_method_block_add.validate_on_submit():
        method_add = comm_method_block(
            title=form_comm_method_block_add.title.data,
            image=form_comm_method_block_add.image.data,
            content=form_comm_method_block_add.content.data,
            link=form_comm_method_block_add.link.data,
            link_text=form_comm_method_block_add.link_text.data,
            editor_user_id=current_user.user_id
        )
        db.session.add(method_add)
        db.session.commit()
        flash('content added on method block in comm.html')
        return redirect(url_for('comm'))

    return render_template('app_comm/comm_method_block_add.html', form_comm_method_block_add=form_comm_method_block_add)


@app.route('/comm/method_block/edit/<id>', methods=['GET', 'POST'])
def comm_method_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_comm_method_block_edit = comm_method_block_edit()

    if form_comm_method_block_edit.validate_on_submit():
        if form_comm_method_block_edit.editype.data == 'edit':
            method_edit = comm_method_block.query.filter_by(id=id).first()
            method_edit.title = form_comm_method_block_edit.title.data
            method_edit.image = form_comm_method_block_edit.image.data
            method_edit.content = form_comm_method_block_edit.content.data
            method_edit.link = form_comm_method_block_edit.link.data
            method_edit.link_text = form_comm_method_block_edit.link_text.data
            method_edit.editor_user_id = current_user.user_id
            method_edit.edited_time = datetime.utcnow()

            db.session.commit()
            flash('edited content id: ' + id + ' on method block in comm.html')
        elif form_comm_method_block_edit.editype.data == 'delete':
            comm_method_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on method block in comm.html')
        return redirect(url_for('comm'))
    elif request.method == 'GET':
        get_value = comm_method_block.query.filter_by(id=id).first()
        form_comm_method_block_edit.title.data = get_value.title
        form_comm_method_block_edit.image.data = get_value.image
        form_comm_method_block_edit.content.data = get_value.content
        form_comm_method_block_edit.link.data = get_value.link
        form_comm_method_block_edit.link_text.data = get_value.link_text

    return render_template('app_comm/comm_method_block_edit.html', title='Editing block method in comm.html',
                           form_comm_method_block_edit=form_comm_method_block_edit, id=id)