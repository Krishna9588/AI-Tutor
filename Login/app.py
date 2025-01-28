from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Flask-Login Setup
login_manager = LoginManager()
login_manager.init_app(app)


# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Routes
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password').encode('utf-8')
    remember = request.form.get('remember') == 'on'  # Get checkbox state

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.checkpw(password, user.password.encode('utf-8')):
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))
    flash('Invalid email or password', 'danger')
    return redirect(url_for('home'))


@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Validate passwords match
    if password != confirm_password:
        flash('Passwords do not match!', 'danger')
        return redirect(url_for('home'))

    if User.query.filter_by(email=email).first():
        flash('Email already registered!', 'danger')
        return redirect(url_for('home'))

    # Hash password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Create user
    new_user = User(email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    flash('Account created successfully!', 'success')
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    return "Welcome to your dashboard!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)