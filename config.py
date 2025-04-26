import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '26dd918b-e70d-4470-b328-137159187428'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image18'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'IHfXWkL5NAd4YbQvDX1g23D0bqqbI3lnw4ILQIIUug3Fmva1T1W3GMB1XlBU8cshpinRrraBtPu2+ASt2Iy8WQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=image18;AccountKey=IHfXWkL5NAd4YbQvDX1g23D0bqqbI3lnw4ILQIIUug3Fmva1T1W3GMB1XlBU8cshpinRrraBtPu2+ASt2Iy8WQ==;EndpointSuffix=core.windows.net'
    if not BLOB_CONNECTION_STRING:
        logger.error("BLOB_CONNECTION_STRING is not set")
    else:
        logger.info("BLOB_CONNECTION_STRING is set")

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmstan.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!pwd1234'
    
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET  = os.environ.get('CLIENT_SECRET') or 'kAZ8Q~h21nWxTOyd85KKfkgRsDSeGYGLnLZF7ap3'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"

    CLIENT_ID = os.environ.get('CLIENT_ID') or 'cd8e5735-7129-4065-9538-2a3499e29835'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
