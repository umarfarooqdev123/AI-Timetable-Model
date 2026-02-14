from app import app, db, Admin, Teacher, Department 
from werkzeug.security import generate_password_hash
from datetime import date

# ---------- Adding defalut Admin in DB --------------
def create_default_admin():
    with app.app_context():

        # Create tables first
        db.create_all()

        # Check if admin already exists
        existing_admin = Admin.query.filter_by(email="admin@timetable.com").first()

        if existing_admin:
            print("✅ Default admin already exists.")
            return

        # Create new admin
        admin = Admin(
            username="admin",
            email="admin@timetable.com",
            password_hash=generate_password_hash("admin123"),
            full_name="System Administrator",
            role="super_admin",
            is_active=True
        )

        db.session.add(admin)
        db.session.commit()

        print("✅ Default admin created successfully!")
        print("Email: admin@timetable.com")
        print("Password: admin123")

# ---------------- Adding default Teacher in DB ------------
def create_default_teacher():
    with app.app_context():

        # Create tables first
        db.create_all()

        # First, get a department to assign teacher to
        cs_dept = Department.query.filter_by(department_code="CS").first()
        
        if not cs_dept:
            print("❌ No department found! Please seed departments first.")
            return

        # Check if teacher already exists
        existing_teacher= Teacher.query.filter_by(email="teacher@uvas.edu.pk").first()

        if existing_teacher:
            print("✅ Default teacher already exists.")
            return

        # Create new teacher
        teacher = Teacher(
            employee_id="1234",
            username="teacher",
            email="teacher@uvas.edu.pk",
            password_hash=generate_password_hash("teacher123"),
            full_name="UVAS Teacher",
            designation="Lecturer",
            department_id=cs_dept.department_id,
            qualification="M.Sc. Computer Science",
            specialization="Web Development, Database Systems",
            experience_years=5,
            phone="+92-300-1234567",
            address="University of Veterinary and Animal Sciences, Lahore",
            max_weekly_hours=18,
            preferred_time_slots={"morning": True, "afternoon": True, "evening": False},
            is_active=True,
            join_date=date(2023, 1, 15)
        )

        db.session.add(teacher)
        db.session.commit()

        print("✅ Default teacher created successfully!")
        print("Email: teacher@uvas.edu.pk")
        print("Password: teacher123")


# --------- Adding Departments in DB -----------
def seed_departments():
    with app.app_context():
        depts = [
            {"code": "CS", "name": "Computer Science", "teachers": 4, "subjects": 8},
            {"code": "MLT", "name": "Medical Laboratory Technology", "teachers": 3, "subjects": 6}
        ]

        for d in depts:
            existing = Department.query.filter_by(department_code=d["code"]).first()
            if not existing:
                new_dept = Department(
                    department_code=d["code"],
                    department_name=d["name"],
                    total_teachers=d["teachers"],
                    total_subjects=d["subjects"]
                )
                db.session.add(new_dept)

        db.session.commit()
        print(" Departments added successfully!")



if __name__ == "__main__":
    create_default_admin()
    create_default_teacher()
    seed_departments()
