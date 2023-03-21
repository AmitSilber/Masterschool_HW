# MasterSchool Home Assignment

1. Logic flow:

    * I looked at tasks/steps as nodes on a kind of line graph. Each node is connected to it successor however
under some conditions nodes can have different successors (this capture the second try for the IQ test).

    * I used strings representing arithmetic/ boolean expressions to represent the conditions for success/ failure in
a task/step, and also the conditions for changes in the successor function of each task.

    * Both task and step have similar structure, so they inherit from a parent class that implement the common
functionality and abstract methods that as a black box act alike but are implemented differently.

2. Input assumptions:
   * the paths for interacting with the program are as follows,
      * Get - The entire flow : `/flow`
      * Get - Current step and task for a specific user : `/state`
      * Post - Step completed (step_name, user_id, step_payload): `/complete_step`
      * Get - Whether the user is accepted, rejected or in progress: `/status`
   * I assumed that the request for the GET calls are of the form: ?user_id=user_id, and for the
   POST calls have the given body,
    ```
        {
            "step_name" : <step_name>,
            "user_id" : <user_id>,
            "step_payload" : {...}
        }
    ```
    * I also formatted the tasks in a specific way, for elaboration have a glimpse at the
    globals.py file Steps/Tasks section

         

### Running project

Clone project to your computer

```shell
git clone https://github.com/AmitSilber/Masterschool_HW
```

Install require packages

```shell
pip install -r requirements.txt
```

Run your server on your localhost

```shell
python manage.py runserver
```