from StudentsOrganizer import StudentsOrganizer

if __name__ == "__main__":
    so = StudentsOrganizer()
    message = so.make_step({"user_id": "1",
                            "first_name": "Amit",
                            "last_name": "Silber",
                            "email": "amit@amit.amit",
                            "timestamp": "16:22"})
    print(message)
    print(so.get_status("1"))
    message = so.make_step({"user_id": "2",
                            "first_name": "Ori",
                            "last_name": "Silber",
                            "email": "ori@ori.ori",
                            "timestamp": "16:30"})
    print(message)
    print(so.get_status("2"))
    message = so.make_step({"user_id": "1",
                            "first_name": "Amit",
                            "last_name": "Silber",
                            "email": "amit@amit.amit",
                            "timestamp": "16:22"})
    print(message)
    print(so.get_status("1"))
    message = so.make_step({"user_id": "1", "test_id": "100", "score": "70", "timestamp": "14:30"})
    print(message)
    print(so.get_status("1"))
    message = so.make_step({"user_id": "1", "test_id": "100", "score_retry": "90", "timestamp": "14:40"})
    print(message)
    print(so.get_status("1"))
    message = so.make_step({"user_id": "2", "test_id": "100", "score_retry": "90", "timestamp": "14:40"})
    print(message)
    print(so.get_status("2"))
