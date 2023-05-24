#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId)
    user_res = requests.get(url)
    user = user_res.json()
    employeeName = user.get("name")

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(done_tasks), len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task))
