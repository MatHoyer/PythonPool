from datetime import datetime

def convertMonth(month: int):
    months = {
		1: 'January',
		2: 'February',
		3: 'March',
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'August',
		9: 'September',
		10: 'October',
		11: 'November',
		12: 'December'
	}
    return months[month]

dateComp = { 'day': 1, 'month': 1, 'year': 1970 }
dateToday = datetime.now()

dateCompValue = datetime(dateComp['year'], dateComp['month'], dateComp['day'])
dateCompToday = datetime(dateToday.year, dateToday.month, dateToday.day, dateToday.hour, dateToday.minute, dateToday.second, dateToday.microsecond)

# Calculer la différence entre les deux dates
diff = dateCompToday - dateCompValue

print('Seconds since ' + convertMonth(dateComp['month']) + ' ' + str(dateComp['day']) + ' ' + str(dateComp['year']) + ': ' + '{:,.4f}'.format(diff.total_seconds()) + ' or ' + '{:.2e}'.format(diff.total_seconds()) + ' in scientific notation')
print(dateCompToday.strftime("%b %d %Y"))