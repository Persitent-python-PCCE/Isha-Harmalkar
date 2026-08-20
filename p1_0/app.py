import os
import logging
from dotenv import load_dotenv
from flask import Flask
from config.database import init_db, db
from models import (
    Role, User, Course, CourseInstructor, Enrollment,
    Module, Lesson, Material, LessonProgress, Quiz, Question, QuizRecord
)
from controllers.authController import authBp
from controllers.studentController import studentBp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
init_db(app)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime) s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Flask appplication initialed successfully")

app.register_blueprint(
    authBp
)
app.register_blueprint(studentBp)

@app.route("/")
def index():
    return "LMS is running"

if __name__ == "__main__":
    """ with app.app_context():
        db.create_all() """


    app.run(debug=True)