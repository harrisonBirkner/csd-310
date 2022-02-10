# Harrison Birkner, module 6.2 assignment, 2/8/2022 

# The purpose of this program is to insert and then delete a specific document in the student collection
# Link to repo: https://github.com/harrisonBirkner/csd-310

from pymongo import MongoClient
import certifi
from Student import Student

def main():
    # Setting up MongoDB connection
    url = "mongodb+srv://admin:admin@cluster0.jancr.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url,tlsCAFile=certifi.where())
    db = client.pytech

    # Database operations
    try:
        # Find and print all docs
        print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
        stu_docs = db.students.find({})
        for doc in stu_docs:
            print("Student ID:", doc["student_id"])
            print("First Name:", doc["first_name"])
            print("Last Name:", doc["last_name"], "\n")
    except Exception as e:
        print("Error finding documents: ", e)

    # Setting up data to be inserted
    velma = Student("1010","velma","dinkley")
    velma_dict = velma.stu_info_as_dict()

    try:
        # Insert document
        print("\n-- INSERT STATEMENTS --")
        result = db.students.insert_one(velma_dict).inserted_id
        print("Inserted student record into the students collection with document_id ", result)
    except Exception as e:
        print("Error inserting documents: ", e)

    try:
        # Find and print a specific doc
        print("\n-- DISPLAYING STUDENT TEST DOC --")
        single_stu_doc = db.students.find_one({"student_id": "1010"})
        print("Student ID:", single_stu_doc["student_id"])
        print("First Name:", single_stu_doc["first_name"])
        print("Last Name:", single_stu_doc["last_name"])
    except Exception as e:
        print("Error updating documents: ", e)

    try:
        # Deleting test doc
        db.students.delete_one({"student_id": "1010"})
    except Exception as e:
        print("Error deleting document: ", e)

    try:
        # Find and print all docs
        print("\n\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
        stu_docs = db.students.find({})
        for doc in stu_docs:
            print("Student ID:", doc["student_id"])
            print("First Name:", doc["first_name"])
            print("Last Name:", doc["last_name"], "\n")
    except Exception as e:
        print("Error finding documents: ", e)

    input("\n\nEnd of program, press any key to continue...")

main()