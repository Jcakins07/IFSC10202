total_seconds = int(input("Enter Length of Time in Seconds: "))

seconds_in_year = 31536000
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

years = days = hours = minutes = seconds = 0

if total_seconds >= seconds_in_year:
    years = total_seconds // seconds_in_year
    total_seconds = total_seconds % seconds_in_year

if total_seconds >= seconds_in_day:
    days = total_seconds // seconds_in_day
    total_seconds = total_seconds - (days * seconds_in_day)

if total_seconds >= seconds_in_hour:
    hours = total_seconds // seconds_in_hour
    total_seconds = total_seconds - (hours * seconds_in_hour)

if total_seconds >= seconds_in_minute:
    minutes = total_seconds // seconds_in_minute
    total_seconds = total_seconds - (minutes * seconds_in_minute)

seconds = total_seconds


print("years", years)
print("days", days)
print("hours", hours)
print("minutes", minutes)
print("seconds", seconds)
