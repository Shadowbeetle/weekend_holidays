import datetime
from statistics import mean, median

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

yearly_weekend_holiday_number = []

for year in range(2022, 2422):
	weekend_holidays = list(filter(lambda holiday: is_weekend(year, holiday), holidays))
	num_weekend_holidays = len(weekend_holidays)

	yearly_weekend_holiday_number.append(num_weekend_holidays)

	print(f'{year}: {weekend_holidays}')
	
print(f'mean: {mean(yearly_weekend_holiday_number)}')
print(f'median: {median(yearly_weekend_holiday_number)}')