from config.database import db
from models.material import Material


class MaterialDao:

    def getMaterialById(self, materialId):
        return db.session.get(Material, materialId)


    def getMaterialsByLessonId(self, lessonId):
        return Material.query.filter_by(
            lesson_id=lessonId
        ).order_by(Material.id).all()


    def saveMaterial(self, material):
        db.session.add(material)
        db.session.commit()
        return material


    def deleteMaterial(self, material):
        db.session.delete(material)
        db.session.commit()