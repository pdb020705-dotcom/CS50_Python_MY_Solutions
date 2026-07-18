def main():
    clock = input("input the current time in ##:## format! ")
    time = convert(clock)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
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

