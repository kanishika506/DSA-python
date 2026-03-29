price=[]
min_price=price[0]
max_profit=0
for i in price:
	if i< min_price:
		min_price=i
	if i-min_price>max_profit:
		max_profit=i-min_price
return max_price
