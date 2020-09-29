from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd53157d4061ed102dae462d1365e8b11'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trip.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from sampleproject import routes
