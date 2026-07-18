def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_list = list(s)
    counter = 0
    digit_counter = 0

    if len(s) < 2 or len(s) > 6:
        return False
    
    for c in char_list:
        if not c.isalnum():
            return False
        elif digit_counter == 0 and c == "0":
            return False
        elif digit_counter > 0 and c.isalpha():
            return False
        elif counter < 2 and c.isdigit():
            return False
        else:
            counter+=1
        if c.isdigit():
            digit_counter+=1

    return True
        



main()
