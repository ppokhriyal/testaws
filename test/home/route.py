from flask import Blueprint,render_template,url_for,flash,redirect,request
from test import app,db
from test.models import Users
from test.home.forms import AddUserForm
blue = Blueprint('home',__name__,template_folder='templates')

#Home
@blue.route('/',methods=('GET','POST'))
def home():
    form = AddUserForm()
    if form.validate_on_submit():
        user_db = Users(firstname=form.firstname.data,lastname=form.lastname.data)
        db.session.add(user_db)
        db.session.commit()
        return redirect(url_for('home.home'))
    return render_template('home/home.html',title='CRUD',form=form)