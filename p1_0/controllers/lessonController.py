import logging
from flask import(
    Blueprint,  render_template,
    redirect,
    url_for,
    session,jsonify,
    request,
    flash
)

from forms.lessonForms import LessonForm
from dao.lessonDao import LessonDao
from services.lessonService import LessonService
from config.auth import roleRequired, wantsJson, loginRequired

logger = logging.getLogger(__name__)
lessonBp = Blueprint("lesson", __name__)
lessonDao = LessonDao()
lessonService = LessonService(lessonDao)


@lessonBp.route("/moudles/<int:moduleId>/lessons", methods=["GET"])
@loginRequired
def listLessons(moduleId):
    lessons = lessonService.getLessonByModuleId(moduleId)

    if wantsJson():
        return jsonify({
            "success": True,
            "lessons": [lesson.toDict() for lesson in lessons]
        })

    return render_template("lessonList.html", lessons=lessons, moduleId=moduleId)



@lessonBp.route("/lessons/<int:lessonId>", method=["GET"])
@loginRequired
def getLesson(lessonId):
    try:
        lesson = lessonService.getLessonById(lessonId)

        if wantsJson():
            return jsonify({"success": True, "lesson": lesson.toDict()})
        return render_template("lesson.html", lesson=lesson)

    except ValueError as ve:
        logger.warning("Lesson lookup failed for id %s", lessonId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404

        return redirect(url_for("course.listCourses"))


    except Exception as e:
        logger.exception("Unexpected error fetching lesson %s", lessonId)
        if wantsJson():
            return jsonify({"success": False, "message": str(e)}), 400

        flash("An unexpected error occured", "danger")
        return redirect(url_for("course.listCourses"))



@lessonBp.route("/modules/<int:moduleId>/lessons", methods=["POST"])
@roleRequired("admin", "instructor")
def createLesson(moduleId):
    form = LessonForm()
    if form.validate_on_submit():
        try:
            lesson = lessonService.createLesson(
                moduleId,
                lessonName=form.lessonName.data,
                content=form.content.data
            )
            logger.info("Lesson created successfully: %s", lesson.lesson_name)

            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Lesson created successfully",
                    "lesson": lesson.toDict()
                }), 201

            flash("Lesson created successfully", "success")

            return redirect(url_for("lessong.listLesson", moduleId=moduleId))


        except ValueError as ve:
            logger.warning("Lesson creation validation failed")
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message" : str(ve)
                }), 400

            flash(str(ve), "danger")

        except Exception as e:
            logger.exception("Unexpected error during lesson creation")
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(e)
                }), 400
            flash("An unexpected error occurred", "danger")

    if request.method == "POST" and wantsJson():
        return jsonify({
            "success": False,
            "errors": form.errors
        }), 400

    return render_template("lessonForm.html", form=form, moduleId=moduleId)


@lessonBp.route("/lessons/<int:lessonId>/update", methods=["POST"])
@roleRequired("admin", "instructor")
def deleteLesson(lessonId):
    form = LessonForm()

    if form.validate_on_submit():
        try:
            lesson = lessonService.updateLesson(
                lessonId,
                lessonName=form.lessonName.data,
                content=form.content.data
            )
            logger.info("Lesson updated successfully: %s", lesson.lesson_name)

            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Lesson updated successfully",
                    "lesson": lesson.toDict()
                })

            flash("Lesson updated successfully", "success")
            return redirect(url_for("lesson.getLesson", lessonId=lesson.id))


        except ValueError as ve:
            logger.warning("Lesson update validationf failed for id %s", lessonId)
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(ve)
                }), 400

            flash(str(ve), "danger")

        except Exception as e:
            logger.warning("Unexpected error occured during lesson update for %s", lessonId)
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(e)
                }), 400

            flash("An unexpected error occured during update", "danger")

    if request.method == "POST" and wantsJson():
        return jsonify({
            "success": False,
            "errors": form.errors
        }), 400

    return render_template("lessonForm.html", form=form)

@lessonBp.route("/lessons/<int:lessonId>/delete", methods=["POST"])
@roleRequired("admin", "instructor")
def deleteLesson(lessonId):
    try:
        lesson = lessonService.getLessonById(lessonId)
        moduleId = lesson.module_id
        lessonService.deleteLesson(lessonId)
        logger.info("Lesson deleted successfully: %s", lessonId)

        if wantsJson():
            return jsonify({
                "success": True,
                "message": "Lesson  deleted successfully"
            })

        flash("Lesson deleted successfully", "success")
        return redirect(url_for("lesson.firstLessons", moduleId=moduleId))


    except ValueError as ve:
        logger.warning("Lesson deletion failed for id %s", lessonId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404



        flash(str(ve), "danger")

    except Exception as e:
        logger.warning("Unexpeccted error during lesson deletion for id: ", lessonId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 400
        



        flash("An unexpected error occured when trying to delete", "danger")

    return redirect(url_for("course.listCourses"))




        

    
