import os
import logging
from werkzeug.utils import secure_filename

from models.material import Material

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "mp4", "docx", "pptx"}
MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024
UPLOAD_ROOT = "uploads"


class MaterialService:
    def __init__(self, materialDao, lessonDao):
        self.materialDao  = materialDao
        self.lessonDao = lessonDao


    def _getExtension(self, filename):
        if "." not in filename:
            return ""

        return filename.rsplit(".", 1)[1].lower()


    def uploadMaterial(self, lessonId, courseInstructorId, title, fileStorage, access="public"):
        lesson = self.lessonDao.getLessonById(lessonId)
        if not lesson:
            raise ValueError("Lesson not found")

        filename = secure_filename(fileStorage.filename)
        extension = self._getExtension(filename)



        if extension not in ALLOWED_EXTENSIONS:
            raise ValueError("File exceeds maximum allowed size")


        courseId = lesson.module.course_id
        moduleId = lesson.module_id


        targetDir = os.path.join(targetDir, filename)
        os.makedirs(targetDir, exist_ok=True)

        filePath = os.path.join(targetDir, filename)
        fileStorage.save(filePath)

        material = Material(
            lesson_id = lessonId,
            course_instructor_id =courseInstructorId,
            title=title,
            file_path=filePath,
            file_type=extension,
            access=access            
        )

        return self.materialDao.saveMaterial(material)


    def getMaterialById(self, materialId):
        material = self.materialDao.getMaterialById(materialId)
        if not material:
            raise ValueError("Material not found")
        return material


    def getMaterialsByLessonId(self, lessonId):
        return self.materialDao.getMaterialsByLessonId(lessonId)


    def deleteMaterial(self, material, instructorId):

        if material.course_instructor.instructor_id != instructorId:
            raise PermissionError("You are not authorized to delete this material")

        

        if os.path.exists(material.file_path):
            try:
                os.remove(material.file_path)
            except OSError:
                logger.exception("Failed to remove file from disk: %s", material.file_path)


        self.materialDao.deleteMateria(material)
