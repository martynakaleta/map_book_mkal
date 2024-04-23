def read(users: list[dict[str,str]])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['name']} opulikował {user['post']} posty')

def add_user(lista: list) -> None:
        user_name = input('podaj imię:')
        user_surname = input('podaj nazwisko:')
        user_post = input('podaj ile postów:')
        lista.append({'name': user_name, 'surname': user_surname, 'post': user_post})

 def search(users: list[dict[str, str]]) -> None:
         user_name = input('kogo szukasz?')
            for user in users[1:]:
                if user['name'] == user_name:
                    print(f'znaleziono użytkownika {user}')

def remove_user(users: list[dict[str,str]])->None:
    user_name=input('kogo usunąć?')
    for user in users[1:]:
        if user['name']==user_name:
            print(f'znaleziono użytkownika {user['name']}')
            users.remove(user)

def update_user(users: list[dict[str, str]]) -> None:
    user_name = input('kogo zaktualizować?')

    for user in users[1:]:
        if user['name'] == user_name:
            user['name'] = input('podaj nowe imie')
            user['surname'] = input('podaj nowe nazwisko')
            user['post'] = input('podaj nową liczbe postów')
