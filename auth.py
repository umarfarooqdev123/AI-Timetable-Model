from flask import Blueprint, session, redirect, url_for

# 1. Define the Blueprint
auth = Blueprint('auth', __name__)

# 2. The Logout Route
@auth.route('/logout')
def logout():
    session.clear() # Clear the session (Throw away badge)
    return redirect(url_for('login')) # Send them back to the Login page
