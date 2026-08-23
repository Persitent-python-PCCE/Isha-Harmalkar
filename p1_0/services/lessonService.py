import logging

from models.lesson import Lesson
logger = logging.getLogger(__name__)


class LessonService:

    def __init__(self, lessonDao):
        self.lessonDao = lessonDao



    def createLesson(self, moduleId, lessonName, content=None):
        if self.lessonDao.lessonExistsByName(moduleId, lessonName) or self.lessonDao.lessonExistsByName(moduleId, lessonName.lower()):
            raise ValueError("A lesson with this name already exists in this module")

        lesson = Lesson(
            module_id=moduleId,
            lesson_name=lessonName,
            content=content            
        )

        return self.lessonDao.saveLesson(lesson)


    def getLessonById(self, lessonId):
        lesson = self.lessonDao.getLessonById(lessonId)
        if not lesson:
            raise ValueError("Lesson not found")

        return lesson


    def getLessonByModuleId(self, moduleId):
        return self.lessonDao.getLessonByModuleId(moduleId)


    def updateLesson(self, lessonId, lessonName=None, content=None):
        lesson = self.getLessonById(lessonId)

        if lessonName and lessonName != lesson.lesson_name:
            if self.lessonDao.lessonExistsByName(lesson.module_id, lessonName) or self.lessonDao.lessonExistsByName(lesson.module_id, lessonName.lower()):
                raise ValueError("A lesson witht this name already exists in the moudles")
            lesson.lesson_name = lessonName.strip()


        if content is not None:
            lesson.content = content.strip()


        return self.lessonDao.saveLesson(lesson)


    def deleteLesson(self, lessonId):
        lesson = self.getLessonById(lessonId)
        self.lessonDao.deleteLesson(lesson)
