# from flask import Flask, render_template, request
# app = Flask(__name__) 


# # Static & Dynamic Routes
# #from flask import render_template
# @app.route('/')  #(static-route) every route has function to deal with it(page or action)   
# def hello_world():
#     # return 'Hello, From flask!'
#     return render_template('home.html') # to render html page
#                                         #<h1>Welcome to Home Page</h1>

# #from flask import Flask
# @app.route('/<name>') # (dynamic-route)
# def welcome(name):
#     return f'Hello, {name}! to my page' # http://127.0.0.1:5000/ali
#                                         #  Hello, ali! to my page

# #from flask import request
# @app.route('/users', methods=['GET', 'POST']) # to allow post method && #http://127.0.0.1:5000/users
# def users():
#     users = {'ali': 'ali@gmail.com', 'ahmed': 'ahmed@gmail.com'}
#     if request.method == 'GET':
#         return f'Users are: {users}' #http://127.0.0.1:5000/users ---> Users are: {'ali': 'ali@gmail.com', 'ahmed': 'ahmed@gmail.com'}
#     elif request.method == 'POST':
#         return 'the request is post'
    

# @app.route('/hello')
# def hello():
#     name="ali"
#     email='ali224101539@ksiu.edu.eg'
#     # return 'hello from flask'
#     return render_template('hello.html', n=name, g=email) #http://127.0.0.1:5000/hello --> This is hello path 
#     #                                                         hello ali
#     #                                                        email ali224101539@ksiu.edu.eg



# # Forms in Flask
# from flask_wtf import FlaskForm # to create form && prepare inputs,labels in class
# from wtforms import StringField, PasswordField, SubmitField,EmailField
# from wtforms.validators import DataRequired, Length, Email

# app.config['SECRET_KEY']='mysecretkey' # to protect from csrf attacks

# class RegisterForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
#     email = EmailField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     submit = SubmitField('Sign Up')
# @app.route('/register', methods=['GET', 'POST']) #http://http://127.0.0.1:5000/register
# def reg():
#     form = RegisterForm()
#     return render_template('register.html', form=form)




#Connect with database (with middleware)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey' # flash messages (like error msg)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # to connect with database
db=SQLAlchemy(app) 
migrate = Migrate(app, db) # to create migration folder
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/jobs')
def jobs():
    jobs = Job.query.all() # select * from jobs
    return render_template('jobs.html', jobs=jobs)

@app.route('/create',methods=['GET','POST']) #127.0.0.1:5000/create
def create():
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        location = request.form['location']
        job= Job(title=title, company=company, location=location)
        db.session.add(job)
        db.session.commit() # to save in database
        return redirect(url_for('jobs')) # after add job redirect to jobs page
    return render_template('create.html')







#API
from flask import jsonify
@app.route('/api/jobs', methods=['GET']) #http://127.0.0.1:5000/api/jobs
def get_jobs(): # return list of objects (json-format)
    jobs = Job.query.all() # select * from jobs
    data=[]
    for job in jobs: # extract data from each job object
        _job = {}
        _job['id'] = job.id
        _job['title'] = job.title
        _job['company'] = job.company
        _job['location'] = job.location
        data.append(_job) # append each job to data list
    # return {'jobs': data} # return json format
    return jsonify(data) 


# choose by id
@app.route('/api/jobs/<id>', methods=['GET']) #http://127.0.0.1:5000/api/jobs/4
def get_job(id):
    job= Job.query.get_or_404(id) # select * from jobs where id=id 
                                  # if not found return 404 error #http://127.0.0.1:5000/api/jobs/7
    data={'id': job.id, 'title': job.title, 'company': job.company, 'location': job.location}                  
    return jsonify(data)


#update
@app.route('/api/jobs/update/<id>', methods=['PUT']) #put method to update sumthing in database
def update_job(id):                                  
    job= Job.query.get_or_404(id) 
    if request.method == 'PUT':
        data=request.get_json() 
        job.title = data['title']
        job.company = data['company']
        job.location = data['location']
        db.session.commit()
        return 'job updated successfully'
    

#Delete
@app.route('/api/jobs/delete/<id>', methods=['DELETE'])
def delete_job(id):
    job = Job.query.get_or_404(id) 
    db.session.delete(job)
    db.session.commit()
    return 'job deleted successfully'
                                                
      