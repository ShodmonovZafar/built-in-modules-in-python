import datetime

# Constantas
datetime.MINYEAR  # The smallest year number allowed in a date or datetime object. MINYEAR is 1.
datetime.MAXYEAR  # The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
datetime.UTC  # Alias for the UTC timezone singleton datetime.timezone.utc.

# Available Types

def datetime_date():
    """
    class datetime.date
        An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. 
        Attributes: year, month, and day.
    """
    datetime.date(2023, 6, 17)

def datetime_time():
    """
    class datetime.time
        An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. 
        (There is no notion of “leap seconds” here.) 
        Attributes: hour, minute, second, microsecond, and tzinfo.
    """
    datetime.time()

def datetime_datetime():
    """
    class datetime.datetime
        A combination of a date and a time. 
        Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
    """
    datetime.datetime()

def datetime_timedelta():
    """
    class datetime.timedelta
        A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
    """

def main():
    date1 = datetime.date(2023, 6, 17)
    date2 = datetime.date(2023, 6, 15)
    timedelta1 = date1 - date2

    print(timedelta1.days)
    

if __name__ == "__main__":
    main()