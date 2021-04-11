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

@app.route("/progress", methods=['GET', 'POST'])
def progresspage():
    print(request.method)
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in gyms.html
        exercise = request.form.get("exercise")
        print(exercise)
        # call fetch_gyms with passed parameters and get query return list.
        items = db_helper.fetch_progress(exercise)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("progress.html", items=items)
    else:
        #If not POST req occurs, display all gyms to user
        items = db_helper.fetch_progress("")
        return render_template("progress.html", items=items)
    return render_template("progress.html")

@app.route("/findbuddies", methods=['GET', 'POST'])
def buddypage():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get("username")
        items = db_helper.fetch_buddies(username)
        print("test")
        return render_template("findbuddies.html", items=items)
    return render_template("findbuddies.html")

@app.route("/findmaxprogress", methods=['GET', 'POST'])
def maxpage():
    print(request.method)
    if request.method == 'POST':
        exercise = request.form.get("exercise")
        items = db_helper.fetch_progmax(exercise)
        print("test")
        return render_template("findmaxprogress.html", items=items)
    return render_template("findmaxprogress.html")

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

@app.route("/addprogress", methods=['GET', 'POST'])
def addprogpage():
    print(request.method)
    if request.method == 'POST':
        progressid = request.form.get("progressid")
        print(progressid)
        exercise = request.form.get("exercise")
        print(exercise)
        set_size = request.form.get("set_size")
        print(set_size)
        exercise_stat = request.form.get("exercise_stat")
        print(exercise_stat)
        db_helper.insert_new_progress(progressid, exercise, set_size, exercise_stat)
        return render_template("addprogress.html")
    return render_template("addprogress.html")

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

@app.route("/updateprogress", methods=['GET', 'POST'])
def updateprogpage():
    print(request.method)
    if request.method == 'POST':
        progressid = request.form.get("progressid")
        print(progressid)
        exercise = request.form.get("exercise")
        set_size = request.form.get("set_size")
        exercise_stat = request.form.get("exercise_stat")
        if len(exercise) > 0:
            db_helper.update_prog_exer(exercise, progressid)
        if len(set_size) > 0:
            db_helper.update_prog_set(set_size, progressid)
        if len(exercise_stat) > 0:
            db_helper.update_prog_stat(exercise_stat, progressid)
        return render_template("updateprogress.html")
    return render_template("updateprogress.html")

@app.route("/removegym", methods=['GET', 'POST'])
def removegympage():
    print(request.method)
    if request.method == 'POST':
        gymid = request.form.get("gymid")
        print(gymid)
        db_helper.remove_gym_by_id(gymid)
        return render_template("removegym.html")
    return render_template("removegym.html")


@app.route("/removeprogress", methods=['GET', 'POST'])
def removeprogpage():
    print(request.method)
    if request.method == 'POST':
        progressid = request.form.get("progressid")
        print(progressid)
        db_helper.remove_progress_by_id(progressid)
        return render_template("removeprogress.html")
    return render_template("removeprogress.html")