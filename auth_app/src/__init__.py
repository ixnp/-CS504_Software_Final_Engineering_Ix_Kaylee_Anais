# - Krishna, A. (2023, November 27). How to Implement Two-Factor Authentication with PyOTP and Google Authenticator in Your Flask App.
#   freeCodeCamp.org. https://www.freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app/
#
# This file is responsible for initializing the Flask application and
# configuring its major components.

from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Redirect users to the login page if they are not authenticated
login_manager.login_view = "accounts.login"

# Flash login messages using the "danger" category
login_manager.login_message_category = "danger"

# Initialize password hashing
bcrypt = Bcrypt(app)

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Initialize database migration support
migrate = Migrate(app, db)

# Import the User model after the Flask app and extensions
# have been initialized to avoid circular imports
from src.accounts.models import User

# Load the current user from the session using their user ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

# Blueprints organize routes into separate, modular components
from src.accounts.views import accounts_bp
from src.core.views import core_bp

# Register application blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
