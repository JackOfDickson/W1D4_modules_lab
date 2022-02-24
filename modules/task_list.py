# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    to_do_list = []
    for chore in list:
        if chore['completed'] == False:
            to_do_list.append(chore)
    return(to_do_list)

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_list = []
    for chore in list:
        if chore['completed'] == True:
            completed_list.append(chore)
    return(completed_list)


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    task_list = []
    for chore in list:
        if chore["time_taken"] >= time:
            task_list.append(chore)
    return(task_list)

## Find a task with a given description
def get_task_with_description(list, description):
    for chore in list:
        if chore["description"] == description:
            return(chore)

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    status_list = []
    for task in list:
        if status == "Done" and task["completed"] == True:
            status_list.append(task)
        elif status == "Not Done" and task["completed"] == False:
            status_list.append(task)
        else:
            continue
    return(status_list)


def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)
