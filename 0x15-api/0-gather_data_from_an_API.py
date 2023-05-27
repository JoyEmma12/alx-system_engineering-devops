#!/usr/bin/python3
"""
Script that uses REST API 
for an employee and returns inoformation
about his/her TODO list
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Employee TODO list output
    """
    try:
        emply_id = int(argv[1])
    except ValueError:
        exit()


    url = 'https://jsonplaceholder.typicode.com'
    user = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo = '{user_uri}/todos'.format(user_uri=user_uri)

    res = requests.get(url).json()

    name = res.get('name')

    res = requests.get(todo).json()

    total = len(res)

    non_completed = sum([elem['completed'] is False for elem in res])

    completed = total - non_completed
    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(emp_name=name, completed=completed, total=total))

    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
