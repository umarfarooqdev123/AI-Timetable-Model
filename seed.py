from app import app, db, Admin, Department 
from werkzeug.security import generate_password_hash


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
    seed_departments()
