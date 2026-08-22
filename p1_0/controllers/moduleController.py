import logging
from flask import(
    Blueprint,
    render_template,
    redirect,
    url_for,
    jsonify,
    request,
    flash
)
from forms.moduleForms import ModuleForm
from dao.moduleDao import ModuleDao
from models import module
from services.moduleService import ModuleService
from config.auth import wantsJson, loginRequired, roleRequired

logger = logging.getLogger(__name__)
moduleBp = Blueprint("module", __name__)
moduleDao = ModuleDao()
moduleService = ModuleService(moduleDao)


@moduleBp.route("/courses/<int:courseId>/modules", methods=["GET"])
@loginRequired
def listModules(courseId):
    modules  = moduleService.getModuleByCourseId(courseId)
    if wantsJson():
        return jsonify({
            "success": True,
            "modules": [module.toDict() for module in modules]
        })

    return render_template("module_list.html", modules=modules, courseId=courseId)


@moduleBp.route("/courses/<int:courseId>/modules", methods=["GET","POST"])
@roleRequired("admin")
def createModule(courseId):
    form = ModuleForm()

    if form.validate_on_submit():
        try:
            module = moduleService.createModule(
                courseId,
                moduleName=form.moduleName.data,
                description=form.description.data
            )

            logger.info("Module created successfully: %s", module.module_name)

            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Module created successfully",
                    "module": module.toDict()
                }), 201


            flash("Module created successfully", "success")
            return redirect(url_for("module.listModules", courseId=courseId))

        except ValueError as ve:
            logger.warning("Module creation validation failed")
            if wantsJson():
                return jsonify({"success": False, "message":str(ve)}), 400

            flash(str(ve), "danger")

        except Exception as e:
            logger.exception("Unexcpected error during module creation")
            if wantsJson():
                return jsonify({"success": False, "message": str(e)}), 400
            flash("An unexpected error occured", "danger")

        if request.method == "POST" and wantsJson():
            return jsonify({
                "success": False,
                "errors": form.errors
            }), 400


        return render_template("moduleForm.html", form=form, courseId=courseId)


@moduleBp.route("/modules/<int:moduleId>/update", methods=["GET", "POST"])
@roleRequired("admin")
def updateModule(moduleId):
    form = ModuleForm()

    if form.validate_on_submit():
        try:
            module = module.Service.updateModule(
                moduleId,
                moduleName=form.moduleName.data,
                description=form.description.data
            )
            logger.info("Module updated successfully: %s",module.module_name)


            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Module updated successfully",
                    "module": module.toDict()
                })

            flash("Module updated successfully", "success")
            return redirect(url_for("module.listModules", courseId=module.course_id))

        except ValueError as ve:
            logger.warning("Module update validation failed for id %s", moduleId)
            if wantsJson():
                return jsonify({"success": False, "message": str(ve)}), 400
            flash(str(ve), "danger")

        except Exception as e:
            logging.exception("Unexpected error during module update for id %s", moduleId)
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


@moduleBp.route("/modules/<int:moduleId>/delete", methods=["POST"])
@roleRequired("admin")
def deleteModule(moduleId):
    try:
        module = moduleService.getModuleById(moduleId)
        courseId = module.course_id
        moduleService.deleteModule(moduleId)
        logger.info("Module deleted successfully: %s", moduleId)

        if wantsJson():
            return jsonify({
                "success": True,
                "message": "Module deleted successfully"
            })

        flash("Module deleted successfully", "success")

    except ValueError as ve:
        logger.warning("Module delete failed for id %s", moduleId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(ve)
            }), 404

        flash(str(ve), "danger")

    except Exception as e:
        logger.exception("Unexpected error during module deletion for id %s", moduleId)
        if wantsJson():
            return jsonify({
                "success": False,
                "message": str(e)
            }), 400

        flash("An unexpected error occured", "danger")

    return redirect(url_for("course.listCourses"))