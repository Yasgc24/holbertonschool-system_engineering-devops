#!/usr/bin/python3
"""Script to export data in the CSV format."""
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    with requests.session() as session:
        response_tasks = session.get(todos_url)
        response_users = session.get(user_url)
        data_tasks = response_tasks.json()
        data_users = response_users.json()
        username = data_users["username"]
        tasks_done = 0
        total_tasks = len(data_tasks)
        data = ""
        for record in data_tasks:
            completed = record["completed"]
            title = record["title"]
            data += '"{}","{}","{}","{}"\n'.format(
                argv[1], username, completed, title)
        text_file = "{}.cvs".format(argv[1])
        with open(text_file, mode="w+", encoding="utf-8") as file:
            file.write(data)
