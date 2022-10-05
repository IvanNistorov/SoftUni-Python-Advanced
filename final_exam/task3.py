def shopping_cart(*args):
    cart = {"Pizza": [],
            "Soup": [],
            "Dessert": [],
            }

    for el in range(0, len(args), 1):
        if args[el] == "Stop":
            break
        meal = args[el][0]
        product = args[el][1]
        if len(cart["Pizza"]) == 4 or product in cart["Pizza"]:
            continue
        elif len(cart["Soup"]) == 3 or product in cart["Soup"]:
            continue
        elif len(cart["Dessert"]) == 2 or product in cart["Dessert"]:
            continue

        if meal == "Pizza":
            cart["Pizza"].append(product)
        elif meal == "Soup":
            cart["Soup"].append(product)
        elif meal == "Dessert":
            cart["Dessert"].append(product)

    result = ""
    for key, value in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{key}:\n'
        for value_type in sorted(value):
            result += f' - {value_type}\n'

    return result.strip()


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
