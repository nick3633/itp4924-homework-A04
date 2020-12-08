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
    return render_template('app_learn/learn.html', title='Learn', learn_tutor_block=learn_tutor_block_load)
    
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