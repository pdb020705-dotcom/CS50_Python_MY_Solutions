def main():
    text = input("Input: ")
    shortened = shortener(text)
    print("Output: ", end="")
    for c in shortened:
        print(c, end="")


def shortener(txt):
    char_list = list(txt)
    shortened_char_list = [] 
    vowel = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    for c in char_list:
        if c in vowel:
            shortened_char_list.append("")
        else:
            shortened_char_list.append(c)
    return shortened_char_list

main()