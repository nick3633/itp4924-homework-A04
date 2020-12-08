from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app
from app.app_architecture.forms import architecture_item_block_add, architecture_item_block_edit, \
    architecture_ebook_block_add, architecture_ebook_block_edit
from app.app_architecture.models import architecture_item_block, architecture_ebook_block


@app.route('/architecture', methods=['GET', 'POST'])
def architecture():
    architecture_item_block_load = architecture_item_block.query
    architecture_ebook_block_load = architecture_ebook_block.query
    return render_template(
        'app_architecture/architecture.html', title='Architecture',
        architecture_item_block=architecture_item_block_load,
        architecture_ebook_block=architecture_ebook_block_load
    )


@app.route('/architecture/item_block/add', methods=['GET', 'POST'])
def architecture_item_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_architecture_item_block_add = architecture_item_block_add()
    if form_architecture_item_block_add.validate_on_submit():
        item_add = architecture_item_block(
            title = form_architecture_item_block_add.title.data,
            content = form_architecture_item_block_add.content.data,
            link = form_architecture_item_block_add.link.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(item_add)
        db.session.commit()
        flash('content added on item block in architecture.html')
        return redirect(url_for('architecture'))
    return render_template('app_architecture/architecture_item_block_add.html', form_architecture_item_block_add=form_architecture_item_block_add)


@app.route('/architecture/item_block/edit/<id>', methods=['GET', 'POST'])
def architecture_item_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_architecture_item_block_edit = architecture_item_block_edit()

    if form_architecture_item_block_edit.validate_on_submit():
        if form_architecture_item_block_edit.editype.data == 'edit':
            item_edit = architecture_item_block.query.filter_by(id=id).first()
            item_edit.title = form_architecture_item_block_edit.title.data
            item_edit.content = form_architecture_item_block_edit.content.data
            item_edit.link = form_architecture_item_block_edit.link.data
            item_edit.edited_time = datetime.utcnow()
            item_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on item block in architecture.html')
        elif form_architecture_item_block_edit.editype.data == 'delete':
            architecture_item_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on item block in architecture.html')
        return redirect(url_for('architecture'))
    elif request.method == 'GET':
        get_value = architecture_item_block.query.filter_by(id=id).first()
        form_architecture_item_block_edit.title.data = get_value.title
        form_architecture_item_block_edit.content.data = get_value.content
        form_architecture_item_block_edit.link.data = get_value.link

    return render_template('app_architecture/architecture_item_block_edit.html', title='Editing block item in architecture.html',
                           form_architecture_item_block_edit=form_architecture_item_block_edit, id=id)


@app.route('/architecture/ebook_block/add', methods=['GET', 'POST'])
def architecture_ebook_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_architecture_ebook_block_add = architecture_ebook_block_add()
    if form_architecture_ebook_block_add.validate_on_submit():
        ebook_add = architecture_ebook_block(
            cover_url = form_architecture_ebook_block_add.cover_url.data,
            link = form_architecture_ebook_block_add.link.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(ebook_add)
        db.session.commit()
        flash('content added on ebook block in architecture.html')
        return redirect(url_for('architecture'))
    return render_template('app_architecture/architecture_ebook_block_add.html', form_architecture_ebook_block_add=form_architecture_ebook_block_add)


@app.route('/architecture/ebook_block/edit/<id>', methods=['GET', 'POST'])
def architecture_ebook_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_architecture_ebook_block_edit = architecture_ebook_block_edit()

    if form_architecture_ebook_block_edit.validate_on_submit():
        if form_architecture_ebook_block_edit.editype.data == 'edit':
            ebook_edit = architecture_ebook_block.query.filter_by(id=id).first()
            ebook_edit.cover_url = form_architecture_ebook_block_edit.cover_url.data
            ebook_edit.link = form_architecture_ebook_block_edit.link.data
            ebook_edit.edited_time = datetime.utcnow()
            ebook_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on ebook block in architecture.html')
        elif form_architecture_ebook_block_edit.editype.data == 'delete':
            architecture_ebook_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on ebook block in architecture.html')
        return redirect(url_for('architecture'))
    elif request.method == 'GET':
        get_value = architecture_ebook_block.query.filter_by(id=id).first()
        form_architecture_ebook_block_edit.cover_url.data = get_value.cover_url
        form_architecture_ebook_block_edit.link.data = get_value.link

    return render_template('app_architecture/architecture_ebook_block_edit.html', title='Editing block ebook in architecture.html',
                           form_architecture_ebook_block_edit=form_architecture_ebook_block_edit, id=id)