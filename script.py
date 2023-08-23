#!/usr/bin/python

#Create a test directory with the terminal, in which we should have 10 txt files 
#(for example test_1.txt, test_2.txt...), randomly write status in each one: status: PASS or status:FAIL. 
#Next to the Test directory, we should have script.py, which when we run it will create result.txt next to it, 
#in which the name of the file without txt and its status should be written (for example, test_1 -> PASS, etc.)

import os

def check_file_existence(filename):
    if not os.path.exists(filename):
        print("Result.txt file is created.")
    else:
        print("There is a result.txt file in your home directory ")
        exit()

def read_from_directory(dir_path):
    result = []
    files = os.listdir(dir_path)
    for name in files:
        if name.endswith(".txt"):
            with open(os.path.join(dir_path, name), "r") as file:
                status = file.read().strip()
                result.append((name[:-4], status))

    return result

def write_statuses_to_file(result, output_file_path):
    with open(output_file_path, "w") as result_file:
        for file_name, status in result:
            result_file.write(f"{file_name} -> {status}\n")

def main():
    dir_path =  '/home/lida/Desktop/Files_in_python/test'      #test directory path
    statuses = read_from_directory(dir_path)
    output_file_path = "../result.txt"
    check = check_file_existence(output_file_path)
    if not check:
        write_statuses_to_file(statuses, output_file_path)
        print("Statuses were written to the file")

main()
