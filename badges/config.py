import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = (
        os.getenv("SECRET_KEY")
        or "equity~reprogram~unworried~splendid~deviation~width~pungent~awkward"
    )
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    URL_PREFIX = os.getenv("URL_PREFIX") or ""
