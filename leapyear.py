def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        print("this is leap year")
    else:
        return leap
        print("not aleap year")


# year = int(raw_input())
print(is_leap(2500))