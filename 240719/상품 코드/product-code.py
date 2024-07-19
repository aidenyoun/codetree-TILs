class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

product1 = Product()
print(f"product {product1.code} is {product1.name}")
temp = input().split()
product2 = Product(temp[0], temp[1])
print(f"product {product2.code} is {product2.name}")