from visits import load_visits, analyze_visits
from products import load_products, analyze_products
from orders import load_orders, analyze_orders
from analytics import calculate_revenue, customer_spending, advanced_analysis


def main():
    visits = load_visits("website_visits.txt")
    products = load_products("products.json")
    orders = load_orders("orders.csv")

    # Visits
    total_visits, unique_visitors, visit_count, most_frequent = analyze_visits(visits)

    # Products
    most_exp, least_exp = analyze_products(products)

    # Orders
    qty_per_product, orders_per_customer = analyze_orders(orders)

    # Revenue
    total_revenue, revenue_per_product, top_product = calculate_revenue(orders, products)

    # Customers
    spending, top_customer = customer_spending(orders, products)

    # Advanced
    visited_not_ordered, ordered_once_visitors = advanced_analysis(visits, orders)

    # Write report
    with open("sales_report.txt", "w", encoding="utf-8") as f:
        f.write("E-Commerce Sales Report\n")
        f.write(f"Total Website Visits: {total_visits}\n")
        f.write(f"Unique Visitors: {len(unique_visitors)}\n")
        f.write(f"Total Revenue: {total_revenue}\n\n")

        f.write(f"Top Customer: {top_customer}\n\n")

        f.write("Product Sales:\n")
        for product, revenue in revenue_per_product.items():
            f.write(f"{product} → {revenue}\n")

        f.write("\nVisitors who never ordered:\n")
        f.write(str(visited_not_ordered) + "\n")

        f.write("\nCustomers who ordered but visited once or less:\n")
        f.write(str(ordered_once_visitors) + "\n")


if __name__ == "__main__":
    main()