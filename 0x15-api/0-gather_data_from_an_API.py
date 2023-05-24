#!/usr/bin/python3
"""
retrieves info from an api and prints the values to the standard Output
imports are arranged in alphabetical order
"""

import requests
import sys


if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(ID)
    user_res = requests.get(url)
    user = user_res.json()

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task.get("title"))

    print('Employee {} is done with tasks\
({}/{}):'.format(user.get("name"), len(done_tasks), len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task))
