class CreateTables:

    def __init__(self, cur):
        self.cur = cur

    def create_table(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS company_info(
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR UNIQUE NOT NULL,
            inn INTEGER NOT NULL,
            ogrn INTEGER NOT NULL,
            signer VARCHAR NOT NULL, 
            authority VARCHAR NOT NULL
        );
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS contract_info (
            contract_id SERIAL PRIMARY KEY,
            series VARCHAR NOT NULL,
            number INTEGER NOT NULL,
            version INTEGER NOT NULL,
            title VARCHAR NOT NULL,
            cost FLOAT NOT NULL,
            customer INTEGER NOT NULL REFERENCES company_info(company_id),
            executor INTEGER NOT NULL REFERENCES company_info(company_id),
            approver INTEGER NOT NULL REFERENCES approves(employee_id)
        );
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS approves (
        employee_id SERIAL PRIMARY KEY,
        employee_name VARCHAR NOT NULL UNIQUE,
        department VARCHAR NOT NULL UNIQUE
        );
        ''')

    def drop_tables(self):
        self.cur.execute('''
        DROP TABLE contract_info;
        ''')

        self.cur.execute('''
        DROP TABLE company_info;
         ''')

        self.cur.execute('''
        DROP TABLE approves;
        ''')

