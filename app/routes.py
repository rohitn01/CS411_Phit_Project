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

#Physical Data
@app.route("/PhysicalData", methods=['GET', 'POST'])
def PhysicalDataPage():
    print(request.method)
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in gyms.html
        Username = request.form.get("Username")
        print(Username)
        # call fetch_gyms with passed parameters and get query return list.
        items = db_helper.fetchPhysicalData(Username)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("PhysicalData.html", items=items)
    else:
        #If not POST req occurs, display all gyms to user
        items = db_helper.fetch_gyms("")
        return render_template("PhysicalData.html", items=items)
    return render_template("PhysicalData.html")

@app.route("/findReservations", methods=['GET', 'POST'])
def reservationsPage():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get("username")
        items = db_helper.getAvailibleReservations(username)
        print("test")
        return render_template("findReservations.html", items=items)
    return render_template("findReservations.html")

@app.route("/addPhysicalData", methods=['GET', 'POST'])
def addPhysicalDataPage():
    #Username, LastMuscleGroup, Injury, LastRecorded, WorkSplit
    print(request.method)
    if request.method == 'POST':
        Username = request.form.get("Username")
        print(Username)
        lastMuscleGroup= request.form.get("LastMuscleGroup")
        print(lastMuscleGroup)
        injury = request.form.get("Injury")
        print(injury)
        lastRecorded = request.form.get("LastRecorded")
        print(lastRecorded)
        workSplit = request.form.get("WorkSplit")
        print(workSplit)
        db_helper.insert_new_gym(Username, lastMuscleGroup, injury, lastRecorded, workSplit)
        return render_template("addPhysicalData.html")
    return render_template("addgym.html")