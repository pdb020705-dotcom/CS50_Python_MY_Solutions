def main():
    i = 50
    while i >= 0:
        print(f"Amount due: {i}")
        insert = int(input("Insert coin: "))
        if validDenomination(insert):
            i -= insert
        if i == 0:
            break
    i *= -1
    print(f"Change owed: {i}" )   
    

def validDenomination(denom):
    if denom == 25 or denom == 10 or denom == 5: return True


if __name__ == "__main__":
    main()