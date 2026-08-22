
import logging
from models.module import Module

logger = logging.getLogger(__name__)

class ModuleService:

    def __init__(self, moduleDao):
        self.moduleDao = moduleDao



    def createModule(self, courseId, moduleName, description=None):
        if self.moduleDao.moduleExistsByName(courseId,moduleName) or self.moduleDao.moduleExistsByName(courseId,moduleName.strip().lower()) :
            raise ValueError("A module with this name already exists in this course")

        module = Module(
            course_id=courseId,
            module_name=moduleName.strip(),
            description=description            
        )

        return self.moduleDao.saveModule(module)

    def getModuleById(self, moduleId):
        module = self.moduleDao.getModuleById(moduleId)
        if not module:
            raise ValueError("Module not found")

        return module


    def getModuleByCourseId(self, courseId):
        return self.moduleDao.getModulesByCourseId(courseId)


    def updateModule(self, moduleId,moduleName=None, description=None):
        module = self.getModuleById(moduleId)
        if moduleName and moduleName != module.module_name:
            if self.moduleDao.moduleExistsByName(module.course_id, moduleName) or self.moduleDao.moduleExistByName(module.course_id, moduleName.strip().lower()):
                raise ValueError("A module with this name already exists in this course")
            module.module_name = moduleName


        if description is not None:
            module.description = description

        return self.moduleDao.saveModule(module)


    def deleteModule(self, moduleId):
        module = self.getModuleById(moduleId)
        self.moduleDao.deleteModule(module)
        