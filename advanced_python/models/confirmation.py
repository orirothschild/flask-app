from time import time
from typing import List
from uuid import uuid4

from db import db

CONFIRMATION_EXPIRATION_DELTA = 1800  # 30 minutes


class ConfirmationModel(db.Model):
    __tablename__ = "confirmations"

    id = db.Column(db.String(50), primary_key=True)
    expire_at = db.Column(db.Integer, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel")

    def __init__(self, user_id: int, **kwargs): # we cant detrmain the amount of kwargs we wish to pass
        super().__init__(**kwargs) # this way when every kwarg that is passed is assigned to its counterpart, but we dont have to
      # python will call the super method and assign the correct kwargs inside db model
        #sql alchamy is smart enough to do it on its own
        self.user_id = user_id
        self.id = uuid4().hex
        self.expire_at = int(time()) + CONFIRMATION_EXPIRATION_DELTA
        self.confirmed = False

    @classmethod
    def find_by_id(cls, _id: str) -> "ConfirmationModel":
        return cls.query.filter_by(id=_id).first()


    @classmethod
    def find_all_id(cls) -> List["ConfirmationModel"]:
        return cls.query.all()

    @property
    def expired(self) -> bool:
        return time() > self.expire_at

    def force_to_expire(self) -> None:  # forcing current confirmation to expire
        if not self.expired: # self.expired is now passed inside a decorator so its not called as a function
            self.expire_at = int(time())
            self.save_to_db()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
