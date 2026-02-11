from auth import auth
from flask import Flask, render_template, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'uvas_secret_key'

# 1. Configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/timetable_db"

# 2. Disable unnecessary tracking for better performance
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 3. Create database instance/object for better performance
db = SQLAlchemy(app)

def generate_uuid():
    return str(uuid.uuid4())

# Teacher Data (Temporary storage for login verification)
TEACHERS = {
    "teacher@uvas.edu.pk": {"name": "Dr.Fareed", "password": "fareed@21", "full_name": "Dr.Fareed"},
    "ali@uvas.edu.pk": {"name": "Dr.Ali", "password": "ali@21", "full_name": "Dr.Ali"}
}

# Register the Blueprint globally
app.register_blueprint(auth)

# ------------- Admin Table --------------------
class Admin(db.Model):
    _tablename_ = 'admins'

    admin_id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='admin')
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# -------------- Department Table --------------
class Department(db.Model):
    _tablename_ = 'departments'

    department_id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    department_code = db.Column(db.String(20), unique=True, nullable=False)
    department_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    hod_teacher_id = db.Column(db.String(36), db.ForeignKey('teachers.teacher_id'))
    total_teachers = db.Column(db.Integer, default=0)
    total_subjects = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# ------------- Teacher Table ------------------
class Teacher(db.Model):
    _tablename_ = 'teachers'

    teacher_id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.String(36), db.ForeignKey('departments.department_id'), nullable=False)
    qualification = db.Column(db.Text)
    specialization = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    max_weekly_hours = db.Column(db.Integer, default=18)
    preferred_time_slots = db.Column(db.JSON) # Store as JSON
    is_active = db.Column(db.Boolean, default=True)
    join_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Relationships
    subjects = db.relationship(
        'TeacherSubject',
        backref='teacher',
        lazy=True
    )

  # -------- Teacher_Subject Relation Table --------
class TeacherSubject(db.Model):
    _tablename_ = 'teacher_subjects'

    teacher_subject_id = db.Column(
        db.String(36),
        primary_key=True,
        default=generate_uuid
    )

    teacher_id = db.Column(
        db.String(36),
        db.ForeignKey('teachers.teacher_id'),
        nullable=False
    )

    subject_id = db.Column(
        db.String(36),
        db.ForeignKey('subjects.subject_id'),
        nullable=False
    )

    semester = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    weekly_hours = db.Column(db.Integer, nullable=False)
  

# ----------------- Subject Table ------------------
class Subject(db.Model):
    _tablename_ = 'subjects'

    subject_id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    subject_code = db.Column(db.String(20), unique=True, nullable=False)
    subject_name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.String(36), db.ForeignKey('departments.department_id'), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    total_hours = db.Column(db.Integer, nullable=False)
    hours_per_week = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer)
    year = db.Column(db.Integer)
    subject_type = db.Column(db.String(20), default='theory')
    prerequisite_subject_id = db.Column(db.String(36), db.ForeignKey('subjects.subject_id'))
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        # Relationships
    teachers = db.relationship(
        'TeacherSubject',
        backref='subject',
        lazy=True
    )
   

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/student_info")
def student_info():
    return render_template("student_info.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_input = request.form.get("username").strip()

        pass_input = request.form.get("password").strip()
        if email_input in TEACHERS:
            # Check if the password matches the email
            if TEACHERS[email_input]["password"] == pass_input:
                session["user_email"] = email_input
                session["user_name"] = TEACHERS[email_input]["full_name"]
                return redirect(url_for("Admin_dashboard"))
            else:
                return render_template("login.html", error="Incorrect Password")
        else:
            return render_template("login.html", error="User not found")
            
    return render_template("login.html")

@app.route("/Admin_dashboard")
def Admin_dashboard():
    # YOUR SECURITY CHECK:
    # "if user emailis NOT in the bag, go away!" 
    if "user_email" not in session:
        return redirect(url_for("login"))
    return render_template("Admin_dashboard.html")

@app.route("/Admin_dashboard/departments")
def departments():
    return render_template("departments.html")

if __name__ == "__main__":
    app.run(debug=True)