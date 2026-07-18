def main():
    expression = input("Input your arithmetic expression ").strip()
    x, y, z = expression.split(" ")
    print(calculate(x, y, z))

def calculate(i1, e, i2):
    x = float(i1)
    z = float(i2)
    if e == "+":
        return float(x + z)
    elif e == "-":
        return float(x - z)
    elif e == "/":
        return float(x / z)
    elif e == "*":
        return float(x * z)

if __name__ == "__main__":
    main()
