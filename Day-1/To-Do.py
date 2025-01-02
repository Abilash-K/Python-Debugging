def add_task(task, task_list):
    task_list.append(task)
    return task_list

def delete_task(task, task_list):
    if task in task_list:
        task_list.remove(task)
    return task_list

tasks = []
add_task("Buy groceries", tasks)
delete_task("Go for a run", tasks)
print(tasks)


# Bugs
# The delete_task function will return the list 
# without the task even if the task doesn't exist 
# (i.e., it doesn't handle the case when the task is not found properly).
# No check to ensure that the task being added is not empty.
