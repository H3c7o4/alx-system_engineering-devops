#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json = r.json()
    dico = json.load(json)
    print('Employee {} is done with tasks({}/{}):\n'.format(
          dico.get('EMPLOYEE_NAME'), dico.get('NUMBER_OF_DONE_TASKS'),
          dico.get('TOTAL_NUMBER_OF_TASKS')))
    
    for i in range(int(dico.get('NUMBER_OF_DONE_TASKS'))):
        print("\t" + dico.get(TASK_TITLE))
