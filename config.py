import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f6963a86-a8bc-4b35-b712-d63f674043e2'

    # BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image26'
    # BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '58BsQsutgcvQWTwvNE65Milz6q6VZefHKr7tj+Ql+J7CCxHx8HPHxPdmJGjUwG3aj20ymYKcDuxU+AStpqAxnw=='
    # BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=image18;AccountKey=IHfXWkL5NAd4YbQvDX1g23D0bqqbI3lnw4ILQIIUug3Fmva1T1W3GMB1XlBU8cshpinRrraBtPu2+ASt2Iy8WQ==;EndpointSuffix=core.windows.net'
    if not BLOB_CONNECTION_STRING:
        logger.error("BLOB_CONNECTION_STRING is not set")
    else:
        logger.info("BLOB_CONNECTION_STRING is set")

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms26.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms26'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '@pass1234'
    
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET  = os.environ.get('CLIENT_SECRET') or 'bLr8Q~GbbNA3.I-CLGQVqch3bVeVpJQqh-oKGbNH'
    
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"

    CLIENT_ID = os.environ.get('CLIENT_ID') or 'aa0b42a1-202d-46cb-8e07-4b3cd591ac76'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
