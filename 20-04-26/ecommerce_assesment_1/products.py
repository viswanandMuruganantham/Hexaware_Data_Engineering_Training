import json

def load_products(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    product_dict = {}

    for p in data["products"]:
        product_dict[p["product_id"]] = {
            "name": p["name"],
            "price": p["price"]
        }

    return product_dict


def analyze_products(product_dict):
    most_expensive = max(product_dict.items(), key=lambda x: x[1]["price"])
    least_expensive = min(product_dict.items(), key=lambda x: x[1]["price"])

    return most_expensive, least_expensive