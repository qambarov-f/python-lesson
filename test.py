# # from datetime import datetime


# # today = datetime.now()

# # print(today)

# # birth_date = datetime(1999, 8, 17)


# # old = today - birth_date


# # print("Your birth:", old.days, "")


# from datetime import datetime


# birth_date = datetime(1999, 8, 17, 18, 17, 0)


# today = datetime.now()


# pass_time = today - birth_date


# second = pass_time.total_seconds()
# minute = second / 60
# hour = minute / 60
# day = hour / 24


# old = today.year - birth_date.year


# print("How many second you're living:", second)
# print("How many minute you're living:", minute)
# print("How many hour you're living", hour)
# print("How many day you're living:", day)
# print("Your old is:", old)


from datetime import datetime


birth_date = datetime(datetime.now().year, 8, 17)


today = datetime.now()


if today > birth_date:
    
    birth_date = datetime(datetime.now().year + 1, 8, 11)

left_day = (birth_date - today).days


print( left_day , "days left until your birthday")

