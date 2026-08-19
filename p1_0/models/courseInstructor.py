from datetime import datetime, timezone

from config.database import db

class CourseInstructor(db.Model):
    __tablename__ = "course_instructors"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False,
        index=True
    )

    instructor_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        index=True
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
    
    __table_args__ = (
        db.UniqueConstraint(
            "course_id",
            "instructor_id",
            name="uq_course_instructor"
        ),
    )

    course  = db.relationship(
        "Course",
        back_populates="instructors"
    )

    instructor = db.relationship(
        "User",
        back_populates="course_instructors"
    )

    enrollemnts = db.relationship(
        "Enrollment",
        back_populates="course_instructor",
        cascade="all, delete-orphan"
    )

    materials = db.relationship(
        "Material",
        back_populates="course_instructor"
    )

