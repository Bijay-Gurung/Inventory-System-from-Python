import json
class Inventory:
    def display_title(self):
        title = "Inventory Management System"
        print(title)

    def add_product(self):
        x = "Add product".center(50)
        print(x)
        product_id = int(input("Enter Product ID: "))
        product_name = input("Enter Product Name: ")
        product_type = input("Enter Product Type: ")
        product_price = int(input("Enter Product Price: "))

        product = {
            "ID": product_id,
            "Product Name": product_name,
            "Product Type": product_type,
            "Product Price": product_price
        }

        with open("products.txt", "a") as file:
            file.write(json.dumps(product) + '\n')
            print("Product added")

    def remove_product(self):
        x = "Remove Products".center(50)
        product_id = int(input("Enter Product ID to remove: "))
        lines = []

        with open("products.txt", "r") as file:
            for line in file:
                product = json.loads(line)
                if product["ID"] != product_id:
                    lines.append(line)

        with open("products.txt", "w") as file:
            file.writelines(lines)
            print("Product removed")

    def display_inventory(self):
        with open("products.txt", "r") as file:
            for line in file:
                product = json.loads(line)
                print("ID:", product.get("ID", "N/A"))
                print("Name:", product.get("Product Name", "N/A"))
                print("Type:", product.get("Product Type", "N/A"))
                print("Price:", product.get("Product Price", "N/A"))
                print()

    def main(self):
        while True:
            self.display_title()
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Display Inventory")
            print("q. Quit")
            self.choice = input("> ")

            if self.choice == "1":
                self.add_product()
            elif self.choice == "2":
                self.remove_product()
            elif self.choice == "3":
                self.display_inventory()
            elif self.choice == "q" or self.choice == "Q":
                break
            else:
                print("Invalid input, try again!")


if __name__ == "__main__":
    inventory_system = Inventory()
    inventory_system.main()
