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