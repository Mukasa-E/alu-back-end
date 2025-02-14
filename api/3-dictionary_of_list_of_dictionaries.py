#!/usr/bin/python3
"""
Script to export all employees' TODO list progress to a JSON file.
"""
import json
import requests

def export_all_todo_progress_to_json():
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error: Unable to fetch users.")
        return
    users_data = users_response.json()

    # Fetch all TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODOs.")
        return
    todos_data = todos_response.json()

    # Prepare JSON data
    json_data = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_todos = [task for task in todos_data if task.get("userId") == user_id]
        json_data[user_id] = [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in user_todos
        ]

    # Write to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as file:
        json.dump(json_data, file, indent=4)

if __name__ == "__main__":
    export_all_todo_progress_to_json()
