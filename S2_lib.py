# (A) LOAD THE SQLITE MODULE
from os import curdir
from pickle import TRUE
from pickletools import read_string1
import sqlite3
from calendar import monthrange

DBFILLE = "DB/events.db"

# (B) SAVE EVENT
def save (start, end, txt, color, bg, id=None):
    # (B1) CONNECT
    conn = sqlite3.connect(DBFILLE)
    cursor = conn.cursor()

    # (B2) DATA $ SQL
    data = (start, end, txt, color, bg,)
    if id is None:
        sql = "INSERT INTO `events` (`start`, `end`, `text`, `color`, `bg`) VALUES (?,?,?,?,?)"
    else:
        sql = "UPDATE `events` SET `start`=?, `end`=?, `text`=?, `color`=?, `bg`=? WHERE `id`=?"
        data = data + (id,)
    
    # (B3) EXECUTE
    cursor.execute(sql, data)
    conn.commit
    conn.close
    return True

# (C) DELETE EVENT
def delete (id):
    # (C1) CONNECT
    conn = sqlite3.connect(DBFILLE)
    cursor = conn.cursor()

    # (C2) EXECUTE
    sql = "DELETE FROM `events` WHERE `id`=?"
    data = (id,)
    cursor.execute(sql, data)
    conn.commit()
    conn.close()
    return True

# (D) GET EVENTS
def get (month, year):
    # (D1) CONNECT
    conn = sqlite3.connect(DBFILLE)
    cursor = conn.cursor()

    # (D2) DATE RANGE CALCULATIONS
    daysInMonth = str(monthrange(year, month)[1])
    month = month if month>=10 else "0" + str(month)
    dateYM = str(year) + "-" + str(month) + "-"
    start = dateYM + "01 00:00:00"
    end = dateYM + daysInMonth + "23:59:59"

    # (D3) GET EVENTS
    sql = "SELECT * FROM `events` WHERE ((`start` BETWEEN ? AND ?) OR (`end` BETWEEN ? AND ?) OR (`start` <= ? AND `end` >= ?))"
    inputs = (start, end, start, end, start, end)
    cursor.execute(sql, inputs)
    rows = cursor.fetchall()
    if len(rows)==0:
        return None
    
    # s & e : start and end date
    # c & b : text and background color
    # t : event text

    data = {}
    for r in rows:
        data[r[0]] = {
            "s" : r[1],
            "e" : r[2],
            "t" : r[3],
            "c" : r[4],
            "b" : r[5]

        }
    return data







