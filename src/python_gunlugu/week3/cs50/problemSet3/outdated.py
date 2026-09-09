
Months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        try:
            my_date = input("Date: ")
            if "/" in my_date:
                month, day, year = my_date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in my_date:
                month_day, year = my_date.split(",")
                month_name, day = month_day.strip().split(" ")
                month = Months.get(month_name)
                if month is None:
                    raise ValueError("Invalid month name.")
                day = int(day)
                year = int(year.strip())
            else:
                raise ValueError("Invalid date format.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        else:
            print(f"{year}-{month:02d}-{day:02d}") 


main()