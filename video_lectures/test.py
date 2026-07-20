def main():
    number = leading_zeros("Input Agent Code: ")
    print(number)

def leading_zeros(prompt):
    code = input(prompt)
    return f"{code:03}"

main()