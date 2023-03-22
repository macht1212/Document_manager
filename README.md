# DOCUMENT MANAGER  
by Alex Nazimov

## Program Description  

The program accepts various data as input, which are then transferred to the Database and, if necessary, issued to the user.

## Implemented methods

### DataBase package
#### create_tables.py  
This module has ```class CreateTables``` which takes 'cur' (cursor) as an argument with 
two methods:
```python
.create_table()
``` 
- creates three tables (company_info, contract_info, 
approver_info)   
This class uses in ```def create_tables():``` (DB_main.py module)

```python
.drop_tables()
```
 - dropped all tables (if it necessary).

This class uses in ```def create_tables():``` (DB_main.py module)

#### add_info.py  
This module has ```class AddInfo``` which takes 'cur' (cursor) as an argument with four 
methods:  
```python
.add_company_info(company_name, inn, ogrn, signer, authority)
```
- method adds information about the company. Multiple parameters are accepted as input.

```python
.get_company_id()
```
- method is only used inside another method

```python
.add_contract_info(series, number, version, title, cost, customer, executor)
```
- method adds information about the contract. Multiple parameters are accepted as input.

```python
.add_approver_info(employee_name, department)
```
- method adds information about the approver. Two parameters are accepted as input.

#### 