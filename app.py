import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """ Returns list of recipes from database """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Insert new user into db """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get(
            "password") != request.form.get("password-confirm"):
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log in existing user and redirect to custom profile view"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("The Username and Password do not match.")
                return redirect(url_for("login"))

        else:
            flash("The Username and Password do not match.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ Render profile page based on logged in session user """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Remove session cookies from user """
    flash("Logged out Successfully")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """ Insert new recipe to database """
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "image": request.form.get("image"),
            "description": request.form.get("description"),
            "cuisine_type": request.form.get("cuisine_type"),
            "servings": request.form.get("servings"),
            "prep_time": request.form.get("prep_time"),
            "prep_steps": request.form.getlist("prep_steps"),
            "ingredients": request.form.getlist("ingredients"),
            "username": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return render_template("add_recipe.html", cuisines=cuisines)


@app.errorhandler(404)
def not_found(error):
    """ Return custom 404  page when page is not found """
    return render_template('404.html')


@app.errorhandler(500)
def internal_error(error):
    """ Return custom 500 page when an error occurs """
    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
