users: list = [
    {"name": "Bartek", "location": "Ełk", "posts": 400}


]
print(users)

def remove_user(users_data: list)->None:

    user_name=input("podaj imie uzytkownika do usuniecia: ")
    for user in users:
        if user["name"] == user_name:
            users_data.remove(user)


remove_user(users)



print(users)

