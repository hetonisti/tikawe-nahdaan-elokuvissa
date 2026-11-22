import sqlite3
from flask import g
from datetime import datetime

def get_connection():
    con = sqlite3.connect("database.db")
    #con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id

def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def add_event(movie, location, showtime, users, tags=[], *new_tag):
    created_on = datetime.now().strftime("%Y-%m-%dT%H%M")

    sql_event = """INSERT INTO Events 
        (movie, location, showtime, created_on) 
        VALUES (?, ?, ?, ?)"""
    sql_new_tag = "INSERT INTO Tags (tag) VALUES (?)"
    sql_user = "INSERT INTO Seeings (event_id, user_id) VALUES (?, ?)"
    sql_tag = "INSERT INTO Taggings (tag_id, event_id, user_id) VALUES (?, ?, ?)"
    sql_can_modify = "INSERT INTO Can_modify_event (event_id, user_id) VALUES (?, ?)"
    con = get_connection()
    if new_tag and new_tag != "": #TODO: joku ongelma että lisätään tyhjä new tag
        r = con.execute(sql_new_tag, [new_tag[0]])
        new_tag_id = r.lastrowid
        tags.append(new_tag_id)

    result = con.execute(sql_event, [movie, location, showtime, created_on])
    event_id = result.lastrowid
    print(f"event id {event_id}")
    for u in users:
        con.execute(sql_user, [event_id, u])
    for t in tags:
        con.execute(sql_tag, [t, event_id, users[0]])
    con.execute(sql_can_modify, [event_id, users[0]])
    try: 
        con.commit()
    except Exception as err:
        con.close()
        raise Exception(f"Virhe. Virheen tyyppi: {type(err)}")
    con.close()