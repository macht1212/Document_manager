from DataBase.DB_main import create_tables, add_info


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'create':
            create_tables()

        elif command == 'add info':
            add_info()

        elif command == 'update info':


        elif command == 'exit':
            exit()


if __name__ == '__main__':
    main()
