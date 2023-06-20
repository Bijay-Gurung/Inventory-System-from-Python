def welcome():
    print("Welcome to Inventory System!")

def add_product():
    welcome()

    product = {}

    product_id = input("Enter Product Id: ")
    product_type = input("Enter Product Type: ")
    product_name = input("Enter Product Name: ")
    product_amount = input("Enter Product Amount: ")

    product.update({
        'Product_id' : product_id,
        'Product_type' : product_type,
        'Product_name' : product_name,
        'Product_amount' : product_amount
    })

    print(product)

add_product()

