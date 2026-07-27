import sys
import os

def main():
    #print(os.getcwd()) <---- this line prints your Current Working Directory (cwd). Remove comment to find where THIS file is!
    if len(sys.argv) != 2:
        sys.exit("Invalid input or format")
    elif not sys.argv[1].lower().endswith(".py"):
        sys.exit("Invalid input or format")

    counter = 0
    try:
        with open(f"test_files/{sys.argv[1]}") as file:
            for line in file:
                if line.lstrip().startswith("#") or not line.strip():
                    continue
                else:
                    counter+=1
    except FileNotFoundError:
        sys.exit("File does not exist!")

    print(counter)

if __name__ == "__main__":
    main()
    