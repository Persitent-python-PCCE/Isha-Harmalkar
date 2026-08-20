from functools import wraps
from flask import request, session, redirect, url_for, jsonify


def loginRequired(view):
    @wraps(view)
    def wrappedView(*args, **kwargs):
        if "user_id" not in session:
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": "Authentication required"
                }), 401

            return redirect(url_for("login"))

        return view(*args, **kwargs)

    return wrappedView

def roleRequired(*allowedParams):
    def decorator(view):
        @wraps(view)
        def wrappedView(*args, **kwargs):
            if "user_id" not in session:
                if wantsJson():
                    return jsonify({
                        "success": False,
                        "message": "Authentication reuqired"
                    }), 401

                return redirect(url_for("login"))

            role = session.get("role")

            if role not in allowedRoles:
                if wantsJson():
                    return jsonify({
                        "success": False,
                        "message": "Access Denied"
                    }), 403

                return "Forbidden", 403
            return  view(*args, **kwargs)

        return wrappedView



def wantsJson():
    return (
        "application/json"
        in request.accept_mimetypes
    )
                

