import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(dev):
    
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', 'dev' + '.py')
    #  python - import os - os.getcwd() - os.path.join(os.getcwd(), 'config', config_type + '.py')
    # 'C:\\Users\\Bulti\\WebDev\\s14a\\lab3_book_store\\config\\dev.py'
    app.config.from_pyfile(configuration)   
    db.init_app(app)
   
    bootstrap.init_app(app)  # Initialize bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main # importing blueprint from app.catalog
    app.register_blueprint(main)
    
    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



