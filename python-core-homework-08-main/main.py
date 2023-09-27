from datetime import date, datetime


def get_birthdays_per_week(users):
    print(date.today)
    return users


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
