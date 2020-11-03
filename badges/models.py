import re
from typing import TypeVar, Union
from uuid import uuid4

from badges import db
import uuid as UUID

User = TypeVar("User")


VALID_ATTENDEE_TYPES = ["attendee", "speaker", "volunteer"]


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email_id = db.Column(db.String(120), index=True, unique=True)
    avatar_url = db.Column(
        db.String(120),
        nullable=False,
        default="https://www.gravatar.com/avatar/00000000000000000000000000000000",
    )
    twitter_id = db.Column(db.String(120))
    about = db.Column(db.String(240))
    type = db.Column(db.String(120), default="attendee")


    def set_type(self, type: str):
        if type not in VALID_ATTENDEE_TYPES:
            raise ValueError(
                "Attendee type has to be one of {}".format(
                    ", ".join(VALID_ATTENDEE_TYPES)
                )
            )

        self.type = type
        self.update()

    def update(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return "<User {}>".format(self.id)

    @classmethod
    def create(cls, email_id: str, fullname: str, type: str) -> User:
        a = User(
            type=type,
            email_id=email_id,
            fullname=fullname,
        )
        db.session.add(a)
        db.session.commit()

        return a

    @classmethod
    def find_by_id(cls, id: int) -> Union[User, None]:
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email_id(cls, email_id: str) -> Union[User, None]:
        return cls.query.filter_by(email_id=email_id).first()
