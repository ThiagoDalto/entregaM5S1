from menu import products
from statistics import mode


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(tipo: str):
    listed_products_by_type = []
    if type(tipo) != str:
        raise TypeError("product type must be a str")
    for product in products:
        if product.get('type') == tipo:
            listed_products_by_type.append(product)       
    return listed_products_by_type


def menu_report():
    counted_products = len(products)
    sum_price = 0
    values_type = []
    for product in products:
        price = product["price"]
        sum_price += price
        values_type.append(product["type"])
    average_price = round(sum_price / counted_products, 2)
    most_commom = mode(values_type)

    return f"Products Count: {counted_products} - Average Price: {average_price} - Most Common Type: {most_commom}"


def add_product(menu, **new_register):
    values_id = []
    if menu == []:
        new_register["_id"] = 1
        return new_register        
    for product in menu:
        values_id.append(product["_id"])
    max_value = max(int(value) for value in values_id)
    new_register["_id"] = max_value + 1
    products.append(new_register)
    return new_register
