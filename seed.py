from app import app, db, Admin
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


if __name__ == "__main__":
    create_default_admin()
