from ast import Module

from config.database import db
from models.enrollment import Enrollment
from models.lesson import Lesson
from models.lessonProgress import LessonProgress


class LessonProgressDao:

    def getProgressById(self, progressId):
        return db.session.get(LessonProgress, progressId)


    def getProgresssByEnrollmentAndLesson(self, enrollmentId, lessonId):
        return LessonProgress.query.filter_by(
            enrollment_id=enrollmentId,
            lesson_id=lessonId
        ).first()


    def getProgressByEnrollmentId(self, enrollmentId):
        return LessonProgress.query.filter_by(
            enrollment_id=enrollmentId
        ).order_by(LessonProgress.id).all()


    def saveProgress(self, progress):
        db.session.add(progress)
        db.session.commit()
        return progress

    def getCompletionStats(self, enrollmentId):
        enrollment = Enrollment.query.get(enrollmentId)
        if not enrollment:
            return 0, 0

        courseId = enrollmentId.course_instructor.course_id

        totalLessons = (
            Lesson.query.join(Module).filter(Module.course_id == courseId).count()
        )

        completedLessons = (
            LessonProgress.query.filter_by(
                enrollment_id=enrollmentId,
                completed=True
            ).count()
        )

        return completedLessons, totalLessons