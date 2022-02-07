# Harrison Birkner, module 5.3 assignment, 2/6/2022 

# The purpose of this program is to use the find and findOne methods
# to return all documents and a specific document from the students collection.
# Link to repo: https://github.com/harrisonBirkner/csd-310

from pymongo import MongoClient
import certifi
from Student import Student

def main():
    # Setting up MongoDB connection
    url = "mongodb+srv://admin:admin@cluster0.jancr.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url,tlsCAFile=certifi.where())
    db = client.pytech

    # Finding documents
    try:
        # Find and print all docs
        print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
        stu_docs = db.students.find({})
        for doc in stu_docs:
            print("Student ID:", doc["student_id"])
            print("First Name:", doc["first_name"])
            print("Last Name:", doc["last_name"], "\n")

        # Find and print a specific doc
        print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
        single_stu_doc = db.students.find_one({"student_id": "1007"})
        print("Student ID:", single_stu_doc["student_id"])
        print("First Name:", single_stu_doc["first_name"])
        print("Last Name:", single_stu_doc["last_name"])

        input("\nEnd of program, press any key to continue...")
    except Exception as e:
        print("Error finding documents: ", e)

main()