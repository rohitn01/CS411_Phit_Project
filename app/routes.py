from flask import render_template, request, jsonify, redirect
from app import app
from app import database as db_helper
from flask_cors import CORS
CORS(app)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    
    return render_template("index.html")

@app.route("/gyms", methods=['GET', 'POST'])
def gympage():
    print(request.method)
    if request.method == 'POST':
        gymname = request.form.get("gymname")
        print(gymname)
        university = request.form.get("university")
        print(university)
        items = db_helper.fetch_gyms(gymname, university)
        print("test")
        return render_template("gyms.html", items=items)
    else:
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