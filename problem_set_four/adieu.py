import inflect


def main():
    name_list = user_input("Name: ")
    p = inflect.engine()
    print("Adieu, adieu, to " + p.join(name_list))

def user_input(prompt):
    names = []
    while True:
        try:
            names.append(input(prompt))
        except EOFError:\
            #print() <--- This is needed because the cs50 codespace would otherwise include "Name: " in the output
            return names

main()