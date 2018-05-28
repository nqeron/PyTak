import TakMove
import Symmetry
import sqlite3

games_db = sqlite3.connect("games_anon.db")
cursor = games_db.cursor()
cursor.execute("SELECT notation FROM games WHERE size = 5")
for notation in cursor.fetchall():
    notation = notation[0]
    moves = notation.split(",")
    moves_ptn = []
    for move in moves:
        move_ptn = TakMove.parse_server_move(move)  ##.lower()
        moves_ptn.append(move_ptn)
    moves_ptn = Symmetry.standardize(moves_ptn, 5)
    print(moves_ptn)

#print(cursor.fetchall()[5])
games_db.close()
