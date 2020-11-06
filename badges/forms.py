import re

from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms import Field, IntegerField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    NumberRange,
    Length,
    ValidationError,
    url,
    UUID,
)


class VerifyEmailForm(FlaskForm):
    email_id = StringField("Email Address", validators=[DataRequired(), Email()])
    submit = SubmitField("Verify!")


class BadgeForm(FlaskForm):
    fullname = StringField(
        "Full Name",
        description="Your name that should be visible on the badge",
        validators=[DataRequired()],
    )
    avatar_url = URLField(
        "Avatar URL",
        description="A link to the image that you want as your photo on the badge. The image ideally should be of 1:1 aspect ratio.",
        validators=[url()],
    )
    twitter_id = StringField("Twitter ID", description="Your Twitter ID")
    about = StringField(
        "About",
        description="Write something unique about you",
        validators=[
            Length(max=80, message="About section needs to be less than 80 characters")
        ],
    )
    submit = SubmitField("Save")
