import logging

from models.lessonProgress import LessonProgress

logger = logging.getLogger(__name__)

class LessonProgressService:

    def __init__(self, lessonProgressDao):
        self.lessonProgressDao = lessonProgressDao


    def markLessonComplete(self, enrollmentId, lessonId, completed=True):
        progress = self.lessonProgressDao.getProgressByEnrollmentAndLesson(
            enrollmentId, lessonId
        )

        if not progress:
            progress = LessonProgress(
                enrollment_id=enrollmentId,
                lesson_id=lessonId,
                completed=completed                
            )
        else:
            progress.completed = completed

        return self.lessonProgressDao.saveProgress(progress)


    def getProgressByEnrollmentId(self, enrollmentId):
        return self.lessonProgressDao.getProgressByEnrollmentId(enrollmentId)


    