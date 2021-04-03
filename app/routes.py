from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:gym_id>", methods=['POST'])
def delete(gym_id):
     try:
        # db_helper.remove_gym_by_id(gym_id)
        result = {'success': True, 'response': 'Removed Gym'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/edit/<int:gym_id>", methods=['POST'])
def update(gym_id):
    data = request.get_json()
		print(data)
    try:
        if "Status" in data:
            # db_helper.update_status_entry(gym_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "GymName" in data:
            # db_helper.update_gym_entry(gym_id, data["description"])
            result = {'success': True, 'response': 'Gym Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    # db_helper.insert_new_gym(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_gyms()
    return render_template("index.html", items=items)