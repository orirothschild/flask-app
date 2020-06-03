import os

secret_key = 'super secret key'
DEBUG = True
DB = os.environ["DB_NAME"]
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URI"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PW = os.environ["POSTGRES_PW"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
PORT = os.environ["PORT"]


SQLALCHEMY_DATABASE_URI = f'{DB}{POSTGRES_USER}:{POSTGRES_PW}@{SQLALCHEMY_DATABASE_URL}:{PORT}/{POSTGRES_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
UPLOADED_IMAGES_DEST = os.path.join("static", "images")  # manage root folder
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"] # we wish to crash the app if it dosent exist
UPLOADED_IMAGES_DEST = os.path.join("static", "images") # location for images
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens


