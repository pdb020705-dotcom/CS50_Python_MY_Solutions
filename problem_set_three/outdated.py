CALENDER_MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    
    while True:
        try:
            old_date = input("Date: ").capitalize().strip()
            month, day, year = split_old_date(old_date)
            if month > 12 or day > 31:
                raise ValueError
            else:
                new_date = ISO_format_converter(month, day, year)
        except ValueError:
            pass
        else:
            print(new_date)
            break

def split_old_date(date):
    if "/" in date:
        month, day, year = date.split("/")
        return int(month), int(day), int(year)
    elif "," in date:
        month, day, year = date.replace(",", "").split()
        return CALENDER_MONTH.index(month) + 1, int(day), int(year)
    
    raise ValueError

def ISO_format_converter(month, day, year):
    month = CALENDER_MONTH[month-1]
    if month.capitalize() in CALENDER_MONTH:
        month = int(CALENDER_MONTH.index(month) + 1)
        day = int(day)
        year = int(year)
        return f"{year}-{month:02}-{day:02}"
    else:
        month = int(month)
        day = int(day)
        year = int(year)
        return f"{year}-{month:02}-{day:02}"

main()