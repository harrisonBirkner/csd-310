# Harrison Birkner, module 5.3 assignment, 2/5/2022 

# The purpose of this program is to insert example data into my students collection in my pytech mongodb database
# Link to repo: https://github.com/harrisonBirkner/csd-310

from pymongo import MongoClient
import certifi
from Student import Student

def main():
    # Setting up MongoDB connection
    url = "mongodb+srv://admin:admin@cluster0.jancr.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url,tlsCAFile=certifi.where())
    db = client.pytech
    students_col = db['students']

    # Setting up data to be inserted
    fred = Student("1007","fred","jones")
    fred_dict = fred.stu_info_as_dict()
    daphne = Student("1008","daphne","blake")
    daphne_dict = daphne.stu_info_as_dict()
    norville = Student("1009","norville","rogers")
    norville_dict = norville.stu_info_as_dict()

    # Trying insert operations
    try:
        print("-- INSERT STATEMENTS --")
        
        fred_doc_id = students_col.insert_one(fred_dict).inserted_id
        print("Inserted student record ", fred.first_name, fred.last_name, "into the students collection with document_id ", fred_doc_id)

        daphne_doc_id = students_col.insert_one(daphne_dict).inserted_id
        print("Inserted student record ", daphne.first_name, daphne.last_name, "into the students collection with document_id ", daphne_doc_id)

        norville_doc_id = students_col.insert_one(norville_dict).inserted_id
        print("Inserted student record ", norville.first_name, norville.last_name, "into the students collection with document_id ", norville_doc_id)

        input("\nEnd of program, press any key to exit...")
    except Exception as e:
        print("Error inserting record into database: ", e)
    
main()