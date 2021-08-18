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

app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_product_offers")
def get_product_offers():
    product_offers = mongo.db.product_offers.find()
    return render_template("offers.html", product_offers=product_offers)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


def allowed_logo(filename):
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_logo_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/business_signup", methods=["GET", "POST"])
def business_signup():
    # business logo saved to mongodb
    # if "logo" in request.files:
    #     logo = request.files["logo"]
    #     mongo.save_file(logo.filename, logo)

    if request.method == "POST":

        existing_email = mongo.db.business_users.find_one(
            {"business_email_address": request.form.get("business_email_address").lower()})

        if existing_email:
            flash("Email Address already in use")
            return redirect(url_for("business_signup"))

        if request.files:
            logo = request.files["logo"]

            if "filesize" in request.cookies:

                if not allowed_logo_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(url_for("business_signup"))

            if logo.filename == '':
                print("No filename. Please name file and try again")
                return redirect(url_for("business_signup"))

            if allowed_logo(logo.filename):
                # filename = secure_filename(logo.filename)
                mongo.save_file(secure_filename(logo.filename), logo)
                print("Logo saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for("business_signup"))

        business_signup = {
            "business_name": request.form.get("business_name"),
            "signers_name": request.form.get("sign_up_name"),
            "industry": request.form.get("industry"),
            "business_address_line_1": request.form.get("business_address_line_1"),
            "business_address_line_2": request.form.get("business_address_line_2"),
            "business_address_line_3": request.form.get("business_address_line_3"),
            "business_contact_number": request.form.get("business_contact_number"),
            "business_email_address": request.form.get("business_email_address"),
            "facebook": request.form.get("facebook"),
            "instagram": request.form.get("instagram"),
            "twitter": request.form.get("twitter"),
            "website_url": request.form.get("website_url"),
            "logo_img": logo.filename,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.business_users.insert_one(business_signup)

        session["business_user"] = request.form.get("business_name")
        flash("Business Sign Up Successful")

    return render_template("business_signup.html")


@app.route("/consumer_signup", methods=["GET", "POST"])
def consumer_signup():
    if request.method == "POST":

        existing_email = mongo.db.consumer_users.find_one(
            {"consumer_email_address": request.form.get("consumer_email_address").lower()})

        if existing_email:
            flash("Email Address already in use")
            return redirect(url_for("consumer_signup"))

        consumer_signup = {
            "consumer_name": request.form.get("consumer_name"),
            "consumer_address_line_1": request.form.get("consumer_address_line_1"),
            "consumer_address_line_2": request.form.get("consumer_address_line_2"),
            "consumer_address_line_3": request.form.get("consumer_address_line_3"),
            "consumer_contact_number": request.form.get("consumer_contact_number"),
            "consumer_email_address": request.form.get("consumer_email_address"),
            "consumer_dob": request.form.get("consumer_dob"),
            "consumer_password": generate_password_hash(request.form.get("consumer_password"))
        }
        mongo.db.consumer_users.insert_one(consumer_signup)

        session["consumer_user"] = request.form.get("consumer_name")
        flash("Consumer Sign Up Successful")

    return render_template("consumer_signup.html")


@app.route("/upload_logo", methods=["GET", "POST"])
def upload_logo():
    return render_template("upload_logo.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
