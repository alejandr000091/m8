from datetime import datetime
import re

data_transforn = "2021-05-27 17:08:34.149Z"

def get_str_date(date):
    date = re.sub(r" ", "-", date)
    new_date = date.split("-")
    return_date = datetime(year=int(new_date[0]), month=int(new_date[1]), day=int(new_date[2]))
    return return_date.date().strftime('%A %d %B %Y')

print(get_str_date(data_transforn))