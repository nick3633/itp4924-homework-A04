from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *
from app import app
from app.app_about.forms import about_net_block_add, about_net_block_edit
from app.app_about.models import about_net_block


@app.route('/about', methods=['GET', 'POST'])
def about():
    about_net_block_load = about_net_block.query
    return render_template('app_about/about.html', title='About', about_net_block=about_net_block_load)


@app.route('/about/net_block/add', methods=['GET', 'POST'])
def about_net_blk_add():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))

    form_about_net_block_add = about_net_block_add()
    if form_about_net_block_add.validate_on_submit():
        net_add = about_net_block(
            title = form_about_net_block_add.title.data,
            media = form_about_net_block_add.media.data,
            content = form_about_net_block_add.content.data,
            link = form_about_net_block_add.link.data,
            link_text = form_about_net_block_add.link_text.data,
            editor_user_id = current_user.user_id
        )
        db.session.add(net_add)
        db.session.commit()
        flash('content added on net block in about.html')
        return redirect(url_for('about'))
    return render_template('app_about/about_net_block_add.html', form_about_net_block_add=form_about_net_block_add)


@app.route('/about/net_block/edit/<id>', methods=['GET', 'POST'])
def about_net_blk_edit(id):
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form_about_net_block_edit = about_net_block_edit()

    if form_about_net_block_edit.validate_on_submit():
        if form_about_net_block_edit.editype.data == 'edit':
            net_edit = about_net_block.query.filter_by(id=id).first()
            net_edit.title = form_about_net_block_edit.title.data
            net_edit.media = form_about_net_block_edit.media.data
            net_edit.content = form_about_net_block_edit.content.data
            net_edit.link = form_about_net_block_edit.link.data
            net_edit.link_text = form_about_net_block_edit.link_text.data
            net_edit.edited_time = datetime.utcnow()
            net_edit.editor_user_id = current_user.user_id

            db.session.commit()
            flash('edited content id: ' + id + ' on net block in about.html')
        elif form_about_net_block_edit.editype.data == 'delete':
            about_net_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on net block in about.html')
        return redirect(url_for('about'))
    elif request.method == 'GET':
        get_value = about_net_block.query.filter_by(id=id).first()
        form_about_net_block_edit.title.data = get_value.title
        form_about_net_block_edit.media.data = get_value.media
        form_about_net_block_edit.content.data = get_value.content
        form_about_net_block_edit.link.data = get_value.link
        form_about_net_block_edit.link_text.data = get_value.link_text

    return render_template('app_about/about_net_block_edit.html', title='Editing block net in about.html',
                           form_about_net_block_edit=form_about_net_block_edit, id=id)