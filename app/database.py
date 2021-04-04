from app import db

def fetch_gyms(gymname: str, university: str) -> dict:
    conn = db.connect()
    query = 'SELECT GymName, University, Capacity, Status FROM Gyms WHERE GymName = "{0}" OR University = "{1}" ORDER BY University ASC, GymName ASC;'.format(gymname, university)
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
