#!/usr/bin/python3
import requests
import sys

ID = sys.argv[1]
user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}')
user = user_response.json()
todo_response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = todo_response.json()

total_tasks = 0
done_tasks = []

if __name__ == "__main__":
    for todo in todos:
        if str(todo["userId"]) == ID:
            total_tasks += 1
            if todo["completed"]:
                done_tasks.append(todo["title"])

                print(f'Employee {user["name"]} is done with tasks({len(done_tasks)}/{total_tasks}):')
                for task in done_tasks:
                    print(f"\t {task}")
