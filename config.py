import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '2971343e-c5d9-4bce-a664-56e7d292b42e'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') 
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') 
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') 
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') 

    SQL_SERVER = os.environ.get('SQL_SERVER') 
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    
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
    SCOPE = ["User.Read"] # Only need to read user profile for this app
    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
