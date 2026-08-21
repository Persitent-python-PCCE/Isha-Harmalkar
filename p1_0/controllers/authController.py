import logging
from flask import(
    Blueprint,  render_template,
    redirect,
    url_for,
    session,jsonify,
    request,
    flash
)

from forms.authForms import(
    RegisterForm,
    LoginForm
)

from config.auth import wantsJson

from services.userService import UserService

logger = logging.getLogger(__name__)

authBp = Blueprint(
    "auth",
    __name__
)

userService = UserService()

@authBp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = userService.register(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data
            )
            logger.info("User resgistered successfully: %s", form.email.data)

            if wantsJson():
                return jsonify({
                    "success": True,
                    "message": "Registration successfull",
                    "user": 
                       user.toDict()
                    
                }), 201

            flash(
                "Registration succesful. Please Login",
                "success"

            )
            return redirect(
                url_for("auth.login")
            )


        except ValueError as ve:
            logger.warning("registration validation failed for %s"
            , form.email.data)
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(ve)
                }), 400
            flash(str(ve), "danger")

        except Exception as e:
            logger.exception("Unexpected error during user registration for %s.", form.email.data)
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": str(e)
                }), 400
            flash("An unexpected error occured", "danger")

    if request.method == "POST" and wantsJson():
        logger.warning("Form validation failed on register: %s", form.errors)
        return jsonify({
            "success": False,
            "errors": form.errors
        }), 400

    return render_template(
        "register.html",
        form=form
    )


@authBp.route(
        "/login",
        methods=["GET", "POST"]
)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = userService.authenticate(
            form.email.data,
            form.password.data
        )

        if not user:
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": "Invlaid email or password"
                }), 401

            flash(
                "Invalid email or password",
                "danger"
            )

            return render_template(
                "login.html",
                form=form
            )

        session.clear()
        session["user_id"] = user.id
        session["role"] = user.role.role_name

        if wantsJson():
            return jsonify({

                "success": True,
                "message": "Login successful",
                "user": 
                   user.toDict()
                
            })

        if user.role.role_name == "admin":
            return redirect(
                url_for("admin.dashboard")
            )

        if user.role.role_name == "instructor":
            return redirect(
                url_for("instructor.dashboard")
            )

        return redirect(
            url_for("student.dashboard")
        )

    if request.method == "POST" and wantsJson():
        return jsonify({
            "success": False,
            "errors": form.errors
        }), 400

    return render_template(
        "login.html",
        form=form
    )

@authBp.route("/logout")
def logout():
    session.clear()
    if wantsJson():
        return jsonify({
            "success": True,
            "message": "Logged Out"

        })

    return redirect(
        url_for("auth.login")
    )


