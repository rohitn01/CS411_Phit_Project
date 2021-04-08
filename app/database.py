from app import db
from sqlalchemy.sql import text
def fetch_gyms(gymname: str, university: str) -> dict:
    conn = db.connect()
    if len(gymname) > 0 and len(university) > 0:
        statement = 'SELECT GymName, University, Capacity, Status FROM Gyms WHERE GymName LIKE "%{0}%" OR University LIKE "%{1}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(gymname, university)
    elif len(gymname) > 0:
        statement = 'SELECT GymName, University, Capacity, Status FROM Gyms WHERE GymName LIKE "%{0}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(gymname)
    elif len(university) > 0:
        statement = 'SELECT GymName, University, Capacity, Status FROM Gyms WHERE University LIKE "%{0}%" ORDER BY Status DESC, University ASC, GymName ASC;'.format(university)
    else:
        statement = 'SELECT GymName, University, Capacity, Status FROM Gyms ORDER BY Status DESC, University ASC, GymName ASC;'
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    gyms_list = []
    for result in query_results:
        item = {
            "GymName": result[0],
            "University": result[1],
            "Capacity": result[2],
            "Status": result[3]
        }
        gyms_list.append(item)
    return gyms_list

def fetch_buddies(username: str) -> dict:
    conn = db.connect()
    if len(gymname) > 0 and len(university) > 0:
        statement = ''
    query = text(statement)
    print(query)
    query_results = conn.execute(query).fetchall()
    conn.close()
    gyms_list = []
    for result in query_results:
        item = {
            "FirstName": result[0],
            "LastName": result[1],
            "Email": result[2],
            "Username": result[3],
            "StartTime": result[4],
            "EndTime": result[5],
            "Day": result[6],
            "Month": result[7],
            "Year": result[8],
        }
        gyms_list.append(item)
    return gyms_list
  
def update_gym_name(GymID: int, text: str) -> None:
    conn = db.connect()
    query = 'Update Gyms set GymName = "{}" where GymID = {};'.format(text, GymID)
    conn.execute(query)
    conn.close()

def update_gym_uni(GymID: int, text: str) -> None:
    conn = db.connect()
    query = 'Update Gyms set University = "{}" where GymID = {};'.format(text, GymID)
    conn.execute(query)
    conn.close()

def update_gym_status(GymID: int, text:str) -> None:
    conn = db.connect()
    query = 'Update Gyms set Status = "{}" where GymID = {};'.format(text, GymID)
    conn.execute(query)
    conn.close()


def insert_new_gym(GymName: str, University: str, Capacity: int, Status: str):
    conn = db.connect()
    query = 'Insert Into Gyms (GymName, University, Capacity, Status) VALUES ("{}", "{}", "{}", "{}");'.format(GymName, University, Capacity, Status)
    conn.execute(query)
    conn.close()

def remove_gym_by_id(GymID: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Gyms where GymID={};'.format(GymID)
    conn.execute(query)
    conn.close()
