'''
This program is for use with a standard GTFS stop_times.txt file.
This file for a specific transit agency can be obtained from https://transitfeeds.com/
The program will create individual files for each stop, then add the stop times for each
    stop into the appropriate files.
Please note this can take a while for large datasets.
'''

import csv
import time


def do_nothing():
    return


def get_stop_ids(csv_file_path):
    stop_ids = []
    print("Getting all stop IDs...")
    start_time = time.time()
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        id_count = 0
        for row in csv_reader:
            if id_count != 0:
                stop_ids.append(row[3])
                id_count += 1
            else:
                id_count += 1
    elapsed_time = time.time() - start_time
    print("Got %s IDs : " % id_count
          + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    return stop_ids


def add_data(csv_file_path, dest_folder):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Processing data...")
                start_time = time.time()
                line_count += 1
            else:
                stop_id = row[3]
                f = open("%s/%s.txt" % (dest_folder, stop_id), "a")
                f.write(str(row) + "\n")
                f.close()
                line_count += 1
        elapsed_time = time.time() - start_time
        print(("Processed %s lines : " % line_count) +
              time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


def create_files(file_names, dest_folder):
    start_time = time.time()
    files = 0
    print("Creating...")
    for id in file_names:
        # create new file with name {id}.txt
        # add rows matching stop_id to file
        f = open("%s/%s.txt" % (dest_folder, id), "w")
        f.close()
        files += 1
    elapsed_time = time.time() - start_time
    print("Created %s files : " % files
          + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


path_to_csv_file = input("Enter the path to the stop_times.txt file: ")
dest_folder = input(
    "Enter the path to the folder you would like to save the files to: ")

create_files_input = input("Do the individual stop files need to be created? (y/n): ")

if create_files_input == 'y':
    stop_ids = get_stop_ids(path_to_csv_file)
    create_files(stop_ids, dest_folder)

add_data_input = input(
    "Type 'exit' to skip adding the data now, or type 'y' to continue \n(Warning: this may take a while depending on the file size.): ")

if add_data_input == 'exit':
    do_nothing()
elif add_data_input == 'y':
    add_data(path_to_csv_file, dest_folder)
