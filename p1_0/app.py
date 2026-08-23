from datetime import timedelta
import os
import logging
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from config.database import init_db, db
from models import (
    Role, User, Course, CourseInstructor, Enrollment,
    Module, Lesson, Material, LessonProgress, Quiz, Question, QuizRecord
)
from controllers.authController import authBp
from controllers.studentController import studentBp
from controllers.instructorController import instructorBp
from controllers.adminController import adminBp
from controllers.courseController import courseBp
from controllers.moduleController import moduleBp
from controllers.lessonController import lessonBp
from controllers.materialController import materialBp
from controllers.lessonProgressController import lessonProgressBp
from controllers.courseInstructorController import courseInstructorBp
from controllers.enrollmentController import enrollmentBp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY', app.config['SECRET_KEY'])
app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies"]
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)
app.config['WTF_CSRF_ENABLED'] = False
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

app.register_blueprint(authBp)
app.register_blueprint(courseBp)
app.register_blueprint(moduleBp)
app.register_blueprint(lessonBp)
app.register_blueprint(materialBp)
app.register_blueprint(lessonProgressBp)
app.register_blueprint(studentBp)
app.register_blueprint(instructorBp)
app.register_blueprint(adminBp)
app.register_blueprint(courseInstructorBp)
app.register_blueprint(enrollmentBp)

@app.route("/")
def index():
    return "LMS is running"

if __name__ == "__main__":
    """ with app.app_context():
        db.create_all() """


    app.run(debug=True)