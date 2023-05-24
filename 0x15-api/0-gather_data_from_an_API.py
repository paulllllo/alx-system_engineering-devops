#!/usr/bin/python3
"""
retrieves info from an api and prints the values to the standard Output
imports are arranged in alphabetical order
"""
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    user_res = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}')
    user = user_res.json()
    todo_res = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todo_res.json()

    total_tasks = 0
    done_tasks = []

    for todo in todos:
        if str(todo.get("userId")) == ID:
            total_tasks += 1
            if todo.get("completed"):
                done_tasks.append(todo.get("title"))

    print(f'Employee {user.get("name")} is done with tasks\
({len(done_tasks)}/{total_tasks}):')
    for task in done_tasks:
        print(f"\t {task}")
