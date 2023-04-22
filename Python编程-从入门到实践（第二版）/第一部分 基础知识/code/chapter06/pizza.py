# 存储所点的比萨的信息。
pizza = {
    'crust': 'thick',  # 外皮类型
    'toppings': ['mushrooms', 'extra cheese'],  # 配料列表
}

# 概述所点的比萨。
print(
    f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)
