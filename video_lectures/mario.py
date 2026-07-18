def main():
    print_block(3)
    # print_row(4)
    # print_column(3)
    

# def print_column(height):
#     for _ in range(height):
#         print("#")
        
# def print_row(width):
#     print("?" * width)

def print_block(dimen):
    for i in range(dimen):
        for j in range(dimen):
            print("#", end="")
        print()

main()