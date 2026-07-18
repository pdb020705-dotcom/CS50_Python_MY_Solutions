def main():
    fuel_tank = calculate_fuel_percentage("Fraction: ")

    if fuel_tank >= 99:
        print("F")
    elif fuel_tank <= 1:
        print("E")
    else:
        print(f"{fuel_tank:.0f}%")

def calculate_fuel_percentage(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
            if x < 0 or y <= 0:
                raise ZeroDivisionError
            return float((float(x) / float(y)) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            print("Can't be less than or equal to 0.")


main()