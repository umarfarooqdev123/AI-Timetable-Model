from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = 'uvas_secret_key'

TEACHERS = {
    "ahmad@uvas.edu.pk": {"password": "ahmad", "full_name": "Dr. Ahmad"},
    "dr.ali@uvas.edu.pk": {"password": "dr.ali", "full_name": "Dr. Ali"}
}

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
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html", error="Incorrect Password")
        else:
            return render_template("login.html", error="User not found")
            
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    
    if "user_email" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/admin/dashboard")
def admin_dashboard():

    return render_template("admin_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)