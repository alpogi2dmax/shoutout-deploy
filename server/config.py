# Standard library imports
import os

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
# from flask_session import Session 
from flask_marshmallow import Marshmallow
from datetime import timedelta

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = 'secret_key'
# app.config["SESSION_COOKIE_SECURE"] = False  # Required for HTTPS
# app.config["SESSION_COOKIE_HTTPONLY"] = True  # Prevent JS access to cookies
# app.config["SESSION_COOKIE_SAMESITE"] = "None"  # Allow cross-site requests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE=True
)

app.json.compact = False



# Session config
app.permanent_session_lifetime = timedelta(days=7)


# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)

ma = Marshmallow(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
# Session(app)
CORS(app, supports_credentials=True, origins=["https://shoutout-deploy-1.onrender.com"])
