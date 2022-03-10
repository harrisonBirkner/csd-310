# Harrison Birkner, 3/9/2022, Module 11.2 & 12.3 Assignment

# The purpose of this program is to provide a ui for users to access various functions of the whatabook book store, including viewing all books, stores, user's wishlists,
# available books for wishlist, and adding books to the wishlist. There is also validation to keep bad data from being entered at any point in the program.

import mysql.connector
from mysql.connector import errorcode

def connect():
# this function is for connecting to the database and is only needed once at the beginning of the program
    config = {
        "user": "whatabook_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "whatabook",
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

def print_menu():
# Prints main menu, returns user choice. Includes logic to deal with invalid input
    print("***************************")
    print("*   Whatabook Book Store  *")
    print("***************************")
    print(" 1. View Books            *")
    print(" 2. View Store Locations  *")
    print(" 3. My Account            *")
    print(" 4. Exit Program          *")
    print("***************************")

    user_choice = input("Please select an option: ")
    if str.isnumeric(user_choice): 
        return int(user_choice)
    else:
        return 0

def view_books(cursor):
# Selects all books at whatabook for the user to see
    cursor.execute("SELECT book_id, book_name, author, details from book;")
    books = cursor.fetchall()

    for book in books:
        print("\nbook id: {}\nauthor: {}\nbook name: {}\ndetails: {}".format(book[1], book[0], book[2], book[3]))

    input("\npress any key to continue...")

def view_stores(cursor):
# Selects all stores of whatabook for the user to see
    cursor.execute("SELECT store_id, locale from store;")
    stores = cursor.fetchall()

    for store in stores:
        print("\nstore id: {}\nlocale: {}".format(store[1], store[0]))
    
    input("\npress any key to continue...")

def validate_user_id():
# Used in the "my account" branch, this function takes user input until it is a valid user id
    val_user_id_list = [1, 2, 3]
    val_user_id = False
    while not val_user_id:
        user_id = input("Please enter a valid user id: ")
        if str.isnumeric(user_id):
            if int(user_id) in val_user_id_list:
                val_user_id = True
    
    return int(user_id)

def print_wishlist_menu(cursor):
# prints the user wishlist menu. Also includes similar logic to print_main_menu for validating user choice
    print("***************************")
    print("*      Wishlist Menu      *")
    print("***************************")
    print(" 1. View Wishlist         *")
    print(" 2. Add Books             *")
    print(" 3. Main Menu             *")
    print("***************************")

    user_choice = input("Please select an option: ")
    if str.isnumeric(user_choice): 
        return int(user_choice)
    else:
        return 0

def view_wishlist(cursor, user_id):
# Selects all books that are in a user's wishlist by using multiple inner joins
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {};".format(user_id))
    wishlists = cursor.fetchall()

    for wishlist in wishlists:
        print("\nuser id: {}\nfirst name: {}\nlast name: {}\nbook id: {}\nbook name: {}\nbook author: {}".format(wishlist[0], wishlist[1], wishlist[2], wishlist[3], wishlist[4], wishlist[5]))

    input("\npress any key to continue...")

def add_book(db, cursor, user_id):
# First, all books not in the user's wishlist is selected, then the user is prompted on which of these books they want added to their wishlist. Validation is included
# to verify the book selected can be.
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {});".format(user_id))
    available_books = cursor.fetchall()
    available_book_id_list = []
    val_book_id = False

    for book in available_books:
        print("\nbook id: {}\nbook name: {}\nauthor: {}\ndetails: {}".format(book[0], book[1], book[2], book[3]))
        available_book_id_list.append(int(book[0]))

    while not val_book_id:
        book_id = input("Please enter the book id of the book you want to add to your wishlist: ")

        if str.isnumeric(book_id):
            if int(book_id) in available_book_id_list: 
                val_book_id = True

    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))
    db.commit()
    input("Book successfully added to wishlist! Press any key to continue...")

def show_account_menu(db, cursor):
# Prints the account menu. Logic is included for validating the user id entered exists as well as a valid menu option is entered.
    user_id = validate_user_id()
    continue_program = True

    while continue_program:
        wishlist_menu_choice = print_wishlist_menu(cursor)
        
        if wishlist_menu_choice == 1:
            view_wishlist(cursor, user_id)
        elif wishlist_menu_choice == 2:
            add_book(db, cursor, user_id)
        elif wishlist_menu_choice == 3:
            print("Returning to main menu...")
            continue_program = False
        else:
            print("Sorry, that's invalid input! Try again.")

def main():
# The main function of the program. Everything stems from here, and the main loop and decision structure of the program is here as well
    db = connect()
    cursor = db.cursor()
    continue_program = True

    while continue_program:
        user_menu_choice = print_menu()
        
        if user_menu_choice == 1:
            view_books(cursor)
        elif user_menu_choice == 2:
            view_stores(cursor)
        elif user_menu_choice == 3:
            show_account_menu(db, cursor)
        elif user_menu_choice == 4:
            print("Have a nice day! Goodbye!")
            continue_program = False
        else:
            print("Sorry, that's invalid input! Try again.")
            
main()