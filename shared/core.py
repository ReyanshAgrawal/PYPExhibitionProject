import json
import os

DB_FILE = "db.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"flags": {}, "pledges": {}}, f)

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_flag(flag_name, value):
    data = read_db()
    data["flags"][flag_name] = value
    write_db(data)

def get_flag(flag_name):
    data = read_db()
    return data["flags"].get(flag_name, False)

def add_pledge(user_id, pledge_text):
    data = read_db()
    data["pledges"][user_id] = pledge_text
    write_db(data)

def get_all_pledges():
    data = read_db()
    return data["pledges"]

print(get_flag("site_open"))