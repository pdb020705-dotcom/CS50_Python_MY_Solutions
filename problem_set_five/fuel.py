def main():
    print(convert(input("Input: ")))


def convert(fraction):
    x, y = fraction.split("/")
    try:
        if not x.isnumeric() or not y.isnumeric():
            raise ValueError
        else:
            x = int(x)
            y = int(y)
        if x > y:
            raise ValueError
        
        if y == 0:
            raise ZeroDivisionError
        percent = round((x / y) * 100)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        return gauge(percent)



def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()