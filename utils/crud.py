def read(users: list[dict[str,str]])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opulikował {user['post']} posty')

def add_user(lista: list) -> None:
        user_name = input('podaj imię:')
        user_surname = input('podaj nazwisko:')
        user_post = input('podaj ile postów:')
        lista.append({'name': user_name, 'surname': user_surname, 'post': user_post})