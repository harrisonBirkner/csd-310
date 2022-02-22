#Harrison Birkner, 02/21/2022, Module 8.3 Assignment

#The purpose of this program is to connect to the pysports database, query multiple tables, and print the data returned

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

        print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        return db

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)

def main():
    db = connect()
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM team")
    teams = cursor.fetchall()
    
    cursor.execute("SELECT * FROM player")
    players = cursor.fetchall()

    print("\n-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    print("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    db.close()

    input("\n\nPress any key to continue... ")

main()