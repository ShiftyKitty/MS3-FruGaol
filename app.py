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
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "JFIF", "WEBP"]


mongo = PyMongo(app)


# offers/homepage
@app.route("/")
@app.route("/offers")
def offers():
    offers = list(mongo.db.offers.find())
    return render_template("offers.html", offers=offers)


# signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


# img type check. taken from flask
def allowed_img(filename):
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


# img filesize check. taken from flask
def allowed_img_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


# business signup. file security from flask official docs
@app.route("/business_signup", methods=["GET", "POST"])
def business_signup():
    if request.method == "POST":
        # business logo saved to mongodb
        if request.files:
            logo = request.files["logo"]

            if "filesize" in request.cookies:

                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Logo file too big. Must be under 500KB")
                    return redirect(url_for("business_signup"))

            if logo.filename == '':
                flash(
                    "No Business Logo Detected. Please add Logo and try again")
                return redirect(url_for("business_signup"))

            if ' ' in logo.filename:
                flash(
                    "Please remove all gaps from Logo filename and try again")
                return redirect(url_for("business_signup"))

            if allowed_img(logo.filename):
                filename = secure_filename(logo.filename)
                mongo.save_file(filename, logo)
                print("Logo saved")
            else:
                flash("File extension not permitted. Please try again.")
                return redirect(url_for("business_signup"))

        # check if business_name already exists in db
        existing_user = mongo.db.business_users.find_one(
            {"business_name": request.form.get("business_name").upper()})

        if existing_user:
            flash(
                "Business Name already exists. Please try again.")
            return redirect(url_for("business_signup"))

        business_signup = {
            "business_name": request.form.get("business_name").upper(),
            "signers_name": request.form.get("signers_name"),
            "industry": request.form.get("industry"),
            "business_address_line_1": request.form.get(
                "business_address_line_1"),
            "business_address_line_2": request.form.get(
                "business_address_line_2"),
            "business_address_line_3": request.form.get(
                "business_address_line_3"),
            "business_contact_number": request.form.get(
                "business_contact_number"),
            "business_email_address": request.form.get(
                "business_email_address").lower(),
            "facebook": request.form.get("facebook"),
            "instagram": request.form.get("instagram"),
            "twitter": request.form.get("twitter"),
            "website_url": request.form.get("website_url"),
            "business_description": request.form.get("business_description"),
            "prodserv_1": request.form.get("prodserv_1"),
            "prodserv_2": request.form.get("prodserv_2"),
            "prodserv_3": request.form.get("prodserv_3"),
            "logo_img": logo.filename,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.business_users.insert_one(business_signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("business_name").upper()
        flash("Registration Successful!")
        return redirect(url_for("profile", business_name=session["user"]))

    return render_template("business_signup.html")


# consumer signup
@app.route("/consumer_signup", methods=["GET", "POST"])
def consumer_signup():
    if request.method == "POST":
        # profile pic saved to mongodb
        if request.files:
            profile_pic = request.files["profile_pic"]

            if "filesize" in request.cookies:

                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("consumer_signup"))

            if ' ' in profile_pic.filename:
                flash(
                    "Please remove all gaps from Profile filename")
                return redirect(url_for("consumer_signup"))

            if allowed_img(profile_pic.filename):
                mongo.save_file(
                    secure_filename(profile_pic.filename), profile_pic)
                print("Profile Pic saved")

        # check if existing_consumer already exists in db
        existing_consumer = mongo.db.consumer_users.find_one(
            {"consumer_email_address": request.form.get(
                "consumer_email_address").lower()})

        if existing_consumer:
            flash("Consumer email already exists. Please try again")
            return redirect(url_for("consumer_signup"))

        consumer_user = {
            "consumer_name": request.form.get("consumer_name"),
            "consumer_address_line_1": request.form.get(
                "consumer_address_line_1"),
            "consumer_address_line_2": request.form.get(
                "consumer_address_line_2"),
            "consumer_address_line_3": request.form.get(
                "consumer_address_line_3"),
            "consumer_contact_number": request.form.get(
                "consumer_contact_number"),
            "consumer_email_address": request.form.get(
                "consumer_email_address").lower(),
            "consumer_dob": request.form.get("consumer_dob"),
            "profile_pic": profile_pic.filename,
            "consumer_password": generate_password_hash(request.form.get(
                "consumer_password"))
        }
        mongo.db.consumer_users.insert_one(consumer_user)

        # put the new consumer into 'session' cookie
        session["consumer"] = request.form.get(
            "consumer_email_address").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "consumer_profile", consumer_email_address=session["consumer"]))

    return render_template("consumer_signup.html")


