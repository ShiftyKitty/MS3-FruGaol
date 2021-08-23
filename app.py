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
@app.route("/offers")
def offers():
    offers = mongo.db.offers.find()
    return render_template("offers.html", offers=offers)
    

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")
    

def allowed_img(filename):
    if "." not in filename:
        return False
        
    ext = filename.rsplit(".", 1)[1]
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
        

def allowed_img_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False
        

@app.route("/business_signup", methods=["GET", "POST"])
def business_signup():
    if request.method == "POST":
        # business logo saved to mongodb
        if request.files:
            logo = request.files["logo"]
            
            if "filesize" in request.cookies:
                
                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("business_signup"))
       
            if logo.filename == '':
                flash("No filename. Please name file and try again")
                return redirect(url_for("business_signup"))
                
            if allowed_img(logo.filename):
                mongo.save_file(secure_filename(logo.filename), logo)
                print("Logo saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for("business_signup"))
                
        # check if business_name already exists in db
        existing_user = mongo.db.business_users.find_one(
            {"business_name": request.form.get("business_name").lower()})
            
        if existing_user:
            flash("business_name already exists")
            return redirect(url_for("business_signup"))
            
        business_signup = {
            "business_name": request.form.get("business_name").lower(),
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

        # put the new user into 'session' cookie
        session["user"] = request.form.get("business_name").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", business_name=session["user"]))

    return render_template("business_signup.html")

# @app.route("/consumer_signup", methods=["GET", "POST"])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if business_name exists in db
        existing_user = mongo.db.business_users.find_one(
            {"business_name": request.form.get("business_name").lower()})
            
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("business_name").lower()
                    flash("Welcome, {}".format(
                        request.form.get("business_name")))
                    return redirect(url_for(
                        "profile", business_name=session["user"]))
                
            else:
                # invalid password match
                flash("Incorrect business_name and/or Password")
                return redirect(url_for("login"))
                
        else:
            # business_name doesn't exist
            flash("Incorrect business_name and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


@app.route("/profile/<business_name>", methods=["GET", "POST"])
def profile(business_name):
    # grab the session user's business_name from db
    business_name = mongo.db.business_users.find_one(
        {"business_name": session["user"]})["business_name"]

    business_users = mongo.db.business_users.find()
    return render_template("profile.html", business_users=business_users)

    if session["user"]:
        return render_template("profile.html", business_name=business_name)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_offer", methods=["GET", "POST"])
def create_offer():
    if request.method == "POST":
        # business offer img saved to mongodb
        if request.files:
            offer_img = request.files["offer_img"]
            
            if "filesize" in request.cookies:
                
                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("create_offer"))
       
            if offer_img.filename == '':
                flash("No filename. Please name file and try again")
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
            "offer_description": request.form.get("offer_description"),
            "offer_price": request.form.get("offer_price"),
            "offer_img": offer_img.filename,
            "created_by": session["user"]
        }

        mongo.db.offers.insert_one(offer)
        flash("Offer Successfully Created")
        return redirect(url_for("create_offer"))

    return render_template("create_offer.html")


@app.route("/edit_offer/<offer_id>", methods=["GET", "POST"])
def edit_offer(offer_id):
     if request.method == "POST":
        # business offer img saved to mongodb
        if request.files:
            offer_img = request.files["offer_img"]
            
            if "filesize" in request.cookies:
                
                if not allowed_img_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit")
                    return redirect(url_for("create_offer"))
       
            if offer_img.filename == '':
                flash("No filename. Please name file and try again")
                return redirect(url_for("create_offer"))
                
            if allowed_img(offer_img.filename):
                mongo.save_file(secure_filename(offer_img.filename), offer_img)
                print("Offer Image saved")
            else:
                flash("That file extension is not permitted")
                return redirect(url_for("create_offer"))

        edit = {
            "offer_name": request.form.get("offer_name"),
            "offer_type": request.form.get("offer_type"),
            "offer_description": request.form.get("offer_description"),
            "offer_price": request.form.get("offer_price"),
            "offer_img": offer_img.filename,
            "created_by": session["user"]
        }

        mongo.db.offers.update({"_id": ObjectId(offer_id)}, edit)
        flash("Offer Successfully Edited")

    offer = mongo.db.offers.find_one({"_id": ObjectId(offer_id)})
    return render_template("edit_offer.html", offer=offer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
