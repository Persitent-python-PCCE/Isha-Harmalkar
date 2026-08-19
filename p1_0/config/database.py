from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    #app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://root:password@localhost/product_1")
    app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://root:password@localhost/lms_1")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)