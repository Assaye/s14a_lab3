import os

DEBUG = False
SECRET_KEY = 's14a_key'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
