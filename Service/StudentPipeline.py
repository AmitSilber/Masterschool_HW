from Service import globals
from Service.Step import Step
from Service.ServicePipeline import StagePipeline


class StudentPipeline(StagePipeline):

    def __init__(self, steps):
        super().__init__(steps, Step)
        self.task_count = 0
        self.data = dict()

    def get_flow(self):
        current_step = self._stages_pipeline[self._stage_index].get_flow() if self._stage_index < len(
            self._stages_pipeline) else globals.EMPTY_STEP
        return {
            "status": globals.STATUS_STRING[self._status],
            "current_step": current_step[globals.STEP_NAME],
            "current_task": current_step[globals.CURRENT_TASK],
            "tasks_completed": self.task_count,
            "steps_completed": self._stage_index,
            "total_tasks": self._get_all_tasks(),
            "total_steps": len(self._stages_pipeline),
            "flow_description": self._get_flow_description()
        }

    def _get_all_tasks(self):
        return sum([step.get_task_count() for step in self._stages_pipeline])

    def _get_flow_description(self):
        return [step.get_step_description() for step in self._stages_pipeline]

    def get_status(self):
        return globals.STATUS_STRING[self._status]

    def get_state(self):
        return self._stages_pipeline[self._stage_index].get_flow() if self._stage_index < len(
            self._stages_pipeline) else globals.ACCEPTED_STEP

    def _validate_input(self, arguments):
        return arguments[globals.STEP_NAME] == self._stages_pipeline[self._stage_index].name

    def update_pipeline(self, arguments):
        if self._status != globals.PENDING:  # if not in progress just skip the update
            return {globals.ACTION_STATUS: globals.PASS, globals.STUDENT_STATUS: self._status}

        validation = self._validate_input(arguments)  # make sure inputs are valid
        if not validation:
            return {globals.ACTION_STATUS: globals.FAIL, globals.STUDENT_STATUS: self._status}

        self.data |= arguments[globals.STEP_PAYLOAD]
        step_status = self._stages_pipeline[self._stage_index].update_pipeline(self.data)
        if not step_status[globals.ACTION_STATUS]:
            return {globals.ACTION_STATUS: globals.FAIL, globals.STUDENT_STATUS: self._status}
        self._update_status(step_status[globals.STUDENT_STATUS])  # update status of the process
        return {globals.ACTION_STATUS: globals.PASS, globals.STUDENT_STATUS: self._status}

    def _update_status(self, step_status):
        if step_status == globals.REJECTED:
            self._status = globals.REJECTED
            return
        self.task_count += 1
        if step_status == globals.PENDING:
            return
        self._stage_index += 1
        if self._stage_index == len(self._stages_pipeline):
            self._status = globals.ACCEPTED

    def _get_personal_info(self):
        personal_info = {}
        personal_info_keys = ("user_id", "first_name", "last_name", "email")
        for key in personal_info_keys:
            if key not in self.data:
                return {}
            personal_info[key] = self.data[key]
        return personal_info
