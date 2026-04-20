import csv

def load_orders(filename):
    orders = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            orders.append({
                "order_id": int(row["order_id"]),
                "customer": row["customer"],
                "product_id": int(row["product_id"]),
                "quantity": int(row["quantity"])
            })

    return orders


def analyze_orders(orders):
    quantity_per_product = {}
    orders_per_customer = {}

    for o in orders:
        pid = o["product_id"]
        customer = o["customer"]

        quantity_per_product[pid] = quantity_per_product.get(pid, 0) + o["quantity"]
        orders_per_customer[customer] = orders_per_customer.get(customer, 0) + 1

    return quantity_per_product, orders_per_customer