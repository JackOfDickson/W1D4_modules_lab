tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def get_tasks_by_status(list, status):
    status_list = []
    for task in list:
        if status == True and task["completed"] == True:
            status_list.append(task)
        elif status == "Not Done" and task["completed"] == False:
            status_list.append(task)
        else:
            continue
    return(status_list)

print(get_tasks_by_status(tasks, True))