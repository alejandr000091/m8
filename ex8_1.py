from datetime import datetime

date = "2020-10-09"
def get_days_from_today(date):
    current_datetime = datetime.now()
    #print(current_datetime.date())  # 2020-10-09
    d1 = date.split("-")
    #print(type(int(d1[0])))
    prev_data = datetime(year=(int(d1[0])), month=(int(d1[1])), day=(int(d1[2])))
    prev_data.date()
    #print(current_datetime.date() - prev_data.date())
    result = current_datetime.date() - prev_data.date()
    #print(result.days)
    result = result.days
    return result

print(get_days_from_today(date))