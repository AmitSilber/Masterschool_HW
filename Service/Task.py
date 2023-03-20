from Service import globals


class Task:

    def __init__(self, task_json):
        self.name = task_json["task_name"]
        self.pass_condition = task_json["pass_condition"]
        self.skip_condition = task_json["skip_condition"]
        self.next_task = int(task_json["next_task"])
        self.inputs = set(task_json["inputs"].split(globals.SEPARATOR))
        self.results = dict()

    def next(self):
        try:
            if eval(self.skip_condition, {}, self.results):
                return self.next_task
            return globals.NO_SKIP
        except NameError:
            return self.next_task

    def validate_input(self, arguments):
        return set(arguments.keys()) == self.inputs

    def attempt_task(self, arguments):
        self.results = arguments
        return globals.ACCEPTED if eval(self.pass_condition, {}, arguments) else globals.REJECTED

    def __repr__(self):
        return self.name
