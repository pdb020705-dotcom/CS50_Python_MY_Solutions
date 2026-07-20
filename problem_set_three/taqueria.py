MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price = 0

    while True:
        try:
            item = input("Item: ").title()
            if item not in MENU:
                raise ValueError
            price += MENU.get(item)
        except ValueError:
            print("That is not on the menu")
        except EOFError:
            break
        print(f"Total: ${price:.2f}")


main()