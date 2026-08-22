from config.database import db
from models.lesson import Lesson


class LessonDao:
    def getLessonById(self, lessonId):
        return db.session.get(Lesson, lessonId)

    def getLessonByModuleId(self, moduleId):
        return Lesson.query.filter(
            module_id=moduleId
        ).order_by(Lesson.id).all()


    def saveLesson(self, lesson):
        db.session.add(lesson)
        db.session.commit()


    def lessonExistsByName(self, moduleId, lessonName):
        return Lesson.query.filter_by(
            module_id=moduleId,
            lesson_name=lessonName
        ).first() is not None


    