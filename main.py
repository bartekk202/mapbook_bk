users:list = [
    {"name":"Bartek","location":"Giżycko","posts":400},
    {"name":"Krzysztof","location":"Białobrzegi","posts":500},
    {"name":"Maja","location":"Świecie","posts":300},
    {"name":"Zuzanna","location":"Radzyń_Podlaski","posts":700},
]



def get_user_info(users_data:list)->None:


    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów")

get_user_info(users)