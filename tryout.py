product = {}

product_id = input("Enter product id: ")
product_type = input("Enter product type: ")
product_name = input("Enter product: ")
product_amount = input("Enter product amount: ")

product.update({
    'Product_id': product_id,
    'Product_type' : product_type,
    'Product_name' : product_name,
    'Product_amount' : product_amount
})

print(product)