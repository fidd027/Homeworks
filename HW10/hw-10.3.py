# 3. მოცემულია პროდუქტების ლისტი:
#
#    products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]
#
# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},

]

fltr = filter(lambda product: product["price"] < 100, products)

print(f"price < 100:  + {list(fltr)}")

mapp = map(lambda product: product["name"] + ' ' +  str(product['price']), products)

print(list(mapp))

sorting = sorted(products, key=lambda product: product["price"])

print(sorting)

lst_of_prices = map(lambda product: product['price'], products)

rdc = reduce(lambda x, y: x + y , lst_of_prices)
print(rdc)

