from flask import Blueprint, session, redirect, url_for, request
from functools import wraps

# 1. Define the Blueprint
auth = Blueprint('auth', __name__)

# --- ADMIN DECORATOR ---
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 1. Check if the user is logged in
        if 'user_id' not in session:
           # Send error message through URL
            return redirect(url_for('login', error="You must log in to access this page."))
        
        # 2.Check if user is an admin
        user_role = session.get('role')
        if user_role != "admin" and user_role != "super_admin":
            return redirect(url_for('login', error="Access Denied: You are not an admin."))
        return f(*args, **kwargs)
    return decorated_function

# 2. The Logout Route
@auth.route('/logout')
def logout():
    session.clear() # Clear the session (Throw away badge)
    return redirect(url_for('login')) # Send them back to the Login page
