from database import get_products


data = get_products()


for i in data:
    print(i[2])

