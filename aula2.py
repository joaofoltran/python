good_credit = True
house_price = 1000000

def calc_percentage(value,percent):
	return (value * percent) / 100

if good_credit:
	down_payment = calc_percentage(house_price,10)
else:
	down_payment = calc_percentage(house_price,20)

print(f"Down payment: ${down_payment}")