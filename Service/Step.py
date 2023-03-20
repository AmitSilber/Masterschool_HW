from Service import globals
from Service.Task import Task


class Step:

    def __init__(self, step):
        self.tasks_pipeline = []
        self.status = globals.PENDING
        self.task_index = 0
        self.name = step["step_name"]
        self.parse_tasks(step["tasks"])

    def parse_tasks(self, tasks):
        for task in tasks:
            self.tasks_pipeline.append(Task(task))

    def check_status(self):
        return {"status": self._status_to_string(), "tasks_completed": self._get_length(self.task_index),
                "total_tasks": self._get_length(len(self.tasks_pipeline))}

    def validate_input(self, argument):
        if self.status != globals.PENDING:
            return True
        return self.tasks_pipeline[self.task_index].validate_input(argument)

    def update_step(self, arguments):
        task_status = self.tasks_pipeline[self.task_index].attempt_task(arguments)
        self._update_status(task_status)
        return self.status

    def _update_status(self, task_status):
        if task_status == globals.ACCEPTED:
            self.task_index += self.tasks_pipeline[self.task_index].next()
            if self.task_index == len(self.tasks_pipeline):
                self.status = globals.ACCEPTED
        else:
            self.status = globals.REJECTED

    def _status_to_string(self):
        if self.status == globals.REJECTED:
            return "rejected"
        elif self.status == globals.ACCEPTED:
            return "accepted"
        return "pending"

    def __repr__(self):
        return self.name + " with tasks: " + str(self._get_available_tasks()) + ", current task to perform: " + str(
            self.tasks_pipeline[self.task_index])

    def _get_available_tasks(self):
        tasks = []
        index = 0
        while index < len(self.tasks_pipeline):
            tasks.append(self.tasks_pipeline[index])
            index += tasks[-1].next()
        return tasks

    def _get_length(self, max_length):
        length = 0
        index = 0
        while index < max_length:
            index += self.tasks_pipeline[index].next()
            length += 1
        return length
