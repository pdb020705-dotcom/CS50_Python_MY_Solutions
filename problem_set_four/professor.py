import random


def main():
    level = get_level()
    math = generate_integer(level)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    count = 0
    while count < 10:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        attempts = 0

        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x+y:
                    count+=1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                attempts+=1

            


if __name__ == "__main__":
    main()