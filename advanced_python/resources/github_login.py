from flask import g, request, url_for
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from models.user import UserModel
from schemas.user import UserSchema
from oa import github

user_schema = UserSchema()


class GithubLogin(Resource):
    @classmethod
    def get(cls):
        return  github.authorize(callback="http://localhost:5000/login/github/authorized")



class GithubAuthorize(Resource):
    @classmethod
    def get(cls):
        resp = github.authorized_response()

        if resp is None or resp.get("access_token") is None:
            error_response = {
                "error" : request.args["error"],
                "error_desc": request.args["error_description"]
            }
        g.access_token = resp['access_token']
        github_user = github.get('user')
        github_username = github_user.data['login']

        user = UserModel.find_by_username(github_username)
        if not user:
            user = UserModel(username= github_username, password=1234, email='ori@gmail.com')
            user.save_to_db() # saved user that didnt register

        access_token = create_access_token(identity=user.id, fresh= True)
        refresh_token = create_refresh_token(identity=user.id)
        # we give him a token so he can make requests

        return {"access_token": access_token,"refresh_token":refresh_token}, 200
