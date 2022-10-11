import datetime

holidays = [
	(1, 1),
	(3, 15),
	(5, 1),
	(8, 20),
	(10, 23),
	(11, 1),
	(12, 25),
	(12, 26)
]

weekend_days = { 5, 6 }

def is_weekend(year: int, holiday_tuple):
	month, day = holiday_tuple
	return datetime.datetime(year, month, day).weekday() in weekend_days

for year in range(2022, 2422):
	weekend_holidays = filter(lambda holiday: is_weekend(year, holiday), holidays)
	print(f'{year}: {len(list(weekend_holidays))}')