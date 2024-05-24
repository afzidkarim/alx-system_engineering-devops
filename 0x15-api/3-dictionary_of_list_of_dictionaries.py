
#!/usr/bin/python3
"""Extend your Python script to export data in JSON format."""

if __name__ == "__main__":
    import requests
    import json

    user_request = requests.get("https://jsonplaceholder.typicode.com/users")
    users = user_request.json()

    tasks_request = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks_request.json()

    formatted_data = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        user_tasks = []

        for task in tasks:
            if task["userId"] == user_id:
                task_data = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                user_tasks.append(task_data)
        formatted_data[user_id] = user_tasks
    with open("todo_all_employees.json", "w") as file:
        json.dump(formatted_data, file)

