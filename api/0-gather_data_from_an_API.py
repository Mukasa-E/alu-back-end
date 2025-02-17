#!/usr/bin/python3
"""
Script to fetch an employee's TODO list progress using a REST API.
"""

import requests
import sys


def fetch_todo_progress(employee_id):
    """Fetches and displays the TODO list progress of an employee."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Validate employee_id
    try:
        employee_id = int(employee_id)
        if employee_id <= 0:
            raise ValueError
    except ValueError:
        print("Error: Employee ID must be a positive integer.")
        return

    # Fetch employee data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's tasks
    todos_response = requests.get(
        f"{base_url}/todos",
        params={
            "userId": employee_id})
    if todos_response.status_code != 200:
        print("Could not retrieve TODO list.")
        return

    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    # Print the required output
    print(f"Employee {employee_name} is done with tasks("
          f"{num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./employee_todo_progress.py <employee_id>")
        sys.exit(1)

    fetch_todo_progress(sys.argv[1])
