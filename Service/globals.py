###################
# Status values:
REJECTED = 0
PENDING = -1
ACCEPTED = 1

STATUS_STRING = {REJECTED: "Rejected", PENDING: "In progress", ACCEPTED: "Accepted"}

##################
# Action status:
PASS = True
FAIL = False

##################
# successor function for tasks:
NO_SKIP = 1
##################
# Messages:
STUDENT_NOT_EXISTS = "Student does not exists"
STUDENT_NOT_PENDING = {REJECTED: "Student rejected", ACCEPTED: "Student accepted"}
INVALID_INPUTS = "Inputs are invalid"
PENDING_MESSAGE = "Current status is in progress"
EMPTY_STEP = {"step_name": "", "current_task": ""}
ACCEPTED_STEP = {"status": "Accepted", "step_name": "", "current_task": ""}

##################
# External parameters
SEPARATOR = ","
USER_ID = "user_id"
STEP_NAME = "step_name"
TASKS = "tasks"
STEP_PAYLOAD = "step_payload"
##################
# Internal parameters
ACTION_STATUS = "action_status"
STUDENT_STATUS = "student_status"
CURRENT_TASK = "current_task"

##################
# Steps/Tasks:
# a step includes the following attributes: name and list of tasks
# a task includes the following attributes: name, pass/fail condition, skip condition, next task (successor), input: arguments for task
###

PERSONAL_DETAILS_FORM = {"step_name": "Personal Details Form",
                         "tasks": [{"task_name": "Personal Details Form",
                                    "pass_condition": "True",
                                    "skip_condition": "False",
                                    "next_task": "1",
                                    "inputs": "user_id,first_name,last_name,email,timestamp",
                                    }]}
IQ = {"step_name": "IQ test",
      "tasks": [{"task_name": "IQ test",
                 "pass_condition": "int(score) > 60",
                 "skip_condition": "int(score) > 80",
                 "next_task": "2",
                 "inputs": "user_id,test_id,score,timestamp",
                 },
                {"task_name": "IQ test retry",
                 "pass_condition": "int(score_retry) > 80",
                 "skip_condition": "False",
                 "next_task": "1",
                 "inputs": "user_id,test_id,score_retry,timestamp",
                 }
                ]}
INTERVIEW = {"step_name": "Interview",
             "tasks": [{"task_name": "schedule interview",
                        "pass_condition": "True",
                        "skip_condition": "False",
                        "next_task": "1",
                        "inputs": "user_id,interview_date",
                        },
                       {"task_name": "perform_interview",
                        "pass_condition": "decision == \"passed_interview\"",
                        "skip_condition": "False",
                        "next_task": "1",
                        "inputs": "user_id,interview_date,interviewer_id,decision",
                        }]
             }
SIGN_CONTACT = {"step_name": "Sign Contract",
                "tasks": [{"task_name": "upload identification document",
                           "pass_condition": "True",
                           "skip_condition": "False",
                           "next_task": "1",
                           "inputs": "user_id,passport_number,timestamp",
                           },
                          {"task_name": "sign contract",
                           "pass_condition": "True",
                           "skip_condition": "False",
                           "next_task": "1",
                           "inputs": "user_id,timestamp",
                           }]}

PAYMENT = {"step_name": "Payment",
           "tasks": [{"task_name": "Payment",
                      "pass_condition": "True",
                      "skip_condition": "False",
                      "next_task": "1",
                      "inputs": "user_id,payment_id,timestamp",
                      }]}
JOIN_SLACK = {"step_name": "Join Slack",
              "tasks": [{"task_name": "Join Slack",
                         "pass_condition": "True",
                         "skip_condition": "False",
                         "next_task": "1",
                         "inputs": "user_id,email,timestamp",
                         }]}

STEPS = [PERSONAL_DETAILS_FORM, IQ, INTERVIEW, SIGN_CONTACT, PAYMENT, JOIN_SLACK]
