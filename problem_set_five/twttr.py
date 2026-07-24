def main():
    text = input("Input: ")
    shortened = shorten(text)
    print(f"Output: {shortened}")


def shorten(txt):
    char_list = list(txt)
    shortened_char_list = [] 
    vowel = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    for c in char_list:
        if c in vowel or c.isnumeric():
            shortened_char_list.append("")
        else:
            shortened_char_list.append(c)
    word = "".join(shortened_char_list)

    return word

if __name__ == "__main__":  
    main()