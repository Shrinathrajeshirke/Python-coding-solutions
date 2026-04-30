# Using itertools.cycle():

# Assign tasks to workers in round-robin
# 3 workers: Alice, Bob, Charlie
# 10 tasks

import itertools
tasks = ["Task1", "Task2", "Task3", "Task4", "Task5", "Task6", "Task7", "Task8", "Task9", "Task10"]
workers = itertools.cycle(['Alice', 'Bob', 'Charlie'])

def task_to_workers(tasks, workers):
    task_assign = {}
    for task, worker in zip(tasks, workers):
        task_assign[task] = worker
    return task_assign

print("Output")
print("Task assignments")
output = task_to_workers(tasks, workers)

for task, worker in output.items():
    print(f"{task}: {worker}")

