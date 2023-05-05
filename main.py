from management import get_product_by_id, get_products_by_type, menu_report, add_product, calculate_tab
from menu import products


def main():
    id = "1"
    tipo = 1
    try:
        get_products_by_type(tipo)
    except TypeError as error:
        print("TypeError tratado")
        print(error)
    try:
        get_product_by_id(id)
    except TypeError as error:
        print(error)
        print("TypeError Tratado")
    
    print("fim da função")


table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
if __name__ == "__main__":
    main()
    # Seus prints de teste aqui
    ...
   
