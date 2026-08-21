import pytest
from app import app
from config.database import db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False


    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

            db.session.remove()
            db.drop_all()


