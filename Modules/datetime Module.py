import datetime

date=datetime.date(2025,8,21)           #gives us the date passed in the arguments
print("Date given in Arguments-----> ",date,"\n")

today=datetime.date.today()                             #gives us the current date
print("Today's date----->",today,"\n")

time=datetime.time(13,45)                   #gives us the time passed in the arguments
print("Time given in Arguments----->",time,"\n")

now=datetime.datetime.now()                             #gives us the current time and date
print("Current date & time----->",now,"\n")

# We can also change the format of how the time and date are shown

print("modified format")

now=now.strftime("%H:%M:%S %d/%m/%Y")
print(now)

# The arguments in "strftime" can be changed according to the requirements.
# Here's a breakdown of common "strftime" format codes:
# Year:
# %Y: Year with century (e.g., 2023).
# %y: Year without century (e.g., 23).

# Month:
# %m: Month as a zero-padded decimal number (01-12).
# %b: Abbreviated month name (e.g., Jan, Feb).
# %B: Full month name (e.g., January, February).
# %h: Abbreviated month name (same as %b).

# Day:
# %d: Day of the month as a zero-padded decimal number (01-31).
# %e: Day of the month as a decimal number (1-31), with a space preceding single digits.
# %j: Day of the year as a zero-padded decimal number (001-366).
# %w: Day of the week as a decimal number (0-6, Sunday is 0).
# %u: Day of the week as a decimal number (1-7, Monday is 1).

# Time:
# %H: Hour (24-hour clock) as a zero-padded decimal number (00-23).
# %I: Hour (12-hour clock) as a zero-padded decimal number (01-12).
# %M: Minute as a zero-padded decimal number (00-59).
# %S: Second as a zero-padded decimal number (00-59).
# %X: Preferred time representation for the current locale without the date.
# %r: Time in a.m. or p.m. notation (e.g., 02:30:00 PM).
# %R: Time in 24-hour notation (e.g., 14:30).
# %T: Time in 24-hour notation, including seconds (e.g., 14:30:00).

# Other:
# %a: Abbreviated weekday name (e.g., Sun, Mon).
# %A: Full weekday name (e.g., Sunday, Monday).
# %c: Preferred date and time representation for the current locale.
# %x: Preferred date representation for the current locale without the time.
# %Z: Time zone name or abbreviation.
# %z: Time zone as hour offset from GMT.
# %p: AM or PM.
# %%: A literal '%' character.

#We can also use comparison operators between datetime objects in datetime
# (Note that the class should be same between comparisons)
target_time=datetime.datetime(2025,1,12,14,12,14)
current_time=datetime.datetime.now()

if current_time > target_time:
    print("Current time is after target time")
else:
    print("Current time is before target time")


from datetime import date
d=date(2025,3,4)
print(d)
print(d.year)
print(d.month)
print(d.day)

today_date=date.today()
print(today_date)

from datetime import time

t=time(13,45,59)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

from datetime import datetime
t_now=datetime.now().time()
print(t_now)


from datetime import timedelta,date

Date_today=date.today()
delta_days=timedelta(days=30)
days_addition=Date_today + delta_days
print(days_addition)
days_subtraction=Date_today - delta_days
print(days_subtraction)

time_now=datetime.now()
delta_minutes=timedelta(minutes=30)
print(time_now + delta_minutes)


# days,seconds,microseconds,milliseconds,minutes,hours,weeks   can be used in arguments of timedelta

