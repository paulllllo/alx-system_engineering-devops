#!/usr/bin/python3
"""sends request to api based on input and formats outputs"""
import requests
import sys

def main():
    ID = sys.argv[1]
    EMPLOYEE_NAME = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}').json().get('name')
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}/todos')
    tasks = []
    total = 0

    for todo in res.json():
        if todo.get('completed'):
            tasks.append(todo.get('title'))
        total += 1
    print(f'Employee {EMPLOYEE_NAME} is done with tasks({len(tasks)}/{total}):')
    for task in tasks:
        print(f'\t {task}')


if __name__ == "__main__":
    main()
