from Service import globals
from Service.Task import Task
from Service.ServicePipeline import StagePipeline


class Step(StagePipeline):

    def __init__(self, step):
        super().__init__(step[globals.TASKS], Task)
        self.name = step[globals.STEP_NAME]

    def get_flow(self):
        current_task = self._stages_pipeline[self._stage_index].name if self._status == globals.PENDING else ""
        step_name = self.name if self._status == globals.PENDING else ""
        return {globals.STUDENT_STATUS: globals.STATUS_STRING[self._status], globals.STEP_NAME: step_name,
                globals.CURRENT_TASK: current_task}

    def _validate_input(self, arguments):
        return self._stages_pipeline[self._stage_index].validate_input(arguments)

    def update_pipeline(self, arguments):
        print(arguments)
        if self._status != globals.PENDING:
            return {globals.ACTION_STATUS: globals.PASS, globals.STUDENT_STATUS: self._status}
        validation = self._validate_input(arguments)
        if not validation:
            return {globals.ACTION_STATUS: globals.FAIL, globals.STUDENT_STATUS: self._status}
        task_status = self._stages_pipeline[self._stage_index].attempt_task(arguments)
        self._update_status(task_status)
        return {globals.ACTION_STATUS: globals.PASS, globals.STUDENT_STATUS: self._status}

    def _update_status(self, task_status):
        if task_status == globals.REJECTED:
            self._status = globals.REJECTED
            return
        self._stage_index += self._stages_pipeline[self._stage_index].next()
        if self._stage_index == len(self._stages_pipeline):
            self._status = globals.ACCEPTED

    def _get_available_tasks(self):
        tasks = []
        index = 0
        while index < len(self._stages_pipeline):
            tasks.append(self._stages_pipeline[index])
            index += tasks[-1].next()
        return tasks

    def get_task_count(self):
        length = 0
        index = 0
        while index < len(self._stages_pipeline):
            index += self._stages_pipeline[index].next()
            length += 1
        return length

    def get_step_description(self):
        return {self.name: [task.name for task in self._stages_pipeline]}
