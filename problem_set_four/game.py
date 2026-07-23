from random import randint

def main():
    level = get_level("Level: ")
    print(guessing_game("Guess: ", level))

def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return level

def guessing_game(prompt, l):
    correct_num = randint(0, l)
    while True:
        try:
            guess = int(input(prompt))
            if guess < 0:
                raise ValueError
        except ValueError:
            pass
        else:
            if guess == correct_num:
                return "Just right!"
            elif guess < correct_num:
                print("Too small!")
                pass
            elif guess > correct_num:
                print("Too large!")
                pass
            else:
                pass

main()