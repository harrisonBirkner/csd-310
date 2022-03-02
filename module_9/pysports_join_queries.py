# Harrison Birkner, 03/01/2022, Module 9.2 Assignment

#The purpose of this program is to connect to the pysports database, query multiple tables using an inner join, and print the data returned

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

def main():
    db = connect()

    cursor = db.cursor()

    cursor.execute("SELECT p.player_id, p.first_name, p.last_name, t.team_name "
                    "FROM player p "
                    "INNER JOIN team t "
                    "ON p.team_id = t.team_id")

    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

    db.close()

    input("\n\nPress any key to continue... ")

main()