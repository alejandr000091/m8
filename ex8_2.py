from datetime import date

month = 2
year = 2024

def get_days_in_month(month, year):
    for day_n in range(27,33):
        try:
            prev_data = date(year=year, month=month, day=day_n)

            prev_data_ti_print = prev_data
        except:
            print(prev_data_ti_print.day)
            return prev_data_ti_print.day
            break

get_days_in_month(month, year)