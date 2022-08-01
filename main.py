from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date

from flask_wtf import FlaskForm
from werkzeug import security
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_gravatar import Gravatar
from functools import wraps
from flask import abort
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6nzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar()

##CONNECT TO DB

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pujan", methods=["POST"])
def receive_data():
    name = request.form["username"]
    email = request.form["email"]
    additonal_details = request.form["additional-details"]
    try:
        budget = request.form["project-budget"]
        type_of_project = request.form['type-of-project']
    except:
        budget="nothing"

    # import pandas
    # import smtplib
    # import datetime as dt
    # import random as ra
    #
    # # CONSTANTS
    # MY_EMAIL = "gamingfury317@gmail.com"
    # MY_PASSWORD = 'sagarjadu770'
    # if not budget == "nothing":
    #     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         connection.sendmail(
    #             from_addr=MY_EMAIL,
    #             to_addrs="pujanvasania@gmail.com",
    #             msg=f"Subject:New project\n\nName - {name}\nEmail - {email}\nBudget - {budget}\nType of project - {type_of_project}\nAdditional Details={additonal_details}"
    #         )
    # else:
    #     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         connection.sendmail(
    #             from_addr=MY_EMAIL,
    #             to_addrs="pujanvasania@gmail.com",
    #             msg=f"Subject:New message for internship or timepass\n\nName - {name}\nEmail - {email}\nAdditional Details={additonal_details}"
    #         )

    return redirect(url_for("home"))


@app.route('/login',methods=['GET',"POST"])
def login():
    # error = None
    try :
        error = int(request.args.get("id"))
        print(error)
    except:
        error = 3


    return render_template("login.html",id=error)



if __name__ == "__main__":
    app.run(debug=True)
