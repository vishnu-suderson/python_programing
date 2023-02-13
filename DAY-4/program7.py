cost_price = float(input("Enter the cost price of the bike: "))
if cost_price > 100000:
    road_tax = 0.15 * cost_price
elif cost_price > 50000 and cost_price <= 100000:
    road_tax = 0.1 * cost_price
elif cost_price <= 50000:
    road_tax = 0.05 * cost_price
else:
    print("Invalid cost price!")

print("Road tax to be paid: ", road_tax)
