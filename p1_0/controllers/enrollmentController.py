import logging
from flask import(
    Blueprint,
    render_template,
    redirect,
    session,
    url_for,
    jsonify,
    request,
    flash
)


from dao.enrollmentDao import EnrollmentDao
from dao.courseInstructorDao import CourseInstructorDao
from services.enrollmentService import EnrollmentService
from config.auth import wantsJson, loginRequired, roleRequired

logger = logging.getLogger(__name__)
enrollmentBp = Blueprint("enrollment", __name__)

enrollmentDao = EnrollmentDao()
courseInstructorDao = CourseInstructorDao()
enrollmentService = EnrollmentService(enrollmentDao, courseInstructorDao)

@enrollmentBp.route("/enrollments", methods=["GET"])
@roleRequired("student")
def listMyEnrollments():
    studentId = session["user_id"]
    enrollments = enrollmentService.getEnrollmentsByStudentId(studentId)

    if wantsJson():
        return jsonify({
            "success": True,
            "enrollments": [enrollment.toDict() for enrollment in enrollments]
        })

    return jsonify({
        "enrollments": [enrollment.toDict() for enrollment in enrollments]
    })



@enrollmentBp.route("/courseInstructors/<int:courseInstructorId>/enroll", methods=["POST"])
@roleRequired("student")
def enroll(courseInstructorId):
    studentId = session["user_id"]


    try:
        enrollment = enrollmentService.enrollStudent(studentId, courseInstructorId)
        logger.info("Student %s enrolled via course-instructor %s", studentId, courseInstructorId)

        if wantsJson():
            return jsonify({
                "success": True,
                "message": "Enrolled Successfully",
                "enrollment": enrollment.toDict()
            }), 201

        flash("Enrolled successfully", "success")
        return redirect(url_for("enrollment.listMyEnrollments"))

    
    except ValueError as ve:
        logger.warning("Enrollment failed for student %s: %s", studentId, str(ve))
        if wantsJson():
            return jsonify({"success": False, "message": str(ve)}), 400

        flash(str(ve), "danger")

        return redirect(url_for("course.listCourses"))


    except Exception as e:
        logger.exception("Unexpected error enrolling student %s", studentId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 400

        flash("An unexpected error occurred", "danger")
        return redirect(url_for("course.listCourses"))


@enrollmentBp.route("/courseInstrucotrs/<int:courseInstructorId>/enrollments", methods=["GET"])
@roleRequired("admin", "instructor")
def listEnrollmentsForOffering(courseInstructorId):
    enrollments = enrollmentService.getEnrollmentByCourseInstructorId(courseInstructorId)
    if wantsJson():
        return jsonify({
            "success": True,
            "enrollments": [enrollment.toDict() for enrollment in enrollments]
        
        })

    return jsonify({
        "enrollments": [enrollment.toDict() for enrollment in enrollments]
    })


@enrollmentBp.route("/enrollments/<int:enrollmentId>/status", methods=["POST"])
@roleRequired("admin", "instructor", "student")
def updateStatus(enrollmentId):
    payload  = request.get_json(silent=True) or request.forms
    status = payload.get("status")

    try:
        enrollment = enrollmentService.updateStatus(enrollmentId, status)
        logger.info("Enrollment %s status updated to %s", enrollmentId, status)

        return jsonify({
            "success": True,
            "message": "Status updated",
            "enrollment": enrollment.toDict()
        })

    except ValueError as ve:
        logger.warning("Status update failed for enrollment %s", enrollmentId)
        return jsonify({
            "success": False,
            "message": str(ve)
        }), 400

    except Exception as e:
        logging.exception("Unexpected error updating status for enrollment %s", enrollmentId)
        return jsonify({
            "success": False,
            "message": str(ve)
        }), 400

    except Exception as e:
        logger.exception("Unexpected error updating status for enrollment %s", enrollmentId)
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400


@enrollmentBp.route("/enrollments/<int:enrollmentId>/uneroll", methods=["POST"])
@roleRequired("admin", "student")
def unenroll(enrollmentId):
    try:
        enrollmentService.unenrollStudent(enrollmentId)
        logger.info("Enrollment %s removed", enrollmentId)

        if wantsJson():
            return jsonify({
                "success": True,
                "message": "Unenrolled successfully"
            })

        flash("Unenrolled successfully", "success")

    except ValueError as ve:
        logger.warning("Uneroll failed for id %s", enrollmentId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404

        flash(str(ve), "danger")

    except Exception as e:
        logger.exception("Unexpected error unerolling %s", enrollmentId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 400

        flash("An unexpected error occurred", "danger")

    return redirect(url_for("enrollment.listMyEnrollments"))