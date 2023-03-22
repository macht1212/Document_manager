class AddInfo:

    def __init__(self, cur):
        self.cur = cur

    def add_company_info(self, company_name, inn, ogrn, signer, authority):
        self.cur.execute('''
        INSERT INTO company_info (company_name, inn, ogrn, signer, authority)
            VALUES (%s, %s, %s, %s, %s);
        ''', (company_name, inn, ogrn, signer, authority,))

    def get_company_id(self, company_name):
        self.cur.execute('''
        SELECT company_id FROM company_info
        WHERE company_name = %s
        ''', (company_name,))
        return self.cur.fetchone()

    def add_contract_info(self, series, number, version, title, cost, customer, executor):
        self.cur.execute('''
        INSERT INTO contract_info (series, number, version, title, cost, customer, executor)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        ''', (series, number, version, title, cost, customer.get_company_id(self.cur, customer),
              executor.get_company_id(self.cur, executor)))

    def add_approver_info(self, employee_name, department):
        self.cur.execute('''
        INSERT INTO approves (employee_name, department)
            VALUES (%s, %s);
        ''', (employee_name, department, ))


