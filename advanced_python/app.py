import os
from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_uploads import configure_uploads, patch_request_class
from marshmallow import ValidationError
from resources.github_login import GithubLogin, GithubAuthorize
from werkzeug.urls import url_quote, url_decode, url_encode
from werkzeug.http import parse_accept_header
from werkzeug.utils import cached_property


load_dotenv(".env", verbose=True) # loads our env file before we run our app

from flask_migrate import Migrate
from ma import ma
from db import db
from oa import oauth
from blacklist import BLACKLIST
from sqlalchemy import create_engine

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.confirmation import Confirmation, ConfirmationByUser
from resources.user import UserRegister, UserLogin, User, TokenRefresh, UserLogout, UserList
from resources.image import ImageUpload, Image, AvatarUpload, Avatar
from libs.image_helper import IMAGE_SET


app = Flask(__name__)
app.config.from_object("default_config") #load the app with the default config
app.secret_key = 'super secret'
app.config.from_envvar("APPLICATION_SETTINGS") #the config is loaded to memory, notice to edit when k8s is used
patch_request_class(app, 10 * 1024 * 1024) # 10 mb max size
configure_uploads(app, IMAGE_SET)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_marshmellow_validation(err): # exceptr all ValidationError, bubbles up all validation errors here
    return jsonify(err.messages),400


jwt = JWTManager(app)
migrate = Migrate(app, db)

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserList, "/users")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(Confirmation, "/user_confirm/<string:confirmation_id>")
api.add_resource(ConfirmationByUser, "/confirmation/user/<int:user_id>")
api.add_resource(ImageUpload, "/upload/image")
api.add_resource(Image, "/image/<string:filename>")
api.add_resource(AvatarUpload, "/upload/avatar")
api.add_resource(Avatar, "/avatar/<int:user_id>")
api.add_resource(GithubLogin, "/login/github")
api.add_resource(GithubAuthorize, "/login/github/authorized")


def create_app():
    db.init_app(app)
    # tells the marshmallow what app to communicate with
    ma.init_app(app)
    oauth.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)