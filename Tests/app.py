from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")

# Database URI from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    item_condition = db.Column(db.String(50))
    listing_type = db.Column(db.String(50))
    price = db.Column(db.Float)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_submit():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    role = request.form["role"]

    try:
        new_user = User(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password=password,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return f"User {username} added! <a href='/signup'>Add another</a> or <a href='/'>Go Home</a>"
    except Exception as e:
        return f"Error: {e}. <a href='/signup'>Try again</a>"

@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("signin.html")

@app.route("/signin", methods=["POST"])
def signin_submit():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return f"Welcome back, {username}! <a href='/'>Go Home</a>"
    else:
        return "Invalid username or password. <a href='/signin'>Try again</a>"

@app.route("/admin", methods=["GET"])
def admin_dashboard():
    try:
        users = User.query.all()
        items = Item.query.all()
        return render_template("adminpage.html", users=users, items=items)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
