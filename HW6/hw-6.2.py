# 2. მოცემულია პროდუქტების ლისტი:

products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]


# ა. დაბეჭდეთ ყველა პროდუქტის დასახელება

# product_names = []
# for item in products:
#     product_names.append(list(item.keys()))
# print(f'Product names are: {product_names}')

product_names = [list(item.keys()) for item in products]
print(f'ა)Product names are: {product_names}')


# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)

value_dict = {}
for item in products:
    value_dict.update(item)

price = 0
for value in value_dict.values():
    price += value['price'] * value['quantity']
print(f'ბ)Total price for all the snacks and beverages is: {price}')






