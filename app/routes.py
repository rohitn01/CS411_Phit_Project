from flask import render_template, request, jsonify, redirect, session, url_for, abort, g
from app import app
from app import database as db_helper
from flask_cors import CORS
CORS(app)
'''
class User:
    def __init__(self, username, password, email, ):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'
'''
app.secret_key = 'datadummies69'
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = session['user_id']
        g.user = user

@app.route("/")
def indexpage():
    return redirect(url_for('loginpage'))

@app.route("/home")
def homepage():
    """ returns rendered homepage """
    if not g.user:
        return redirect(url_for('loginpage'))
    print(g.user)
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def loginpage():
    session.pop('user_id', None)
    g.user = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = db_helper.check_login(username, password)
        if verify == 1:
            session['user_id'] = username
            return redirect(url_for('homepage'))
        return redirect(url_for('loginpage'))

    return render_template("login.html")

@app.route("/signup")
def signuppage():
    return render_template("index.html")

# Flask route for gyms.html page. Executes as both GET/POST function
# When post request is passed, function will handle input from gyms.html and pass arguments into
# fetch_gyms() function to call select query to display search results on screen.

# STORED PROCEDURE PAGE
@app.route("/userstats", methods=['GET'])
def statpage():
    print(request.method)
    print(g.user)
    if not g.user:
        return redirect(url_for('loginpage'))
    items = db_helper.fetch_stats(g.user)
    return render_template("userstats.html", items=items)


@app.route("/gyms", methods=['GET', 'POST'])
def gympage():
    print(request.method)
    print(g.user)
    if not g.user:
        return redirect(url_for('loginpage'))
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
    if not g.user:
        return redirect(url_for('loginpage'))
    username = g.user
    items = db_helper.fetch_buddies(username)

    return render_template("findbuddies.html", items=items)

@app.route("/addgym", methods=['GET', 'POST'])
def addgympage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
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
    if not g.user:
        return redirect(url_for('loginpage'))
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
@app.route("/updategym/<GymID>", methods=['GET', 'POST'])
def updategymwid(GymID):
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        gymname = request.form.get("gymname")
        university = request.form.get("university")
        capacity = request.form.get("capacity")
        status = request.form.get("status")
        if len(gymname) > 0:
            db_helper.update_gym_name(gymname, GymID)
        if len(university) > 0:
            db_helper.update_gym_uni(university, GymID)
        if len(capacity) > 0:
            db_helper.update_gym_capacity(capacity, GymID)
        if len(status) > 0:
            db_helper.update_gym_status(status, GymID)
        return render_template("updategym.html")
    return render_template("updategym.html")

@app.route("/removegym/<GymID>", methods=['GET', 'POST', 'DELETE'])
def removegympage(GymID):
    print(request.method)
    print(GymID)
    if not g.user:
        return redirect(url_for('loginpage'))
    db_helper.remove_gym_by_id(GymID)
    return redirect(url_for('gympage'))

#Physical Data
@app.route("/PhysicalData", methods=['GET', 'POST'])
def PhysicalDataPage():
    print(request.method)
    print(g.user)
    if not g.user:
        return redirect(url_for('loginpage'))
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in gyms.html
        mg = request.form.get("LastMuscleGroup")
        print(mg)
        # call fetch_gyms with passed parameters and get query return list.
        items = db_helper.fetchPhysicalData(g.user, mg)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("PhysicalData.html", items=items)
    else:
        #If not POST req occurs, display all gyms to user
        items = db_helper.fetchPhysicalData(g.user, "")
        return render_template("PhysicalData.html", items=items)
    return render_template("PhysicalData.html")

@app.route("/findReservations", methods=['GET', 'POST'])
def reservationsPage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    username = g.user
    items = db_helper.getAvailibleReservations(username)
    return render_template("findReservations.html", items=items)

@app.route("/findReservations/<GymID>", methods=['GET', 'POST'])
def gymReservationsPage(GymID):
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    items = db_helper.getGymReservations(GymID)
    return render_template("findReservations.html", items=items)

@app.route("/makereservation/<ReservationID>", methods=['GET', 'POST'])
def makereservationPage(ReservationID):
    if not g.user:
        return redirect(url_for('loginpage'))
    username = g.user
    db_helper.update_reservation(username, ReservationID)
    return redirect(url_for('reservationsPage'))

@app.route("/myreservations", methods=['GET', 'POST'])
def myreservationsPage():
    if not g.user:
        return redirect(url_for('loginpage'))
    items = db_helper.fetch_my_reservations(g.user)
    return render_template("myreservations.html", items=items)

@app.route("/cancelreservation/<ReservationID>", methods=['GET', 'POST'])
def cancelreservationPage(ReservationID):
    if not g.user:
        return redirect(url_for('loginpage'))
    db_helper.cancel_reservation(ReservationID)
    return redirect(url_for('myreservationsPage'))

@app.route("/addPhysicalData", methods=['GET', 'POST'])
def addPhysicalDataPage():
    #Username, LastMuscleGroup, Injury, LastRecorded, WorkSplit
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        lastMuscleGroup= request.form.get("LastMuscleGroup")
        print(lastMuscleGroup)
        injury = request.form.get("Injury")
        print(injury)
        lastRecorded = request.form.get("LastRecorded")
        print(lastRecorded)
        workSplit = request.form.get("WorkSplit")
        print(workSplit)
        db_helper.insertNewPhysicalData(g.user, lastMuscleGroup, injury, lastRecorded, workSplit)
        return render_template("addPhysicalData.html")
    return render_template("addPhysicalData.html")

