from app import app, db, login_manager
from flask import request, render_template, flash, redirect,url_for
from models import User, Post
from forms import RegistrationForm,LoginForm, DestinationForm
from werkzeug.urls import url_parse


# helper function -- loads user
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
  #check if current_user logged in, if so redirect to a page that makes sense
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
  #check if current_user logged in, if so redirect to a page that makes sense
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#@app.route('/user/<username>',methods=['GET', 'POST'])
#@login_required
#def user(username):
	#user = current_user
	#user = User.query.filter_by(username=user.username).first()
	#posts = Post.query.filter_by(user_id=user.id)
	#if posts is None:
		#posts = []
	#form = DestinationForm()
	#if request.method == 'POST' and form.validate():
		#new_destination = Post(city = form.city.data,country=form.country.data,description=form.description.data, user_id=current_user.id)
		#db.session.add(new_destination)
		#db.session.commit()
	#else:
		#flash(form.errors)
		#unpopular_songs = Song.query.order_by(Song.n).all()[:3]
	#destinations = Destination.query.all()
	#return render_template('user.html', user=user, posts=posts, form=form)

@app.route('/')
def index():
  #posts = Post.query.all()
  #if not posts:
    #posts=[]
  posts=[]
  return render_template('landing_page.html',posts=posts)


