from datetime import datetime, timezone
from config.database import db

class Material(db.Model):
    __tablename__ = "materials"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    lesson_id = db.Column(
        db.Integer,
        db.ForeignKey("lessons.id"),
        nullable=False,
        index=True
    )

    course_instructor_id = db.Column(
        db.Integer,
        db.ForeignKey("course_instructors.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    file_path = db.Column(
        db.String(500),
        nullable=False
    )

    file_type = db.Column(
        db.String(50),
        nullable=False
    )



    access = db.Column(
        db.String(50),
        default="public"
    )

    created_at = db.Column(
            db.DateTime,
            default=lambda: datetime.now(timezone.utc),
            nullable=False
        )
        
    updated_at = db.Column(
        db.DateTime,        
        default=lambda: datetime.now(timezone.utc),
        onupdate= lambda: datetime.now(timezone.utc),
        nullable=False
    )

    lesson = db.relationship(
        "Lesson",
        back_populates="materials"
    )

    course_instructor = db.relationship(
        "CourseInstructor",
        back_populates="materials"
    )


