from psycopg2 import connect
from DataBase.operation_DB.create_tables import CreateTables
from DataBase.operation_DB.add_info import AddInfo
from DataBase.operation_DB.update_info import UpdateInfo
from DataBase.operation_DB.delete_info import DeleteInfo


def create_tables():
    with connect(database='doc_manager', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            drop = CreateTables(cur)
            drop.drop_tables()

            create = CreateTables(cur)
            create.create_table()


def add_info():
    with connect(database='doc_manager', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            command = input('Ввести данные компании [company] или договора (contract): ')
            if command == 'company':
                company_name = input('Введите название компании: ')
                inn = input('Введите ИНН компании: ')
                ogrn = input('Введите ОГРН компании: ')
                signer = input('Введите подписанта (ФИО): ')
                authority = input('Введите основание подписи: ')

                company_info = AddInfo(cur)
                company_info.add_company_info(company_name, inn, ogrn, signer, authority)

            elif command == 'contract':
                series = input('Введите серию договора: ')
                number = input('Введите номер договора: ')
                version = input('Введите версию договора: ')
                title = input('Введите тему договора: ')
                cost = input('Введите стоимость по договору: ')
                customer = input('Введите Заказчика: ')
                executor = input('Введите Исполнителя: ')

                contract_info = AddInfo(cur)
                contract_info.add_contract_info(series, number, version, title, cost, customer, executor)

            elif command == 'approver':
                employee_name = input('Введите ФИО сотрудника: ')
                department = input('Введите название офиса сотрудника: ')
                approve = AddInfo(cur)
                approve.add_approver_info(employee_name, department)


def update_info():
    with connect(database='doc_manager', user='postgres', password='postgres') as conn:
        with conn.cursor() as cur:
            update = UpdateInfo(cur)
            update.update_approver_info()
            update.update_company_info()
            update.update_contract_info()
