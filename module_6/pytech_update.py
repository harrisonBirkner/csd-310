# Harrison Birkner, module 6.2 assignment, 2/8/2022 

# The purpose of this program is to update a specific document in the student collection
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

        # Updating document w/ id: 1007
        result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

        # Find and print a specific doc
        print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")
        single_stu_doc = db.students.find_one({"student_id": "1007"})
        print("Student ID:", single_stu_doc["student_id"])
        print("First Name:", single_stu_doc["first_name"])
        print("Last Name:", single_stu_doc["last_name"])

        input("\n\nEnd of program, press any key to continue...")
    except Exception as e:
        print("Error updating documents: ", e)

main()