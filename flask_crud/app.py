from flask import Flask
from config.database import init_db, db
from controllers.productController import productController

app = Flask(__name__)



init_db(app)
app.register_blueprint(productController)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)