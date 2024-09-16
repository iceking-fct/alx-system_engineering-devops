#!/usr/bin/python3

'''Gather users data from an API'''
import json
import requests
from sys import argv


'''the modules to work with'''


def get_employee_todos_progress(employee_id):
    '''This function returns the info about an employee todos progress'''
    try:
        url = "https://jsonplaceholder.typicode.com/"

        # Fetch user data
        user_data = requests.get(url + f"users/{employee_id}")
        user_data = user_data.json()
        employee_name = user_data.get('username', 'Unknown')

        '''fetch todos list for the employee'''
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        num_task_done = len(task_done)

        '''display results'''
        print(f"Employee {employee_name} is done with tasks("
              f"{num_task_done}/{total_task}):")

        '''title of completed tasks'''
        for task in task_done:
            print(f"\t {task['title']}")


    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: Script <employee_id>")  # Fixed the usage message
    else:
        try:
            employee_id = int(argv[1])  # Ensure the employee ID is an integer
            get_employee_todos_progress(employee_id)
        except ValueError:
            print("Employee ID should be an integer.")
