unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Weryfikacja {current_user.title()}")

    confirmed_users.append(current_user)

print(f"\nZweryfikowan użytkownikow:")
for confirmed in confirmed_users:
    print(confirmed.title())