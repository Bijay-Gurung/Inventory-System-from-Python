import json
product = {}
def welcome():
    print("Welcome to Inventory System!")

def add_product(product):
    print("Here you can Add Product")

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
        file.write(json.dumps(product) + '\n')
def remove_product():
    print("Here you can remove product")
    product_id = input("Enter Product Id to remove: ")
    products = []

    with open('products.txt', 'r') as file:
        for line in file:
            product = json.loads(line)
            if product['Product_id'] == product_id:
                print(f"Removed product with ID {product_id}: {product}")
            else:
                products.append(product)

    with open('products.txt', 'w') as file:
        for product in products:
            file.write(json.dumps(product) + '\n')


def search_product():
    with open('products.txt','r')as file:
        for line in file:
            product = json.loads(line)
            print(product)

def main():
    while True:
        welcome()
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("q. Quit")

        choice = input(">")

        if choice == "1":
            add_product(product)
        elif choice == "2":
            remove_product()
        elif choice == "3":
            search_product()
        elif choice == "q":
            break
        else:
            print("Invalid choice, please try again!")
if __name__ == '__main__':
    main()