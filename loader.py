from database import *
import csv
import os
import time

from operator import itemgetter


def process_csv_file(directory, file):
    file = os.path.join(directory, file)
    rows = []
    with open(file,'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if any(x.strip() for x in row):
                rows.append(row)

    return rows

############################################################
#  TODO: Consider merging the file to database functions   #
# as the only difference between these is the column list  #
# and the table name                                       #
############################################################

def load_death_file_to_database(rows):
    assert_type(rows, list)
    if len(rows) == 0:
        return

    # Want cols 0,1,2,5,6,11
    getter = itemgetter(0, 1, 2, 5, 6, 11)
    rows = list(map(list, (map(getter, rows))))
    rows.pop(0)
    cols = ['country,territory,year,sex,age,deaths']

    db = Database()

    start = time.time()
    db.insert_list("deaths", cols, rows)
    stop = time.time()

    dt = stop-start

    print("DEATHS: Inserted {} rows in {} seconds ({} RPS)".format(len(rows), dt, len(rows)/dt))


def load_pop_file_to_database(rows):
    assert_type(rows, list)
    if len(rows) == 0:
        return

    getter = itemgetter(0, 1, 2, 3, 8, 11)
    rows = list(map(list, (map(getter, rows))))
    rows.pop(0)
    cols = ['country,territory,sex,age,year,population']

    db = Database()

    start = time.time()
    db.insert_list("population", cols, rows)
    stop = time.time()

    dt = stop - start

    print("POP: Inserted {} rows in {} seconds ({} RPS)".format(len(rows), dt, len(rows) / dt))


def load_countries_to_database(rows):
    assert_type(rows, list)
    if len(rows) == 0:
        return

    cols = ['code', 'name']
    db = Database()

    db.insert_list("country_codes", cols, rows)

def numerical_encode_cause(string):
    if can_be_int(string):
        return int(string)
    else:
        return int(string,36) + 10000  # To provide nice range checking

def load_who_to_database(rows):
    assert_type(rows, list)
    if len(rows) == 0:
        return

    getter = itemgetter(0,3,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)
    rows = list(map(list, (map(getter, rows))))
    rows.pop(0)

    cols = ['country,year,cause,sex,format,deaths1,deaths2,deaths3,deaths4,deaths5,deaths6,deaths7,deaths8,deaths9,'
            'deaths10,deaths11,deaths12,deaths13,deaths14,deaths15,deaths16,deaths17,deaths18,deaths19,deaths20,deaths21,'
            'deaths22,deaths23,deaths24,deaths25,deaths26']

        #Pass cause through custom mapping function (Used to reconcile inconsistent cause table systems of WHO, and for grouping causes)
    new_rows = []
    for row in rows:
        new_row = [r if r else 0 for r in row]
        new_row[2] = numerical_encode_cause(row[2])
        new_rows.append(new_row)

    db = Database()

    start = time.time()
    db.insert_list("who_mortality", cols, new_rows)
    stop = time.time()

    dt = stop - start

    print("WHO-MORT: Inserted {} rows in {} seconds ({} RPS)".format(len(rows), dt, len(rows) / dt))

def load_causes_to_database(rows):
    assert_type(rows, list)
    if len(rows) == 0:
        return

    getter = itemgetter(0,2)
    rows = list(map(list, (map(getter, rows))))
    rows.pop(0)
    cols = ['code,cause']

    db = Database()

    start = time.time()
    db.insert_list("causes", cols, rows)
    stop = time.time()

    dt = stop - start

    print("CAUSES: Inserted {} rows in {} seconds ({} RPS)".format(len(rows), dt, len(rows) / dt))

def load_hmd_data():
    print("HMD DATA: =========================================================================")
    for subdir, dirs, files in os.walk(os.getcwd()+"/data/hmd_countries"):
        for file in files:
            if "death" in file and "InputDB" in subdir:
                #print(os.path.join(subdir, file))
                rows = process_csv_file(subdir, file)
                load_death_file_to_database(rows)
            elif "pop" in file and "InputDB" in subdir:
                rows = process_csv_file(subdir, file)
                load_pop_file_to_database(rows)

def load_who_data():
    print("WHO DATA: ==========================================================================")

    base_dir = os.getcwd() + "/data/who_mortality"
    countries_file = "country_codes.csv"
    causes_file = "codes.csv"
    data_file_1 = "Morticd10_part1.csv"
    data_file_2 = "Morticd10_part2.csv"

    country_rows = process_csv_file(base_dir, countries_file)
    load_countries_to_database(country_rows)

    causes_rows = process_csv_file(base_dir, causes_file)
    load_causes_to_database(causes_rows)

    mortality_rows = process_csv_file(base_dir,data_file_1)
    load_who_to_database(mortality_rows)

    mortality_rows = process_csv_file(base_dir,data_file_2)
    load_who_to_database(mortality_rows)

def __main__():

    if "--clean" in sys.argv:
        Database().nuke()

    load_who_data()
    load_hmd_data()
if __name__ == "__main__":
    __main__()