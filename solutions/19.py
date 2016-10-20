# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = [x for x in xrange(1,8)] # M T W T F S S

def get_days_in_month(month, year):
    days_in_february = 28
    if (month == 2):
        if ((year % 4) == 0):
            days_in_february +=1
            if (((year % 100) ==0) and ((year%400!=0))):
                days_in_february -=1 
    return [31,days_in_february,31,30,31,30,31,31,30,31,30,31][month-1]

def main():
    day_count = 1
    sunday_count = 0
    for year in range(1900,2001):
        for month in range(1,13):
            for day in range(1, get_days_in_month(month, year)+1):             
                current_day = days[(day_count%7)-1]
                day_count+=1 
                if ((current_day == 7) and (day==1)):
                    if (year!=1900):
                        sunday_count +=1
    
    print sunday_count

main()
