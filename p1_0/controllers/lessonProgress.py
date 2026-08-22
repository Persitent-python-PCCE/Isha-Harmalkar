import logging
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    jsonify,
    request,
    flash
)

from dao.lessonProgressDao import LessonProgressDao
from services.lessonProgressService import LessonProgressService
from config.auth import wantsJson, loginRequired, roleRequired


logger = logging.getLogger(__name__)

lessonProgressBp = Blueprint("lessonProgress", __name__)
lessonProgressDao = LessonProgressDao()
lessonProgressService = LessonProgressService(lessonProgressDao)

@lessonProgressBp.route("/enrollments/<int:enrollmentId>/progress", methods=["GET"])
@roleRequired("student", "instructor", "admin")
def getProgress(enrollmentId):
    try:
        records = lessonProgressService.getProgressByEnrollmentId(enrollmentId)

        if wantsJson():
            return jsonify({
                "success": True,
                "progress": [record.toDict() for record in records]
            })

        return jsonify({
            "progress": [record.toDict() for record in records]
        })

    except Exception as e:
        logger.exception("Unexpected error fetching progress for enrollment %s", enrollmentId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 400

        flash("An unexpected error occurred", "danger")
        return redirect(url_for("course.listCourses"))


@lessonProgressBp.route(
    "/enrollments/<int:enrollmentId>/lessons/<int:lessonId>/complete",
    methods=["POST"]
)
@roleRequired("student")
def markLessonComplete(enrollmentId, lessonId):
    try:
        completed = request.get_json(silent=True) or {}
        progress = lessonProgressService.markLessonComplete(
            enrollmentId,
            lessonId,
            completed=completed.get("completed", True)
        )

        logger.info(
            "Lesson progress updated: enrollment=%s lesson=%s completed=%s",
            enrollmentId, lessonId, progress.completed
                            )
        return jsonify({
            "success": True,
            "message": "Progress updated",
            "progress": progress.toDict()
        })

    except ValueError as ve:
        logger.warning("Progress update failed for enrollment %s lesson %s",
                       enrollmentId, lessonId)

        return jsonify({
            "success": False,
            "message": str(ve)
        }), 400

    except Exception as e:
        logger.exception("Progress update failed for enrollment %s lesson %s",
                       enrollmentId, lessonId)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400
    
    