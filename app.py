from modules.task_list import *
from modules.output import *
from data.task_lists import *
from modules.input import *

while (True):
    print_menu()
    option = get_input()
    
    if option.lower() == 'q':
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_tasks_by_status(tasks, "Not Done"))
    elif option == '3':
        print_list(get_tasks_by_status(tasks, "Done"))
    elif option == '4':
        description = get_task()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = get_time()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = get_task()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = get_task()
        time_taken = get_time()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
