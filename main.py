from psycopg2 import *

def creating_database():
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    conn.autocommit = True
    db_name = input('Jak chcesz zeby sie nazywala twoja baza danych? ')
    query = "CREATE DATABASE {};".format(db_name)
    cur.execute(query)
    print(f'Baza danych o nazwie {db_name} została pomyślnie dodana')
    conn.commit()
    conn.close()

def delete_database():
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    conn.autocommit = True
    db_name = input('Jaką bazę danych chcesz usunąć? ')
    query = f"DROP DATABASE IF EXISTS {db_name}"
    cur.execute(query)
    print(f'Baza danych o nazwie {db_name} została pomyślnie usunięta')
    conn.commit()
    conn.close()


def creating_table():
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    conn.autocommit = True
    db_name = input('Jak nazywa się baza danych, w której chcesz dodać tabelę? ')
    table_name = input('Jaką tabelę chcesz dodać? ')

    num_columns = int(input('Ile kolumn ma mieć tabela? '))
    columns = []
    for i in range(num_columns):
        column_name = input(f'Podaj nazwę {i + 1}. kolumny: ')
        data_type = input(f'Podaj typ danych kolumny {column_name} (np. VARCHAR(50)): ')
        columns.append((column_name, data_type))

    columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])

    query = f"CREATE TABLE {table_name}({columns_str});"
    cur.execute(query)
    print(f'Tabela {table_name} została pomyślnie dodana do bazy danych {db_name}.')
    conn.commit()
    conn.close()


def insert_data():
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    conn.autocommit = True
    table_name = input('Do jakiej tabeli chcesz dodać dane? ')
    num_values = int(input('Ile wartości chcesz dodać? '))
    values = []
    for i in range(num_values):
        value = input(f'Podaj wartość {i + 1}: ')
        values.append(value)

    values_str = ', '.join([f"'{value}'" for value in values])

    query = f"INSERT INTO {table_name} VALUES ({values_str})"
    cur.execute(query)
    print(f'{num_values} wartości zostały pomyślnie dodane do tabeli {table_name}.')
    conn.commit()
    conn.close()

def delete_table():
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    conn.autocommit = True
    db_name = input('Z której bazy danych chcesz usunąć tabelę? ')
    table_name = input('Jaką tabelę chcesz usunąć? ')
    query = f"DROP TABLE IF EXISTS {table_name};"
    cur.execute(query)
    print(f'Tabela {table_name} została pomyślnie usunięta z bazy danych {db_name}.')
    conn.commit()
    conn.close()
def execute_query(query):
    conn = connect(dbname='postgres', user='postgres', password='123', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    conn.commit()
    conn.close()
    return results

def show_tables():
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    results = execute_query(query)
    print("Dostępne tabele w bazie danych:")
    for row in results:
        print(row[0])

def custom_query():
    query = input("Wpisz zapytanie SQL: ")
    results = execute_query(query)
    if results:
        for row in results:
            print(row)
    else:
        print("Brak wyników")
