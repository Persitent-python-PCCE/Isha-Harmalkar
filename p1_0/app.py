from flask import Flask
from config.database import init_db, db
from models import (
    Role, User, Course, CourseInstructor, Enrollment,
    Module, Lesson, Material, LessonProgress, Quiz, Question, QuizRecord
)

app = Flask(__name__)
init_db(app)


if __name__ == "__main__":
    """ with app.app_context():
        db.create_all() """


    app.run(debug=True)