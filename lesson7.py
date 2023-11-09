import datetime as dt

birthday_str = input("Enter your birthday like year, month, day (F.e: 1999 08 17): ")
birthday = dt.datetime.strptime(birthday_str, "%Y %m %d")
present_day = dt.datetime.now()
diff = present_day - birthday

seconds = diff.total_seconds() 
minutes = seconds / 60 
hours = minutes / 60 
days = diff.days 
months = days / 30 
years = days / 365 

print(f"You are living "
      f"{seconds:.0f} second, "
      f"{minutes:.0f} minute, "
      f"{hours:.0f} hour, "
      f"{days} day and {months:.0f} month.")
print(f"Your old is {years:.0f}.")