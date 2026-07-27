import sys
import csv

def main():

    if len(sys.argv) != 3:
        sys.exit("Incorrect input!")

    students_dict = {}
    try:
        with open(f"test_files/{sys.argv[1]}") as infile, open("test_files/after.csv", "w", newline="") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

            writer.writeheader()
            
            for row in reader:
                last, first = row['name'].split(",")
                first = first.strip()
                house = row['house']
                writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("File does not exist!")


if __name__ == "__main__":
    main()
            
    