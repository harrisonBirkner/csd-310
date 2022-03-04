# Harrison Birkner, 03/01/2022, Module 9.2 Assignment

# The purpose of this program is to connect to the pysports database, insert and delete rows from a table, and query multiple tables
# using a join to show the operations were done successfully.

import mysql.connector
from mysql.connector import errorcode

def connect():
    config = {
        "user": "pysports_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "pysports",
        "raise_on_warnings": True
    }

    try:
        db = mysql.connector.connect(**config) 

        print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        return db

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")

        else:
            print(err)

def select_and_print_players(cursor):
    SELECT_FROM_PLAYER_INNER_JOIN_TEAM_ON_TEAM_ID = ("SELECT p.player_id, p.first_name, p.last_name, t.team_name "
                                                     "FROM player p "
                                                     "INNER JOIN team t "
                                                     "ON p.team_id = t.team_id")
    cursor.execute(SELECT_FROM_PLAYER_INNER_JOIN_TEAM_ON_TEAM_ID)
    players = cursor.fetchall()
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

def main():


    db = connect()
    cursor = db.cursor()

    cursor.execute("INSERT INTO player (first_name, last_name, team_id) "
                      "VALUES('Smeagol', 'Shire Folk', 1)")
    db.commit()

    print("\n-- DISPLAYING PLAYERS AFTER INSERT --")
    select_and_print_players(cursor)

    cursor.execute("UPDATE player "
                      "SET team_id = 2, "
                          "first_name = 'Gollum', "
                          "last_name = 'Ring Stealer' "
                      "WHERE first_name = 'Smeagol'")
    db.commit()

    print("\n-- DISPLAYING PLAYERS AFTER UPDATE --")
    select_and_print_players(cursor)

    cursor.execute("DELETE FROM player "
                   "WHERE first_name = 'Gollum'")
    db.commit()

    print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
    select_and_print_players(cursor)

    db.close()

    input("\n\nPress any key to continue... ")

main()