@app.route("/updatePhysicalData", methods=['GET', 'POST'])
def updatePDpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        lastMuscleGroup = request.form.get("LastMuscleGroup")
        injury = request.form.get("Injury")
        lastRecorded = request.form.get("LastRecorded")
        workSplit = request.form.get("WorkSplit")
        if len(lastMuscleGroup) > 0:
            db_helper.updatePhysicalDataLastMuscleGroup(g.user, lastMuscleGroup)
        if len(injury) > 0:
            db_helper.updatePhysicalDataInjury(g.user, injury)
        if len(lastRecorded) > 0:
            db_helper.updatePhysicalDataLastRecorded(g.user, lastRecorded)
        if len(workSplit) > 0:
            db_helper.updatePhysicalDataWorkSplit(g.user, workSplit)
        return render_template("updatePhysicalData.html")
    return render_template("updatePhysicalData.html")

@app.route("/removePhysicalData", methods=['GET', 'POST'])
def removePDpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        Username = request.form.get("Username")
        print(Username)
        db_helper.removePhysicalDataByUsername(Username)
        return render_template("removePhysicalData.html")
    return render_template("removePhysicalData.html")

    # PROGRESS

@app.route("/progress", methods=['GET', 'POST'])
def progresspage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in gyms.html
        exercise = request.form.get("exercise")
        print(exercise)
        # call fetch_gyms with passed parameters and get query return list.
        items = db_helper.fetch_progress(exercise, g.user)
        print("test")
        # return rendered template of gyms.html with list as items
        return render_template("progress.html", items=items)
        #If not POST req occurs, display all gyms to user
    items = db_helper.fetch_progress("", g.user)
    return render_template("progress.html", items=items)

@app.route("/findmaxprogress", methods=['GET', 'POST'])
def maxpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        exercise = request.form.get("exercise")
        username = g.user
        items = db_helper.fetch_progmax(exercise, username)
        print("test")
        return render_template("findmaxprogress.html", items=items)
    return render_template("findmaxprogress.html")

@app.route("/addprogress", methods=['GET', 'POST'])
def addprogpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        exercise = request.form.get("exercise")
        print(exercise)
        set_size = request.form.get("set_size")
        print(set_size)
        exercise_stat = request.form.get("exercise_stat")
        print(exercise_stat)
        db_helper.insert_new_progress(g.user, exercise, set_size, exercise_stat)
        return redirect(url_for('progresspage'))
    return render_template("addprogress.html")

@app.route("/updateprogress", methods=['GET', 'POST'])
def updateprogpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
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

@app.route("/removeprogress", methods=['GET', 'POST'])
def removeprogpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        progressid = request.form.get("progressid")
        print(progressid)
        db_helper.remove_progress_by_id(progressid)
        return render_template("removeprogress.html")
    return render_template("removeprogress.html")


#USERS

@app.route("/users", methods=['GET', 'POST'])
def userpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    # Check if it is a post req
    if request.method == 'POST':
        # collect gymname and university information from search bar(s) in users.html
        username = request.form.get("username")
        print(username)
        university = request.form.get("university")
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


@app.route("/addusers", methods=['GET', 'POST'])
def adduserpage():
    print(request.method)
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        print(firstname)
        lastname = request.form.get("lastname")
        print(lastname)
        email = request.form.get("email")
        university = request.form.get("university")

        username = request.form.get("username")
        password = request.form.get("password")
        print(password)
        covidstatus = request.form.get("covidstatus")
        print(covidstatus)
        db_helper.insert_new_user(firstname, lastname, email, university, username, password, covidstatus)
        return redirect(url_for('loginpage'))
    return render_template("addusers.html")

@app.route("/updateusers", methods=['GET', 'POST'])
def updateuserpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        university = request.form.get("university")
        newpass = request.form.get("newpassword")
        repass = request.form.get("repassword")
        password = request.form.get("password")
        covidstatus = request.form.get("CovidStatus")

        verify = db_helper.check_login(g.user, password)
        print(verify)
        if verify != 1:
            return render_template("updateusers.html")
        if len(firstname) > 0:
            db_helper.update_user_fname(firstname, g.user)
        if len(lastname) > 0:
            db_helper.update_user_lname(lastname, g.user)
        if len(university) > 0:
            db_helper.update_user_uni(university, g.user)
        if len(newpass) > 0 and len(repass) > 0:
            if(newpass != repass):
                return render_template("updateusers.html")
            db_helper.update_user_password(newpass, g.user)
        if len(covidstatus) > 0:
            db_helper.update_user_covidstatus(covidstatus, g.user)
        return redirect(url_for('homepage'))
    return render_template("updateusers.html")

@app.route("/deleteuser", methods=['GET', 'POST'])
def removeuserpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        password = request.form.get("password")
        repass = request.form.get("password2")
        if(password != repass):
            return render_template("deleteuser.html")
        db_helper.remove_user_by_email(g.user)
        return redirect(url_for('loginpage'))
    return render_template("deleteuser.html")

@app.route("/findliftrecord", methods=['GET', 'POST'])
def liftpage():
    print(request.method)
    if not g.user:
        return redirect(url_for('loginpage'))
    if request.method == 'POST':
        exercise = request.form.get("exercise")
        items = db_helper.fetch_lift_records(exercise)
        print("test")
        return render_template("findliftrecord.html", items=items)
    return render_template("findliftrecord.html")