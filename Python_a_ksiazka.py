pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser'],
}

print(f"Zamowiles pizze na {pizza['crust']} cieście "
      f"wraz z następującymi dodatkami:")
for topping in pizza['toppings']:
    print(f"\t{topping}")