from functools import wraps
from flask import request, session, redirect, url_for, jsonify


def loginRequired(viewFunction):
    @wraps(viewFunction)
    def wrappedView(*args, **kwargs):
        if "user_id" not in session:
            if wantsJson():
                return jsonify({
                    "success": False,
                    "message": "Authentication required"
                }), 401

            return redirect(url_for("auth.login"))

        return viewFunction(*args, **kwargs)

    return wrappedView

def roleRequired(*allowedRoles):
    def decorator(viewFunction):
        @wraps(viewFunction)
        def wrappedView(*args, **kwargs):
            if "user_id" not in session:
                if wantsJson():
                    return jsonify({
                        "success": False,
                        "message": "Authentication reuqired"
                    }), 401

                return redirect(url_for("auth.login"))

            currentRole = session.get("role")

            if currentRole not in allowedRoles:
                if wantsJson():
                    return jsonify({
                        "success": False,
                        "message": "Access Denied"
                    }), 403

                return "Forbidden", 403
            return  viewFunction(*args, **kwargs)

        return wrappedView
    return decorator




def wantsJson():
    return request.is_json or  request.accept_mimetypes.best == "application/json"


        
