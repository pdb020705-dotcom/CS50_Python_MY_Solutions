def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    if to.__contains__(" "):
        first, last = to.split(" ")
        return print(f"Hello, {first}")
    else:
        return print(f"hello, {to}")

main()    