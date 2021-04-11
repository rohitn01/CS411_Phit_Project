from flask import render_template, request, jsonify, redirect
from app import app
from app import database as db_helper
from flask_cors import CORS
CORS(app)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    
    return render_template("index.html")
# Flask route for gyms.html page. Executes as both GET/POST function
# When post request is passed, function will handle input from gyms.html and pass arguments into
# fetch_gyms() function to call select query to display search results on screen.
@app.route("/gyms", methods=['GET', 'POST'])
def gympage():
    print(request.method)
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in gyms.html
        gymname = request.form.get("gymname")
        print(gymname)
        university = request.form.get("university")
        print(university)
        # call fetch_gyms with passed parameters and get query return list.
        items = db_helper.fetch_gyms(gymname, university)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("gyms.html", items=items)
    else:
        #If not POST req occurs, display all gyms to user
        items = db_helper.fetch_gyms("", "")
        return render_template("gyms.html", items=items)
    return render_template("gyms.html")

@app.route("/findbuddies", methods=['GET', 'POST'])
def buddypage():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get("username")
        items = db_helper.fetch_buddies(username)
        print("test")
        return render_template("findbuddies.html", items=items)
    return render_template("findbuddies.html")

@app.route("/addgym", methods=['GET', 'POST'])
def addgympage():
    print(request.method)
    if request.method == 'POST':
        gymname = request.form.get("gymname")
        print(gymname)
        university = request.form.get("university")
        print(university)
        capacity = request.form.get("capacity")
        print(capacity)
        status = request.form.get("status")
        print(status)
        db_helper.insert_new_gym(gymname, university, capacity, status)
        return render_template("addgym.html")
    return render_template("addgym.html")

@app.route("/updategym", methods=['GET', 'POST'])
def updategympage():
    print(request.method)
    if request.method == 'POST':
        gymid = request.form.get("gymid")
        print(gymid)
        gymname = request.form.get("gymname")
        university = request.form.get("university")
        capacity = request.form.get("capacity")
        status = request.form.get("status")
        if len(gymname) > 0:
            db_helper.update_gym_name(gymname, gymid)
        if len(university) > 0:
            db_helper.update_gym_uni(university, gymid)
        if len(capacity) > 0:
            db_helper.update_gym_capacity(capacity, gymid)
        if len(status) > 0:
            db_helper.update_gym_status(status, gymid)
        return render_template("updategym.html")
    return render_template("updategym.html")

@app.route("/removegym", methods=['GET', 'POST'])
def removegympage():
    print(request.method)
    if request.method == 'POST':
        gymid = request.form.get("gymid")
        print(gymid)
        db_helper.remove_gym_by_id(gymid)
        return render_template("removegym.html")
    return render_template("removegym.html")

    @app.route("/users", methods=['GET', 'POST'])
def userpage():
    print(request.method)
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in users.html
        username = request.form.get("Username")
        print(username)
        university = request.form.get("University")
        print(university)
        # call fetch_users with passed parameters and get query return list.
        items = db_helper.fetch_users(username, university)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("users.html", items=items)
    else:
        #If not POST req occurs, display all gyms to user
        items = db_helper.fetch_users("", "")
        return render_template("users.html", items=items)
    return render_template("users.html")


@app.route("/adduser", methods=['GET', 'POST'])
def adduserpage():
    print(request.method)
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        print(firstname)
        lastname = request.form.get("lastname")
        print(lastname)
        email = request.form.get("email")
	    print(email)
	    university = request.form.get("university")
        print(university)
	    username = request.form.get("username")
        print(username)
	    password = request.form.get("password")
        print(password)
        covidstatus = request.form.get("covidstatus")
        print(covidstatus)
        db_helper.insert_new_user(firstname, lastname, email, university, username, password, covidstatus)
        return render_template("adduser.html")
    return render_template("adduser.html")

@app.route("/updateuser", methods=['GET', 'POST'])
def updateuserpage():
    print(request.method)
    if request.method == 'POST':
	email = request.form.get("email")
	print(email)
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
	university = request.form.get("university")
	username = request.form.get("username")
	password = request.form.get("password")
	covidstatus = request.form.get("covidstatus")
        if len(firstname) > 0:
            db_helper.update_user_fname(firstname, email)
        if len(lastname) > 0:
            db_helper.update_user_lname(lastname, email)
        if len(university) > 0:
            db_helper.update_user_uni(university, email)
        if len(username) > 0:
            db_helper.update_user_name(username, email)
        if len(password) > 0:
            db_helper.update_user_password(password, email)
        if len(covidstatus) > 0:
            db_helper.update_user_covidstatus(covidstatus, email)
        return render_template("updateuser.html")
    return render_template("updateuser.html")

@app.route("/removeuser", methods=['GET', 'POST'])
def removeuserpage():
    print(request.method)
    if request.method == 'POST':
        email = request.form.get("email")
        print(email)
        db_helper.remove_user_by_email(email)
        return render_template("deleteuser.html")
    return render_template("deleteuser.html")