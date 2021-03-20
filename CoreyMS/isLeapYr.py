"""
This function checks, whether or not a year passed is Leap or not
"""
# Number of days per month, the first is a placeholder for python indexing
monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]

def isLeap(year):
    """Return True for leap year, False for non-leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )

def daysInMonth(year, month):
    """Return number of days in that month in that year"""
    if not 1 <= month <= 12 : # Month must be between 1 and 12, else Invalid
        return 'Invalid Month'

    if month == 2 and isLeap(year):
        return 29
    
    return monthDays[month]

print(isLeap(2008))