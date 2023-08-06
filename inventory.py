import json
class inventory:
    def __init__(self,product_id,product_name,product_type,product_price,title,choice,container):
        self.product_dict = container
        self.id = product_id
        self.name = product_name
        self.type = product_type
        self.price = product_price
        self.title = title
        self.choice = choice
    def title(self):
        self.title = "Inventory Management System"
        print(self.title)
    def add_product(self):
        self.id = int(input("Enter Product ID: "))
        self.name = input("Enter Product Name: ")
        self.type = input("Enter Product Type: ")
        self.price = int(input("Enter Product Price: "))
        self.product_list = {}
        self.product_list.update({
            "ID": self.id,
            "Product Name": self.name,
            "Product Type": self.type,
            "Product Price": self.price
        })

        with open("products.txt","a")as file:
            file.write(json.dumps(self.product_list) + '\n')

    def remove_product(self):
        pass
    def inventory(self):
        pass
    def main(self):
        while True:
            title()
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Inventory")
            print("q. Quit")
            self.choice = input(">")

            if self.choice == "1":
                add_product()
            elif self.choice == "2":
                remove_product()
            elif self.choice == "3":
                inventory()
            elif self.choice == "q" or self.choice == "Q":
                break
            else:
                print("Invalid input, try again!")

if __name__== "main()":
    main()