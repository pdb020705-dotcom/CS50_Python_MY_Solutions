def main():
    grocery_list = {}
    while True:
        try:
            item = input()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break
    for item in grocery_list:
        upper_cased_item = item.upper()
        print(f"{grocery_list.get(item)} {upper_cased_item}")

main()