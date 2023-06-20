product = {}
def welcome():
    print("Welcome to Inventory System!")

def add_product(product):
    welcome()

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

    with open('products.txt','a')as file:
        file.write(str(product))
add_product(product)
def remove_product():
    pass

def search_product():
    with open('products.txt','r')as file:
        for line in file:
            print(line.strip())
search_product()
