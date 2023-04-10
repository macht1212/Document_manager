class UpdateInfo:

    def __init__(self, cur):
        self.cur = cur

    def company_id(self, company_name, inn):

        self.cur.execute(f"""
        SELECT company_id FROM company_info WHERE company_name = %s AND inn = %s;
        """, (company_name, inn))

        return self.cur.fetchone()[0]

    def update_company_info(self, company_name, inn, company_name_new=None, inn_new=None, ogrn=None, signer=None, authority=None):
        list_of_values = []
        if company_name_new:
            list_of_values.append(company_name_new)
        if inn_new:
            list_of_values.append(inn_new)
        if ogrn:
            list_of_values.append(ogrn)
        if signer:
            list_of_values.append(signer)
        if authority:
            list_of_values.append(authority)

        list_of_keys = []
        if company_name_new:
            list_of_keys.append('company_name')
        if inn_new:
            list_of_keys.append('inn')
        if ogrn:
            list_of_keys.append('ogrn')
        if signer:
            list_of_keys.append('signer')
        if authority:
            list_of_keys.append('authority')

        company_id = self.company_id(company_name, inn)

        keys_str = ', '.join(list_of_keys)
        values_str = ', '.join(list_of_values)

        self.cur.execute(f"""
        UPDATE company_info SET ({keys_str}) = ({values_str}) WHERE company_id = %s;
        """, (company_id, ))

        print('Данные изменены')



    def update_contract_info(self):
        pass

    def update_approver_info(self):
        pass
