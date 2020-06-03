from db import db
from flask import request, url_for
from models.confirmation import ConfirmationModel
from requests import Response
from libs.mailgun import Mailgun
class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)

    confirmation = db.relationship(
        "ConfirmationModel", lazy="dynamic" # retrive only when confirmation is required
        , cascade="all, delete-orphan" # whenever a user is deleted it will delete its confirmation
    )
    # we now know its going to return a ConfirmationModel from the type hinting
    @property
    def most_recent_confirmation(self) -> "ConfirmationModel" :
        return self.confirmation.order_by(db.desc(ConfirmationModel.expire_at)).first()

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()



    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all_users(cls) -> "UserModel":
        return cls.query.all()

    def send_confirmation_email(self) -> Response: # a response is something  we give to another api
        # localhost:5000 is url root
        #[:-1] we request the entrire localhost wothout the endig slash

        #url_for is thge resuource name + the resoururce id named user id
        subject = "Registration Confirmation"
        link = request.url_root[:-1] + url_for(
            "confirmation", confirmation_id=self.most_recent_confirmation.id
        )
        text = f"Please click the link to confirm your registration: {link}"
        html = f"<html>Please click the link to confirm your registration: <a href={link}>link</a></html>"
        return Mailgun.send_email([self.email], subject, text, html)



    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
