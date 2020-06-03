from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# def connect_to_sqlite():
#     db = SQLAlchemy()
#     return db
#
# def connect_to_postgres(app: Flask):
#     db = SQLAlchemy(app)
#     return db


db = SQLAlchemy()
