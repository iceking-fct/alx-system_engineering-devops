#!/usr/bin/python3

'''Gather users data from an API'''

import csv
import requests
from sys import argv
'''the modules to work with'''


def get_employee_todos_progress(employee_id):
    '''This function returns the info about an employee todos progress'''
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_data = requests.get(url + f"users/{employee_id}")
        user_data = user_data.json()
        employee_name = user_data['username']

        '''fetch todos list for the employee'''
        todos_list = requests.get(url + f"todos?userid={employee_id}")
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

            '''export data to csv'''
            csv_filename = f"{employee_id}.csv"
            with open(csv_filename, mode="w", newline='') as csv_file:
                writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for task in json_todos_list:
                    writer.writenow([employee_id, employee_name,
                                     task['completed'], task['title']])

    except Exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: Script <employee_id")
    else:
        get_employee_todos_progress(argv[1])
