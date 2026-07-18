def main():
    text = input("camelCase: ")
    converted_text = snakeCaseConverter(text)
    print("snake_case: ", end="")
    for i in range(len(converted_text)):
        print(converted_text[i], end="")

def snakeCaseConverter(inp):
    char_list = list(inp)
    converted_char_list = []
    for c in char_list:
        if c.isupper():
            converted_char_list.append("_"+c.lower())
        else:
            converted_char_list.append(c)
    return converted_char_list

if __name__ == "__main__":
    main()