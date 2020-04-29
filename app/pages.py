from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.forms import home_function_block_add, home_about_block_add, home_client_block_add, home_function_block_edit, \
    home_about_block_edit, home_client_block_edit, AdminLoginForm, AddAdminForm
from app.models import Admin, home_functions_block, home_about_block, home_client_block


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

            db.session.commit()
            flash('edited content id: ' + id + ' on functions block in home.html')
        elif form_home_func_block_edit.editype.data == 'delete':
            home_functions_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on functions block in home.html')
            # https://stackoverflow.com/questions/27158573/how-to-delete-a-record-by-id-in-flask-sqlalchemy (4/9/2020 4:x9PM)
        return redirect(url_for('home'))
    elif request.method == 'GET':

        form_home_func_block_edit.title.data = str(db.session.query(home_functions_block.title).filter_by(id=id).first())
        form_home_func_block_edit.icon.data = str(db.session.query(home_functions_block.icon).filter_by(id=id).first())
        form_home_func_block_edit.content.data = str(db.session.query(home_functions_block.content).filter_by(id=id).first())

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

            db.session.commit()
            flash('edited content id: ' + id + ' on about block in home.html')
        elif form_home_about_block_edit.editype.data == 'delete':
            home_about_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on about block in home.html')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form_home_about_block_edit.title.data = str(db.session.query(home_about_block.title).filter_by(id=id).first())
        form_home_about_block_edit.image.data = str(db.session.query(home_about_block.image).filter_by(id=id).first())
        form_home_about_block_edit.content.data = str(db.session.query(home_about_block.content).filter_by(id=id).first())
        form_home_about_block_edit.link.data = str(db.session.query(home_about_block.link).filter_by(id=id).first())
        form_home_about_block_edit.link_text.data = str(db.session.query(home_about_block.link_text).filter_by(id=id).first())

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

            db.session.commit()
            flash('edited content id: ' + id + ' on client block in home.html')
        elif form_home_client_block_edit.editype.data == 'delete':
            home_client_block.query.filter_by(id=id).delete()
            db.session.commit()
            flash('deleted content id: ' + id + ' on client block in home.html')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form_home_client_block_edit.client_logo.data = str(db.session.query(home_client_block.client_logo).filter_by(id=id).first())

    return render_template('home_client_block_edit.html', title='Editing block Client in home.html',
                           form_home_client_block_edit=form_home_client_block_edit, id=id)


@app.route('/about', methods=['GET', 'POST'])
def about():


    return render_template('about.html', title='About',)



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

