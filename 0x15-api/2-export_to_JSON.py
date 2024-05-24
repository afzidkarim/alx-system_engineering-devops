#!/usr/bin/python3
"""Extend Python script to export data in JSON format."""

if __name__ == "__main__":

    import requests
    import sys
    import json

    id = int(sys.argv[1])
    user_request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user_request.json()["username"]

    tasks_request = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}")

    tasks = tasks_request.json()
    formatted_tasks = {f"{id}": [{
        "task": task["title"],
        "completed": task["completed"],
        "username": user} for task in tasks]}
    with open(f"{id}.json", mode="w") as file:
        json.dump(formatted_tasks, file)