# file upload. code from pretty printed. referenced in readme
@app.route("/file/<filename>")
def file(filename):
    return mongo.send_file(filename)


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if business_name exists in db
        existing_user = mongo.db.business_users.find_one(
            {"business_name": request.form.get("business_name").upper()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("business_name").upper()
                flash("Welcome, {}".format(request.form.get("business_name")))
                return redirect(url_for(
                    "offers", business_name=session["user"]))

            else:
                # invalid password match
                flash("Incorrect business_name and/or Password")
                return redirect(url_for("login"))

        else:
            # business_name doesn't exist
            flash("Incorrect business_name and/or Password")
            return redirect(url_for("login"))

        # consumer login
        existing_consumer = mongo.db.consumer_users.find_one(
            {"consumer_email_address": request.form.get(
                "consumer_email_address").lower()})

        if existing_consumer:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["consumer_password"], request.form.get(
                    "consumer_password")):
                session["consumer"] = request.form.get(
                    "consumer_email_address").lower()
                return redirect(url_for(
                    "offers", consumer_email_address=session["consumer"]))

            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # business_name doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# consumer login
@app.route("/consumer_login", methods=["GET", "POST"])
def consumer_login():
    if request.method == "POST":
        # consumer login
        existing_consumer = mongo.db.consumer_users.find_one(
            {"consumer_email_address": request.form.get(
                "consumer_email_address").lower()})

        if existing_consumer:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_consumer["consumer_password"], request.form.get(
                    "consumer_password")):
                session["consumer"] = request.form.get(
                    "consumer_email_address").lower()
                return redirect(url_for(
                    "offers", consumer_email_address=session["consumer"]))

            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("consumer_login"))

        else:
            # business_name doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("consumer_login"))

    return render_template("login.html")


# business profile session user
@app.route("/profile/<business_name>/", methods=["GET", "POST"])
def profile(business_name):
    # grab the session user's business_name from db
    business_name = mongo.db.business_users.find_one(
        {"business_name": session["user"]})["business_name"]

    business_users = mongo.db.business_users.find()

    if session["user"]:
        return render_template("profile.html", business_name=business_name,
                               business_users=business_users)

    return redirect(url_for("login"))


