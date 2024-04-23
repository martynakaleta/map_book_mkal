def read(users: list[dict[str,str]])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opulikował {user['post']} posty')