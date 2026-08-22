import logging
from flask import(
    Blueprint,  render_template,
    redirect, send_file,
    url_for,
    session,jsonify,
    request,
    flash
)

from dao.courseInstructorDao import CourseInstructorDao
from forms.materialForms import MaterialForm
from dao.materialDao import MaterialDao
from dao.lessonDao import LessonDao
from services.materialService import MaterialServicea
from config.auth import roleRequired, wantsJson, loginRequired

logger = logging.getLogger(__name__)
materialBp = Blueprint("material", __name__)

materialDao = MaterialDao()
lessonDao = LessonDao()
courseInstructorDao = CourseInstructorDao()
materialService = MaterialServicea(materialDao, lessonDao)


@materialBp.route("/lessons/<int:lessonId>/materials", methods=["GET"])
@loginRequired
def listMaterials(lessonId):
    materials = materialService.getMaterialsByLessonId(lessonId)

    if wantsJson():
        return jsonify({
            "success": True,
            "materials": [material.toDict() for material in materials]
        })

    return render_template("materialList.html", materials=materials, lessonId=lessonId)


@materialBp.route("/lessons/<int:lessonId>/materials", methods=["POST"])
@roleRequired("admin", "instructor")
def uploadMaterial(lessonId):
    form = MaterialForm()
    if form.validate_on_submit():
        try:
            lesson = lessonDao.getLessonById(lessonId)
            courseId = lesson.module.course_id
            courseInstructor = courseInstructorDao.getByCourseAndInstructor(courseId, session["user_id"])
            if not courseInstructor:
                raise ValueError("You are not assigned to teach this course")
            
            courseInstructorId = courseInstructor.id
            material = materialService.uploadMaterial(
                lessonId,
                courseInstructorId=courseInstructorId,
                title=form.title.data,
                fileStorage=form.file.data,
                access=form.access.data
            )
            logger.info("Material uploaded successfully: %s", material.title)

            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Material uploaded successfully",
                    "material": material.toDict()
                }), 201

            flash("Material uploaded successfully", "success")
            return redirect(url_for("material.listMaterials", lessonId=lessonId))

        except ValueError as ve:
            logger.warning("Material upload validation failed")
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(ve)
                }), 400

            flash(str(ve), "danger")

        except Exception as e:
            logger.warning("An unexpected error occured while material upload")
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(e)
                }), 400

            flash("An unexpected error occured", "danger")

    if request.method == "POST" and wantsJson():
        return jsonify({
            "success": False,
            "erros": form.errors
        }), 400

    return render_template("materialForm.html", form=form, lessonId=lessonId)



@materialBp.route("/materials/<int:materialId>/download", methods=["GET"])
@loginRequired
def downloadMaterial(materialId):
    try:
        material = materialService.getMaterialById(materialId)
        return send_file(material.file_path, as_attachment=True)
    except ValueError as ve:
        logger.warning("Material download failed for id: %s", materialId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404

        flash(str(ve), "danger")
        return redirect(url_for("course.listCourses"))


    except ValueError as e:
        logger.warning("Unexpected error during material download  for id: %s", materialId)

        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 404

        flash("An unexpected error occured while downloading material", "danger")
        return redirect(url_for("course.listCourses"))




@materialBp.route("/materials/<int:materialId>/delete", methods=["POST"])
@loginRequired
def deleteMaterial(materialId):
    try:
        material = materialService.getMaterialById(materialId)
        lessonId = material.lesson_id
        materialService.deleteMaterial(materialId)
        logger.info("Material deleted successfully: %s", materialId)

        if wantsJson():
            return jsonify({
                "success": True,
                "message": "Material delted successfully"
            })

        flash("Material deleted successfully", "success")
        
        return redirect(url_for("material.listMaterials", lessonId=lessonId))
    except ValueError as ve:
        logger.warning("Material deletion failed for id: %s", materialId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404

        flash(str(ve), "danger")
     


    except ValueError as e:
        logger.warning("Unexpected error during material deletion  for id: %s", materialId)

        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 404

        flash("An unexpected error occured while deleting material", "danger")

    return redirect(url_for("course.listCourses"))
   