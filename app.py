import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_product_offers")
def get_product_offers():
    product_offers = mongo.db.product_offers.find()
    return render_template("offers.html", product_offers=product_offers)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


@app.route("/business_signup", methods=["GET", "POST"])
def business_signup():
    return render_template("business_signup.html")


@app.route("/consumer_signup", methods=["GET", "POST"])
def consumer_signup():
    return render_template("consumer_signup.html")


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    return render_template("upload_image.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)