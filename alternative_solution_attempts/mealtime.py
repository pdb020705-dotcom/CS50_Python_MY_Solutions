def main():
    clock = input("input the current time in ##:## format! ")
    print(clock)
    time = convert(clock)

    if time >= 7 or time <= 8:
        print("breakfast time")
    elif time >= 12 or time <= 13:
        print("lunch time")
    elif time >= 18 or time <= 19:
        print("dinner time")

def convert(time):
    hour, min = time.split(":")
    min = float(min)
    hour = float(hour)
    min = float(min / 60)
    clock = float(hour + min)


    return clock

if __name__ == "__main__":
    main()

