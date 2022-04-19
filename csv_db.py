import csv

with open("local_db.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)


def insert_record():
    # this is a comment
    print("inserting record")


def find_record():
    print("finding record")


def update_record():
    print("updating record")


def delete_record():
    print("deleting record")


def sell():
    print("selling item")
