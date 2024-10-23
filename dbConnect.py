import sqlite3


def findLevelResult(gameAndKeymode, level):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("select result from level_mst where gameAndKeymode = ? and level = ?", (gameAndKeymode, level))
    row = cursor.fetchone()
    conn.close()
    return row[0]

def findMusicAndDifficulty(gameAndKeymode, level):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("select musicname, difficulty from tunes_mst where gameAndKeymode = ? and level = ?", (gameAndKeymode, level))
    row = cursor.fetchall()
    conn.close()
    return row

def insertInfo(name, phone, email, gameAndKeymode, musicname, difficulty, playstyle, condition1, condition2, condition3):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("insert into entry_mst(entry_name, entry_phone, entry_email, entry_gameAndKeymode, entry_musicname, entry_difficulty, entry_playstyle, entry_condition1, entry_condition2, entry_condition3) values(?,?,?,?,?,?,?,?,?,?)", (name, phone, email, gameAndKeymode, musicname, difficulty, playstyle, condition1, condition2, condition3))
    conn.commit()
    conn.close()