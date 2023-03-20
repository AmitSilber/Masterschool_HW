from Service import globals
from Service.Step import Step


class StudentPipeline:

    def __init__(self):
        self.steps_pipeline = []
        self.status = globals.PENDING
        self.step_index = 0
        self.task_count = 0
        self.data = dict()
        self.parse_steps(globals.STEPS)

    def parse_steps(self, steps):
        for step in steps:
            parsed_step = Step(step)
            self.steps_pipeline.append(parsed_step)

    def check_status(self):
        current_step = self.steps_pipeline[self.step_index] if self.step_index < len(
            self.steps_pipeline) else "completed"
        return {
            "status": self._status_to_string(),
            "current_step": current_step,
            "tasks_completed": self.task_count,
            "steps_completed": self.step_index,
            "total_tasks": self._get_all_tasks(),
            "total_steps": len(self.steps_pipeline),
            "data": self.data,
        }

    def update_steps(self, arguments):
        """
        @param arguments: current arguments to the next task to accomplish
        @return: current status
        """
        if self.status != globals.PENDING:  # if not in progress just skip the update
            return {"action_status": globals.PASS, "student_status": self.status}
        validation = self.steps_pipeline[self.step_index].validate_input(arguments)  # make sure inputs are valid
        if validation == globals.FAIL:
            return {"action_status": globals.FAIL, "student_status": self.status}
        self.data |= arguments
        step_status = self.steps_pipeline[self.step_index].update_step(self.data)
        self._update_status(step_status)  # update status of the process
        return {"action_status": globals.PASS, "student_status": self.status}

    def _update_status(self, step_status):
        if step_status == globals.REJECTED:
            self.status = globals.REJECTED
            return
        self.task_count += 1
        if step_status == globals.PENDING:
            return
        self.step_index += 1
        if self.step_index == len(self.steps_pipeline):
            self.status = globals.ACCEPTED

    def _get_all_tasks(self):
        return sum([step.check_status()["total_tasks"] for step in self.steps_pipeline])

    def get_personal_info(self):
        personal_info = {}
        personal_info_keys = ("user_id", "first_name", "last_name", "email")
        for key in personal_info_keys:
            if key not in self.data:
                return {}
            personal_info[key] = self.data[key]
        return personal_info

    def _status_to_string(self):
        if self.status == globals.REJECTED:
            return "rejected"
        elif self.status == globals.ACCEPTED:
            return "accepted"
        return "pending"

    def print_status(self):
        status = self.check_status()
        print("########################")
        for entry in status:
            print(entry, ":", status[entry])
        print("########################")
