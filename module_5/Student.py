# Harrison Birkner 2/5/2022, module 5.3 assignment

# The purpose of this simple class is to better encapsulate
# the student data and has a custom function to return an
# instance of the class as a dictionary for inserting into 
# MongoDB collections.
# Link to repo: https://github.com/harrisonBirkner/csd-310


class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def stu_info_as_dict(self):
        return {
            "student_id": str(self.student_id),
            "first_name": str(self.first_name),
            "last_name": str(self.last_name)
        }