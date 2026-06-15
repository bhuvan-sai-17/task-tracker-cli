import sys
import os
import pathlib
import json


jf = "\\tasks.json"
json_file_path = str(pathlib.Path().absolute()) + jf


# Returns all the tasks saved in the json file
def load_tasks():

    # create the json file if it dose not exist
    if os.path.exists(json_file_path):
        print("The json file alredy exists")

    else:
        print("The file does not exist, creating json file..")
        with open(json_file_path, "w") as file:
            json.dump([], file)
            print("The file tasks.json is created sucessfully.")

    # else exists then return the contents (task list) of the file
    pass


# writes to the json file
def save_tasks():
    # with open(json_file_path, "w") as file:
    #     json.dump(["something"], file)
    pass


def main():
    load_tasks()
    save_tasks()
    command = sys.argv[1]
    task = sys.argv[2:]

    # print(f"command: {command}")
    # print(f"task: {task}")
    # print(type(pathlib.Path().absolute()))

    # if command is None:
    #     print("You did not enter a command")
    # else:
    #     if command == "add":
    #         save_tasks()


if __name__ == "__main__":
    main()
