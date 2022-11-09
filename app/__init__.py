from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__) # this is checking to confirm that we have an app folder, and init file, etc.

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    from app.models.bike import Bike

    db.init_app(app)
    migrate.init_app(app, db)

    # the import needs to be inside the fuction
    from .routes.bike import bike_bp # this will access route > bike class > bike_bp variable.
    app.register_blueprint(bike_bp) # bring in this blueprint and connect it to my app, this is what I want to use

    from app.models.cyclist import Cyclist

    from .routes.cyclist import cyclist_bp
    app.register_blueprint(cyclist_bp)

    return app