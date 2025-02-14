#!/usr/bin/python3
"""
Script to export an employee's TODO list progress to a JSON file.
"""
import json
import requests
import sys

def export_todo_progress_to_json(employee_id):
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}.")
        return
    user_data = user_response.json()
    employee_name = user_data.get("username")

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}.")
        return
    todos_data = todos_response.json()

    # Prepare JSON data
    json_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name,
            }
            for task in todos_data
        ]
    }

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode="w") as file:
        json.dump(json_data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_progress_to_json(employee_id)
