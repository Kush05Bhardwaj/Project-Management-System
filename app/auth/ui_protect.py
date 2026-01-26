from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask import redirect

def ui_protect(role):
    def wrapper(fn):
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            identity = get_jwt_identity()
            user_role = identity.get('role')
            if user_role != role:
                return redirect('/ui/login')
            return fn(*args, **kwargs)
        return decorator
    return wrapper