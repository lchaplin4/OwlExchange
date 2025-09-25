from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mountain_123",
    database="OwlExchange"
)
cursor = db.cursor()

# Serve index page
@app.route("/")
def index():
    return render_template("index.html")

# Serve signup page
@app.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")

# Handle signup form submission
@app.route("/signup", methods=["POST"])
def signup_submit():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]

    try:
        cursor.execute(
            "INSERT INTO users (firstname, lastname, username, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)",
            (firstname, lastname, username, email, password, role)
        )
        db.commit()
        return f"User {username} added! <a href='/signup'>Add another</a> or <a href='/'>Go Home</a>"
    except mysql.connector.IntegrityError:
        return f"Error: Username {username} already exists. <a href='/signup'>Try again</a>"

# Serve signin page
@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("signin.html")

# Handle signin form submission
@app.route("/signin", methods=["POST"])
def signin_submit():
    username = request.form["username"]
    password = request.form["password"]

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    result = cursor.fetchone()

    if result:
        return f"Welcome back, {username}! <a href='/'>Go Home</a>"
    else:
        return "Invalid username or password. <a href='/signin'>Try again</a>"

# Serve admin dashboard page
@app.route("/admin", methods=["GET"])
def admin_dashboard():
    # Fetch all users with all attributes
    cursor.execute("SELECT id, firstname, lastname, username, email, role FROM users")
    users = cursor.fetchall()

    # Fetch all items (with proper column names from DB)
    cursor.execute("SELECT id, owner_id, name, description, item_condition, listing_type, price FROM items")
    items = cursor.fetchall()

    return render_template("adminpage.html", users=users, items=items)

if __name__ == "__main__":
    app.run(debug=True)
