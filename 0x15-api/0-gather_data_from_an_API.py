#!/usr/bin/python3
"""A script using a REST API that returns information
about the progress of his/her task list."""

if __name__ == "__main__":

    import requests
    import sys

    id = int(sys.argv[1])
    user_request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user_request.json()["name"]

    tasks_request = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}")

    number_1 = 0
    number_2 = 0
    for task in tasks_request.json():
        if task['completed']:
            number_1 += 1
        number_2 += 1

    print(f"Employee {user} is done with tasks({number_1}/{number_2}):")
    for task in tasks_request.json():
        if task['completed'] is True:
            print(f"\t {task['title']}")
