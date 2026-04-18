orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]

total_spending_per_cust = {}
order_count = {}
for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    if customer in total_spending_per_cust:
        total_spending_per_cust[customer] += amount
        order_count[customer] += 1
    else:
        total_spending_per_cust[customer] = amount
        order_count[customer] = 1
print(total_spending_per_cust)

highest = max(total_spending_per_cust, key = total_spending_per_cust.get)
print(highest)

print(order_count)