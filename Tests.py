#!/usr/bin/python

# We need to create "Tests" directory in which should be 10 files named today's "month, date, hour, minute, second.log".
# Files with an odd creation second should contain the "Status -> Fail" otherwise "Status -> Pass"

import os
import datetime
import time

def check_directory_exists(directory_name):
    if os.path.exists(directory_name):
        print("Directory is created")
    else:
        print("Directory isn't created")

def create_current_time_files(directory_name):
    for i in range(1,11):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"file_{i+1}_{current_time}.log"
        file_path = os.path.join(directory_name, file_name)
        with open(file_path, "w") as file:
            if int(datetime.datetime.now().strftime('-%S')) % 2 == 0:
                file.write("Status -> Pass")
            else:
                file.write("Status -> Fail")
        time.sleep(1)
    print(f"Files created successfully in directory '{directory_name}'.")


def main():
    directory_name = "tests"
    os.mkdir(directory_name)

    check_directory_exists(directory_name)
    create_current_time_files(directory_name)

if __name__ == "__main__":
    main()



