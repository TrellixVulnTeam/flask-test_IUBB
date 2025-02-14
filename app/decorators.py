from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permissions_required(permission):
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorator_function
    return decorator


def admin_required(f):
    return permissions_required(Permission.ADMINISTER)(f)
