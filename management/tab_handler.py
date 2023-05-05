from menu import products
import math

# products_consumed = [{"_id": 50, "amount": 5 }]


def calculate_tab(products_consumed):
    prices = []
    for product in products_consumed:
        for pedido in products:
            if pedido.get("_id") == product["_id"]:
                prices_times_amount = round(pedido["price"] * product["amount"], 2)
                prices.append(prices_times_amount)
                price_total = round(sum(prices), 2)
                subtotal = {"sobtotal": f"${price_total}"}
    return subtotal
