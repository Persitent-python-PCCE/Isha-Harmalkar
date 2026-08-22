from config.database import db
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