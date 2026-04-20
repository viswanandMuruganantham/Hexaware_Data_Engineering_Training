def calculate_revenue(orders, products):
    total_revenue = 0
    revenue_per_product = {}

    for o in orders:
        pid = o["product_id"]
        qty = o["quantity"]

        price = products[pid]["price"]
        product_name = products[pid]["name"]

        revenue = price * qty
        total_revenue += revenue

        revenue_per_product[product_name] = revenue_per_product.get(product_name, 0) + revenue

    highest_product = max(revenue_per_product, key=revenue_per_product.get)

    return total_revenue, revenue_per_product, highest_product


def customer_spending(orders, products):
    spending = {}

    for o in orders:
        customer = o["customer"]
        pid = o["product_id"]
        qty = o["quantity"]

        amount = products[pid]["price"] * qty

        spending[customer] = spending.get(customer, 0) + amount

    top_customer = max(spending, key=spending.get)

    return spending, top_customer


def advanced_analysis(visits, orders):
    visit_set = set(visits)
    order_customers = set(o["customer"] for o in orders)

    # Task 29
    visited_not_ordered = visit_set - order_customers

    # Task 30
    visit_count = {}
    for v in visits:
        visit_count[v] = visit_count.get(v, 0) + 1

    ordered_once_visitors = [
        c for c in order_customers if visit_count.get(c, 0) <= 1
    ]

    return visited_not_ordered, ordered_once_visitors