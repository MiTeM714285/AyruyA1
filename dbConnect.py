import sqlite3


def findLevelResult(gameAndKeymode, level):
    conn = sqlite3.connect('DB/ayruya.db3')
    cursor = conn.cursor()
    cursor.execute("select result from level_mst where gameAndKeymode = ? and level = ?", (gameAndKeymode, level))
    row = cursor.fetchone()
    return row[0]
