from models.data import users
from utils.crud import read,add_user,search, remove_user


if __name__ == '__main__':
    print(f'witaj {users[0]['name']}')


    while True:

            print('0. zakończ program')
            print('1. wyświetl znajomych')
            print('2. dodaj znajomych')
            print('3. dodaj znajomego')
            print('4. usuń znajomego')
            menu_option=input('wybierz opcje menu:')
            if menu_option=='0': break
            if menu_option=='1': read(users)
            if menu_option=='2': add_user(users)
            if menu_option=='3': search(users)
            if menu_option=='4': remove_user(users)