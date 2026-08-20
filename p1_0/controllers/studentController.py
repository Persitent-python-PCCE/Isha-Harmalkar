import logging
from flask import(
    Blueprint,  render_template,
    redirect,
    url_for,
    session,jsonify,
    request,
    flash
)




logger = logging.getLogger(__name__)

studentBp = Blueprint(
    "student",
    __name__
)


@studentBp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return f"<h1>Student Dashboard Placeholder</h1>"