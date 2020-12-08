from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db
from app.forms import *
from app.models import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    home_function_block_load = home_functions_block.query
    home_about_block_load = home_about_block.query
    home_client_block_load = home_client_block.query

    return render_template('home.html', title='',
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

    return render_template('home_function_block_add.html', form_home_func_block_add=form_home_func_block_add)

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

    return render_template('home_function_block_edit.html', title='Editing block Functions in home.html',
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

    return render_template('home_about_block_add.html', form_home_about_block_add=form_home_about_block_add)

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

    return render_template('home_about_block_edit.html', title='Editing block About in home.html',
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

    return render_template('home_client_block_add.html', form_home_client_block_add=form_home_client_block_add)

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

    return render_template('home_client_block_edit.html', title='Editing block Client in home.html',
                           form_home_client_block_edit=form_home_client_block_edit, id=id)


@app.route('/about', methods=['GET', 'POST'])
def about():
    about_net_block_load = about_net_block.query
    return render_template('about.html', title='About', about_net_block=about_net_block_load)

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
    return render_template('about_net_block_add.html', form_about_net_block_add=form_about_net_block_add)

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

    return render_template('about_net_block_edit.html', title='Editing block net in about.html',
                           form_about_net_block_edit=form_about_net_block_edit, id=id)
                           
                           
@app.route('/architecture', methods=['GET', 'POST'])
def architecture():
    architecture_item_block_load = architecture_item_block.query
    architecture_ebook_block_load = architecture_ebook_block.query
    return render_template(
        'architecture.html', title='Architecture',
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
    return render_template('architecture_item_block_add.html', form_architecture_item_block_add=form_architecture_item_block_add)
    
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

    return render_template('architecture_item_block_edit.html', title='Editing block item in architecture.html',
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
    return render_template('architecture_ebook_block_add.html', form_architecture_ebook_block_add=form_architecture_ebook_block_add)
    
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

    return render_template('architecture_ebook_block_edit.html', title='Editing block ebook in architecture.html',
                           form_architecture_ebook_block_edit=form_architecture_ebook_block_edit, id=id)


@app.route('/admin_home')
def admin_home():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    admin_list = Admin.query
    return render_template('admin_home.html', title='Admin Home - ', admin_list=admin_list)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(user_id=form.user_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('User ID or password is not correct')
            return render_template('admin_login.html', title='Admin Login - ', form=form)
        login_user(user, remember=form.keep_login_status.data)
        # https://stackoverflow.com/questions/37472870/login-user-fails-to-get-user-id (4/7/2020 1:15AM)
        return redirect(url_for('admin_home'))
    return render_template('admin_login.html', title='Admin Login - ', form=form)

@app.route('/admin_logout')
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/add_admin', methods=['GET', 'POST'])
def add_admin():
    form = AddAdminForm()
    if form.validate_on_submit():
        check_user = Admin.query.filter_by(user_id=form.user_id.data).first()
        check_email = Admin.query.filter_by(email=form.email.data).first()
        if check_user is not None:
            flash('This user ID already used.')
            return render_template('add_admin.html', title='Add Admin - ', form=form)
        if check_email is not None:
            flash('This Email already used.')
            return render_template('add_admin.html', title='Add Admin - ', form=form)
        if form.verification_key.data != 'O8afSh2OHdqyKvJyzeS4XKXQ':
            flash('The verification key is not correct.')
            return render_template('add_admin.html', title='Add Admin - ', form=form)
        user = Admin(user_id=form.user_id.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Added a new admin.')
        return redirect(url_for('admin_home'))
    return render_template('add_admin.html', title='Add Admin - ', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

