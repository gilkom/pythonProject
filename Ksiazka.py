def describe_pet(pet_name, animal_type = 'pies'):
    print(f"\nMoje zwierze to {animal_type}.")
    print(f"Mój {animal_type} ma na imie {pet_name.title()}")

describe_pet(pet_name='harry', animal_type='chomik')
describe_pet('pies', 'willie')
describe_pet('toffi')