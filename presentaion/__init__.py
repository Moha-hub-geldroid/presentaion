from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "ec29e9c6c1116fe18003de25ffa6805200e8711d42ab0cadce7e85b52d07b8c7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ju_users_record.db"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = 'info'

from presentaion import routes