# edit business profile
@app.route("/edit_profile/<business_name>/", methods=["GET", "POST"])
def edit_profile(business_name):
    if request.method == "POST":
        # business logo saved to mongodb
        if request.files:
            logo = request.files["logo"]

            if "filesize" in request.cookies:

                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for(
                        "edit_profile", business_name=business_name))

            if logo.filename == '':
                flash("No filename. Please name file and try again")
                return redirect(url_for(
                    "edit_profile", business_name=business_name))

            if ' ' in logo.filename:
                flash(
                    "Please remove all gaps from Logo filename and try again")
                return redirect(url_for(
                    "edit_profile", business_name=business_name))

            if allowed_img(logo.filename):
                mongo.save_file(secure_filename(logo.filename), logo)
                print("Logo saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for(
                    "edit_profile", business_name=business_name))

        # check if business_name already exists in db
        edit_details = {
            "business_name": session["user"],
            "signers_name": request.form.get("signers_name"),
            "industry": request.form.get("industry"),
            "business_address_line_1": request.form.get(
                "business_address_line_1"),
            "business_address_line_2": request.form.get(
                "business_address_line_2"),
            "business_address_line_3": request.form.get(
                "business_address_line_3"),
            "business_contact_number": request.form.get(
                "business_contact_number"),
            "business_email_address": request.form.get(
                "business_email_address"),
            "facebook": request.form.get("facebook"),
            "instagram": request.form.get("instagram"),
            "twitter": request.form.get("twitter"),
            "website_url": request.form.get("website_url"),
            "business_description": request.form.get("business_description"),
            "prodserv_1": request.form.get("prodserv_1"),
            "prodserv_2": request.form.get("prodserv_2"),
            "prodserv_3": request.form.get("prodserv_3"),
            "logo_img": logo.filename,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.business_users.update(
            {"business_name": session["user"]}, edit_details)
        flash("Profile Successfully Edited")

    business_name = mongo.db.business_users.find_one(
        {"business_name": session["user"]})
    return render_template("edit_profile.html", business_name=business_name)


# consumer profile
@app.route("/consumer_profile/<consumer_email_address>",
           methods=["GET", "POST"])
def consumer_profile(consumer_email_address):
    # consumer profile deetz
    consumer_email_address = mongo.db.consumer_users.find_one(
        {"consumer_email_address": session["consumer"]})

    consumer_users = mongo.db.consumer_users.find()

    if session["consumer"]:
        return render_template("consumer_profile.html",
                               consumer_email_address=consumer_email_address,
                               consumer_users=consumer_users)

    return redirect(url_for("login"))


# business profile public view
@app.route("/business_profile/<business_name>", methods=["GET", "POST"])
def business_profile(business_name):
    # grab the business info for customers from db
    business_users = mongo.db.business_users.find()
    business_name = mongo.db.business_users.find_one(
        {"business_name": business_name})["business_name"]

    return render_template("business_profile.html",
                           business_name=business_name,
                           business_users=business_users)


# logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")

    return redirect(url_for("login"))


# consumer logout
@app.route("/consumer_logout")
def consumer_logout():
    # remove consumer from session cookies
    flash("You have been logged out")
    session.pop("consumer")

    return redirect(url_for("login"))


# create offer
@app.route("/create_offer", methods=["GET", "POST"])
def create_offer():
    if request.method == "POST":
        # offer img saved to mongodb
        if request.files:
            offer_img = request.files["offer_img"]

            if "filesize" in request.cookies:

                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("create_offer"))

            if offer_img.filename == '':
                flash(
                    "No Offer Image Detected. Please add Image and try again")
                return redirect(url_for("create_offer"))

            if ' ' in offer_img.filename:
                flash(
                    "Please remove all gaps from Image filename and try again")
                return redirect(url_for("create_offer"))

            if allowed_img(offer_img.filename):
                mongo.save_file(secure_filename(offer_img.filename), offer_img)
                print("Offer Image saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for("create_offer"))

        offer = {
            "offer_name": request.form.get("offer_name"),
            "offer_type": request.form.get("offer_type"),
            "offer_category": request.form.get("offer_category"),
            "offer_description": request.form.get("offer_description"),
            "old_price": request.form.get("old_price"),
            "offer_price": request.form.get("offer_price"),
            "offer_img": offer_img.filename,
            "created_by": session["user"]
        }

        mongo.db.offers.insert_one(offer)
        flash("Offer Successfully Created")
        return redirect(url_for("offers"))

    return render_template("create_offer.html")


# offer profile
@app.route("/offer/<offer_id>", methods=["GET", "POST"])
def offer(offer_id):
    # grab the offer id from db
    offers = mongo.db.offers.find()
    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})
    reviews = mongo.db.reviews.find()
    consumer_users = mongo.db.consumer_users.find()

    return render_template("offer.html", offer=offer, offers=offers,
                           reviews=reviews, consumer_users=consumer_users)


# my offers
@app.route("/my_offers/<business_name>", methods=["GET", "POST"])
def my_offers(business_name):
    # grab the session user's business_name from db
    business_name = mongo.db.business_users.find_one(
        {"business_name": session["user"]})["business_name"]

    offers = mongo.db.offers.find()

    if session["user"]:
        return render_template(
            "my_offers.html", business_name=business_name, offers=offers)

    return render_template(
        "my_offers.html", offers=offers, business_name=business_name)


