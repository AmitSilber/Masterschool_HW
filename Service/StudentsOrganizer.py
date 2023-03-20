from Service.StudentPipeline import StudentPipeline
from Service import globals


class StudentsOrganizer:
    students = {}
    student_count = 0

    @staticmethod
    def add_student(personal_details_form):
        if "user_id" not in personal_details_form:
            return globals.INVALID_INPUTS

        StudentsOrganizer.student_count += 1
        new_student = StudentPipeline()
        StudentsOrganizer.students[personal_details_form["user_id"]] = new_student
        action_status = StudentsOrganizer.make_step(personal_details_form)

        if action_status == globals.INVALID_INPUTS:
            del StudentsOrganizer.students[personal_details_form["user_id"]]
        return action_status

    @staticmethod
    def make_step(arguments_for_step):
        if arguments_for_step["user_id"] not in StudentsOrganizer.students:
            return globals.STUDENT_NOT_EXISTS
        action_status = StudentsOrganizer.students[arguments_for_step["user_id"]].update_steps(arguments_for_step)

        if action_status["student_status"] != globals.PENDING:
            return globals.STUDENT_NOT_PENDING[action_status["student_status"]]

        if action_status["action_status"] == globals.FAIL:
            return globals.INVALID_INPUTS

        return globals.PENDING_MESSAGE

    @staticmethod
    def check_status(user_id):
        if user_id not in StudentsOrganizer.students:
            return {}
        return StudentsOrganizer.students[user_id].check_status()
