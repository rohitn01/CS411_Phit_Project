from app import db

def fetch_gyms() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Gyms;").fetchall()
    conn.close()
    gyms_list = []
    for result in query_results:
        item = {
            "GymID": result[0],
            "GymName": result[1],
            "University": result[2],
            "Capacity": result[3],
            "Status": result[4]
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