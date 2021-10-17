import os
from functools import wraps
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


# -- GLOBAL FUNCTIONS --
def user_find():
    """
    Get the current user using the username value of the current session
    user, returning the current user as a dict.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    return current_user


def admin_user():
    """ Check to see if user in session is admin """
    admin = mongo.db.users.find_one(
            {"username": "admin".lower()})
    return admin


def id_find():
    """
    Get the ObjectId value of the current user, returning it as
    a string value
    """
    user_id = str(user_find()['_id'])
    return user_id


# Decorators explained
# https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required
def admin_required(function):
    """
    Decorator function that uses the admin_user() function above. Ensures
    that a user has admin privileges to access the wrapped function.
    """
    @wraps(function)
    def wrap(*args, **kwargs):
        if admin_user():
            return function(*args, **kwargs)
        else:
            flash("You do not have admin privileges")
            return redirect(url_for("get_recipes"))
    return wrap


def login_required(function):
    """
    Decorator function ensuring that user is in session before accessing the
    wrapped function.
    """
    @wraps(function)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return function(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for("login"))
    return wrap

# ------


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """ Returns list of recipes from database """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Build query function to show the search page and results """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
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

        mongo.db.users.insert_one({
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        })

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
@login_required
def profile(username):
    """ Render profile page based on logged in session user """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    """ Remove session cookies from user """
    flash("Logged out Successfully")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
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
            "cook_time": request.form.get("cook_time"),
            "username": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """ Update recipe record in database """
    if request.method == "POST":
        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "image": request.form.get("image"),
            "description": request.form.get("description"),
            "cuisine_type": request.form.get("cuisine_type"),
            "servings": request.form.get("servings"),
            "prep_time": request.form.get("prep_time"),
            "prep_steps": request.form.getlist("prep_steps"),
            "ingredients": request.form.getlist("ingredients"),
            "cook_time": request.form.get("cook_time"),
            "username": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, cuisines=cuisines)


@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """ Remove recipe record from database, based on recipe_id """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_cuisines")
def get_cuisines():
    """ Returns list of cuisines from database in ascending order """
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_type", 1))
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
@admin_required
def add_cuisine():
    """
    Allows admin to add a new cuisine in the DB.
    Check whether a cuisine with the same name already exist before
    saving new cuisine.
    """
    if user_find() == admin_user():

        if request.method == "POST":
            existing_cuisine = mongo.db.cuisines.find_one(
                {"cuisine_type": request.form.get("cuisine_type").lower()})

            if existing_cuisine:
                flash("Cuisine Already Exists")
                return redirect(url_for("add_cuisine"))

            cuisine = {
                "cuisine_type": request.form.get("cuisine_type").lower(),
                "image": request.form.get("image")
            }

            mongo.db.cuisines.insert_one(cuisine)
            flash("New Cuisine Added")
            return redirect(url_for("get_cuisines", username=session["user"]))

        return render_template("add_cuisine.html")

    return render_template("login.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
@admin_required
def edit_cuisine(cuisine_id):
    """ Allows admin user to edit existing cuisine data in the database. """
    if request.method == "POST":
        submit = {
            "cuisine_type": request.form.get("cuisine_type"),
            "image": request.form.get("image")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/delete_cuisine/<cuisine_id>")
@admin_required
def delete_cuisine(cuisine_id):
    """ Allows admin user to delete cuisine data from the database. """
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("get_cuisines"))


@app.errorhandler(404)
def not_found(error):
    """ Return custom 404 page when page is not found """
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    """ Return custom 500 page when an error occurs """
    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
