#eps growth of the last five years
year1 = float(input())

year5 = float(input())

windage_growth_rate = (year1-year5)/ year5
highest_pe = float(input())
if windage_growth_rate * 2 < highest_pe:
    windage_pe = windage_growth_rate
else:
    windage_pe = highest_pe

rate_of_return = 15
year = int(input('how many years from now do you want to predict the price'))
future_eps = year1
i = 1
while i <=year:
    future_eps = future_eps * (1+ windage_growth_rate)
    i+=1
print(future_eps)
future_share_price = future_eps * windage_pe
print(future_share_price)
sticker_price = future_share_price/(1.15)**year
print(sticker_price)
margin_of_safety = sticker_price/2
print(margin_of_safety)

