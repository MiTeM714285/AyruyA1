import sqlite3


def findLevelResult(gameAndKeymode, level):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("select result from level_mst where gameAndKeymode = ? and level = ?", (gameAndKeymode, level))
    row = cursor.fetchone()
    return row[0]

def findMusicAndDifficulty(gameAndKeymode, level):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("select musicname, difficulty from tunes_mst where gameAndKeymode = ? and level = ?", (gameAndKeymode, level))
    row = cursor.fetchall()
    return row
