from StudentsOrganizer import StudentsOrganizer

if __name__ == "__main__":
    so = StudentsOrganizer()
    message = so.add_student({"user_id": "1",
                              "first_name": "Amit",
                              "last_name": "Silber",
                              "email": "amit@amit.amit",
                              "timestamp": "16:22"})
    print(message)
    print(so.check_status("1"))
    message = so.add_student({"user_id": "2",
                              "first_name": "Ori",
                              # "last_name": "Silber",
                              "email": "ori@ori.ori",
                              "timestamp": "16:30"})
    print(message)
    print(so.check_status("2"))
    message = so.add_student({"user_id": "1",
                              "first_name": "Amit",
                              "last_name": "Silber",
                              "email": "amit@amit.amit",
                              "timestamp": "16:22"})
    print(message)
    print(so.check_status("1"))

