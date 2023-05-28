# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program generates a calendar for any month after 1752. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was debugging a few problems. The first problem was stopping strings from throwing an error in my get year and month functions. 
#      My second problem was that I accidentally put days_year as my parameter for compute ofset so I was getting weird errors and then incorrect values.
#      My third problem was that I was trying to completely automate the testing so I wasted alot of time trying to figure out how to automatically put values into an input:
#      I also learned two new tools, the isdigit() method and the "in" keyword to quickly check values in an if statement. 
# 5. How long did it take for you to complete the assignment?
#      This program took me a little over 4 hours.

def get_month():
    month = input("Enter a month number: ")
    valid = False
    while valid == False:
        if month.isdigit() == True:
            month = int(month)
            if month < 1 or month > 12:
                print("Selected month must be between 1 and 12.")
                month = input("Enter a valid month number: ")
            elif month > 1 or month <= 12:
                valid = True
        elif month.isdigit() == False:
            print("Selected month must be a integer.")
            month = input("Enter a valid month number: ")
    return month

def get_year():
    valid = False
    year = input("Enter year after 1752: ")
    while valid == False:
        if year.isdigit() == True:
            year = int(year)
            if year <= 1752:
                print("Selected year must be after 1752.")
                year = input("Enter a valid year number: ")
            elif year > 1752:
                valid = True
        elif year.isdigit() == False:
            print("Selected year must be a integer.")
            year = input("Enter a valid year: ")
    return year

def compute_offset(year, month):
    num_days = 0
    for year_count in range(1753, year):
        num_days += days_year(year_count)
    for month_count in range(1, month):
        num_days += days_month(month_count, year)
    return (num_days + 1) % 7

def days_month(month_count, year):
    """This function calculates the days in a month given a month and year"""
    if month_count in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month_count in [4, 6, 9, 11]:
        return 30
    # figuring out the correct days in febuary by detetmining if it's a leap year. 
    elif month_count == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28

def days_year(year):
    """This function calculates the days in a given year"""
    month = 1
    days_year = 0
    while month <= 12:
        days_year += days_month(month, year)
        month += 1
    return days_year

def display_table(month, year, DayOfWeek, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(DayOfWeek) == type(0))
    assert(0 <= DayOfWeek <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print(f"Calendar for {month}/{year}:")
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(DayOfWeek):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        DayOfWeek += 1
        # Newline after Saturdays
        if DayOfWeek % 7 == 0:
            print("") # newline

    # We must end with a newline
    if DayOfWeek % 7 != 0:
        print("") # newline

# Output
test = input("Would you like to run automated testing? Y/N ")

if test == "y" or test == "yes":
    print("Test Case 1: January 1753")
    month = 1
    year = 1753
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Test Case 2: February 1753")
    month = 2
    year = 1753
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Test Case 3: January 1754")
    month = 1
    year = 1754
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Test Case 4: February 1756")
    month = 2
    year = 1756
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Test Case 5: February 1800")
    month = 2
    year = 1800
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Test Case 6: February 2000")
    month = 2
    year = 2000
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print('Test Case 7: Month: "error", 0, 13, 11')
    print('Note values will need to be typed.')
    get_month()
    year = 2023
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print('Test Case 8: Year: "error", -1, 1752, 2019')
    print('Note values will need to be typed. Month is tested as January')
    month = 1
    get_year()
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))
    print("")

    print("Automated testing completed. Have a great day.")
else:
    month = get_month()
    year = get_year()
    DayOfWeek = compute_offset(year, month)
    display_table(month, year, DayOfWeek, days_month(month, year))