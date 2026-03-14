# Nunmber of days per month. First value placeholder for indexing purpose.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap(year):
    """Return True if the year is leap and false otherwise"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(2020))

def days_in_month(year,month):
    """This Function returns the number of days in that month for that year"""
    if not 1 <= month <= 12:
        return "Invalid Month!"
    
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2020,2))