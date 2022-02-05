# Harrison Birkner, module 5.2 assignment, 2/3/2022 

# The purpose of this program is to attempt to connect to my pytech
# MongoDB database and print a list of collections in the database.
# Link to repo: https://github.com/harrisonBirkner/csd-310

from pymongo import MongoClient
import certifi

def main():
    url = "mongodb+srv://admin:admin@cluster0.jancr.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url,tlsCAFile=certifi.where())
    db = client.pytech

    try:
        print("-- Pytech Collection List --")
        print(db.list_collection_names())
        input("\nEnd of program, press any key to exit...")
    except Exception as e:
        print("Error connecting to database: ", e)
    
main()