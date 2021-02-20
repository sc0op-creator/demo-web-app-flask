from datetime import datetime
from enum import unique
from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '0dsdas8asd8as'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/signup form with flask'
db = SQLAlchemy(app)

class Id(db.Model):
    # serial_no , name , email , password , date_time
    serail_no = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    password = db.Column(db.String(50), nullable = False, unique = False)
    date_time = db.Column(db.String(12), nullable=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login',methods = ["GET","POST"])
def login():
    return render_template('login.html')

@app.route('/signup',methods = ["GET","POST"])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        entry = Id(name = username, email = email, password= password, date_time = datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)

