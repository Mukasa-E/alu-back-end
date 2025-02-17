#!/usr/bin/python3
"""
This module fetches all employees' TODO list data from a REST API and
exports the data in JSON format.
"""

import json
import requests


def get_all_employees_todo_data():
    """Fetch all employee tasks and export them in JSON format."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error: Unable to fetch users data")
        return

    users = users_response.json()

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        return

    todos = todos_response.json()

    tasks_by_user = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        tasks_by_user[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos if task["userId"] == user_id
        ]

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks_by_user, file, indent=4)

if __name__ == "__main__":
    get_all_employees_todo_data()