# edit offer
@app.route("/edit_offer/<offer_id>", methods=["GET", "POST"])
def edit_offer(offer_id):
    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})
    if request.method == "POST":
        # offer img saved to mongodb
        if request.files:
            offer_img = request.files["offer_img"]

            if "filesize" in request.cookies:

                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("edit_offer"))

            if offer_img.filename == '':
                flash(
                    "No Offer Image Detected. Please add Image and try again")
                return render_template("edit_offer.html", offer=offer)

            if ' ' in offer_img.filename:
                flash(
                    "Please remove all gaps from Image filename and try again")
                return render_template("edit_offer.html", offer=offer)

            if allowed_img(offer_img.filename):
                mongo.save_file(secure_filename(offer_img.filename), offer_img)
                print("Offer Image saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for("edit_offer"))

        edit = {
            "offer_name": request.form.get("offer_name"),
            "offer_type": request.form.get("offer_type"),
            "offer_category": request.form.get("offer_category"),
            "offer_description": request.form.get("offer_description"),
            "old_price": request.form.get("old_price"),
            "offer_price": request.form.get("offer_price"),
            "offer_img": offer_img.filename,
            "created_by": session["user"]
        }

        mongo.db.offers.update({"_id": ObjectId(offer_id)}, edit)
        flash("Offer Successfully Edited")

    return render_template("edit_offer.html", offer=offer)


# offer finish/delete
@app.route("/offer_finish/<offer_id>")
def offer_finish(offer_id):
    mongo.db.offers.remove({"_id": ObjectId(offer_id)})
    flash("Offer Finished")
    return redirect(url_for("offers"))


# create review
@app.route("/create_review/<offer_id>", methods=["GET", "POST"])
def create_review(offer_id):
    if request.method == "POST":
        # business offer img saved to mongodb
        offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})

        reviews = mongo.db.reviews.find()

        consumer_user = mongo.db.consumer_users.find()

        customer_review = {
            "created_by": session["consumer"],
            "offer_id": offer_id,
            "rate": request.form.get("rate"),
            "consumer_review": request.form.get("consumer_review")
        }

        mongo.db.reviews.insert_one(customer_review)
        flash("Review Submitted")
        return redirect(url_for("offer", offer=offer, offer_id=offer_id,
                                reviews=reviews, consumer_user=consumer_user))

    return render_template("offer.html")


# search offers
@app.route("/search_offers", methods=["GET", "POST"])
def search_offers():
    query = request.form.get("query")
    offers = list(mongo.db.offers.find({"$text": {"$search": query}}))

    return render_template("offers.html", offers=offers, query=query)


# edit consumer profile
@app.route("/edit_consumer_profile/<consumer_email_address>",
           methods=["GET", "POST"])
def edit_consumer_profile(consumer_email_address):
    if request.method == "POST":
        # profile pic saved to mongodb
        profile_pic = request.files["profile_pic"]

        if "filesize" in request.cookies:

            if not allowed_img_filesize(request.cookies["filesize"]):
                flash("Filesize exceeded maximum limit")
                return redirect(url_for("edit_consumer_profile",
                                consumer_email_address=consumer_email_address))

        if ' ' in profile_pic.filename:
            flash("Please remove all gaps from Profile filename and try again")
            return redirect(url_for("edit_consumer_profile",
                            consumer_email_address=consumer_email_address))

        if allowed_img(profile_pic.filename):
            mongo.save_file(secure_filename(
                profile_pic.filename), profile_pic)
            print("Profile Pic saved")

        edit_details = {
            "consumer_name": request.form.get("consumer_name"),
            "consumer_address_line_1": request.form.get(
                "consumer_address_line_1"),
            "consumer_address_line_2": request.form.get(
                "consumer_address_line_2"),
            "consumer_address_line_3": request.form.get(
                "consumer_address_line_3"),
            "consumer_contact_number": request.form.get(
                "consumer_contact_number"),
            "consumer_email_address": request.form.get(
                "consumer_email_address").lower(),
            "consumer_dob": request.form.get("consumer_dob"),
            "profile_pic": profile_pic.filename,
            "consumer_password": generate_password_hash(request.form.get(
                "consumer_password"))
        }

        mongo.db.consumer_users.update(
            {"consumer_email_address": session["consumer"]}, edit_details)
        flash("Profile Successfully Edited")

    consumer_email_address = mongo.db.consumer_users.find_one(
        {"consumer_email_address": session["consumer"]})

    return render_template("edit_consumer_profile.html",
                           consumer_email_address=consumer_email_address)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
