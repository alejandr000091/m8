from datetime import date, datetime

def get_current_day(number):
    if number == 1:
        return "Monday"
    if number == 2:
        return "Tuesday"
    if number == 3:
        return "Wednesday"
    if number == 4:
        return "Thursday"
    if number == 5:
        return "Friday"
    if number == 6:
        return "Saturday"
    if number == 7:
        return "Sunday"

def get_birthdays_per_week(users):
    current_date = date.today()
    print(current_date)
    current_date_day = current_date.isoweekday()
    print(get_current_day(current_date_day))

    test_date = date(2023, 10, 2)
    print(test_date)
    print(test_date.isoweekday())
    for user in users:
        user_data = (user["birthday"])
        #new_user_data = date("2023", user_data.month, user_data.day)
        print(user_data, type(user_data))

        d1 = date(year=2023, month=user_data.month , day=user_data.day)
        print(d1) # 2012-01-07 14:00:00
        print(user["birthday"], user["name"])
    #return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "A G", "birthday": datetime(1993, 9, 18).date()},
        {"name": "В понеділок привітати, ДН вихдний", "birthday": datetime(1993, 9, 30).date()},
        {"name": "В четвер привітати", "birthday": datetime(1993, 10, 5).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
