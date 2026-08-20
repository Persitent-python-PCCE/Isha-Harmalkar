from datetime import datetime, timezone
from config.database import db

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    course_name = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        #default=datetime.now(datetime.timezone.utc),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    
    updated_at = db.Column(
        db.DateTime,
        #default=datetime.now(datetime.timezone.utc),
        default=lambda: datetime.now(timezone.utc),
        #onupdate=datetime.now(datetime.timezone.utc),
        onupdate= lambda: datetime.now(timezone.utc),
        nullable=False
    )

    instructors = db.relationship(
        "CourseInstructor",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    modules = db.relationship(
        "Module",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    """    quizzes = db.relationship(
        "Quiz",
        back_populates="course",
        cascade="all, delete-orphan"
    ) """