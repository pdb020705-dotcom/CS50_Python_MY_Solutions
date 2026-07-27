import sys
from tabulate import tabulate
import csv

def main():

    if len(sys.argv) != 2:
        sys.exit("Invalid input or format")
    elif not sys.argv[1].lower().endswith(".csv"):
        sys.exit("Invalid input or format")

    table = []
    try:
        with open(f"test_files/{sys.argv[1]}", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist!")



    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()