#!/usr/bin/python3
"""
Script to export an employee's TODO list progress to a CSV file.
"""
import csv
import requests
import sys

def export_todo_progress_to_csv(employee_id):
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

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_progress_to_csv(employee_id)
