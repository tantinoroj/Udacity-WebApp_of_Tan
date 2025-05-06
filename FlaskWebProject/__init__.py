"""
The flask application package.
"""
import logging , os , sys
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__)
app.config.from_object(Config)

# Create a file handler that logs messages to a file
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.WARNING)  

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the app's logger
app.logger.addHandler(handler)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Import views after app is initialized to avoid circular imports
from FlaskWebProject import views, models

@login.user_loader
def load_user(id):
    return models.User.query.get(int(id))
