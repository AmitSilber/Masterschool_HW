from Service.StudentPipeline import StudentPipeline
from Service import globals
import json


class StudentsOrganizer:
    students = {}
    student_count = 0

    @staticmethod
    def add_student(personal_details_form):
        StudentsOrganizer.student_count += 1
        new_student = StudentPipeline(globals.STEPS)
        StudentsOrganizer.students[personal_details_form[globals.USER_ID]] = new_student
        action_status = StudentsOrganizer.make_step(personal_details_form)

        if action_status == globals.INVALID_INPUTS:
            del StudentsOrganizer.students[personal_details_form[globals.USER_ID]]
            StudentsOrganizer.student_count -= 1
        return action_status

    @staticmethod
    def make_step(arguments_for_step):
        # step_name, user_id, step_payload

        if not StudentsOrganizer.validate_input(arguments_for_step):
            return globals.INVALID_INPUTS

        if not StudentsOrganizer.validate_id(arguments_for_step[globals.USER_ID]):
            return StudentsOrganizer.add_student(arguments_for_step)

        action_status = StudentsOrganizer.students[arguments_for_step[globals.USER_ID]].update_pipeline(
            arguments_for_step)

        if action_status[globals.STUDENT_STATUS] != globals.PENDING:
            return globals.STUDENT_NOT_PENDING[action_status[globals.STUDENT_STATUS]]

        if action_status[globals.ACTION_STATUS] == globals.FAIL:
            return globals.INVALID_INPUTS
        return globals.PENDING_MESSAGE

    @staticmethod
    def get_flow(user_id):
        if user_id not in StudentsOrganizer.students:
            return json.dumps({"message": globals.STUDENT_NOT_EXISTS}, indent=4)
        return json.dumps(StudentsOrganizer.students[user_id].get_flow(), indent=4)

    @staticmethod
    def get_status(user_id):
        if not StudentsOrganizer.validate_id(user_id):
            return globals.STUDENT_NOT_EXISTS
        return StudentsOrganizer.students[user_id].get_status()

    @staticmethod
    def get_state(user_id):
        if not StudentsOrganizer.validate_id(user_id):
            return json.dumps({"message": globals.STUDENT_NOT_EXISTS}, indent=4)
        return json.dumps(StudentsOrganizer.students[user_id].get_state(), indent=4)

    @staticmethod
    def validate_input(arguments):
        return globals.USER_ID in arguments and globals.STEP_NAME in arguments and globals.STEP_PAYLOAD in arguments

    @staticmethod
    def validate_id(user_id):
        return user_id in StudentsOrganizer.students
