import os
import logging
basedir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2971343e-c5d9-4bce-a664-56e7d292b42e'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'image30'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '6g1dmgSmM4xJuujBArXCDZnGUe4kmxavKi2qyCc8qJ3RseIHhZRBLg/9xcclMiLY+oustPrFyXE/+AStKi8CwQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'image'
    
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=image30;AccountKey=6g1dmgSmM4xJuujBArXCDZnGUe4kmxavKi2qyCc8qJ3RseIHhZRBLg/9xcclMiLY+oustPrFyXE/+AStKi8CwQ==;EndpointSuffix=core.windows.net'
    if not BLOB_CONNECTION_STRING:
        logger.error("BLOB_CONNECTION_STRING is not set")
    else:
        logger.info("BLOB_CONNECTION_STRING is set")

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmstan2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!pwd1234'
    
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET  = '5038Q~N~2KCnaRV3gov~STzRepw6hcINpKXh4b9z'
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"
    CLIENT_ID = '416d6f76-eb16-48ac-a864-59b8326309a1'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app
    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
