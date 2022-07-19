import psycopg2
import os

DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')

class Conexao():
    
    def new_conn(self):
        return psycopg2.connect(host=DB_HOST, port=DB_PORT,database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

    def insert_account(self, user, pwd):
        try:
            connection = self.new_conn()
            cursor = connection.cursor()
            sql_command = "INSERT INTO accounts (username, password) VALUES (%s, %s);"
            cursor.execute(sql_command, (user, pwd))
            connection.commit()
            cursor.close()
            print("Account created sucessfully")
        except (Exception, psycopg2.Error) as error:
            print("Failed to create account ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def select_all_account(self):
        try:
            connection = self.new_conn()
            cursor = connection.cursor()
            sql_command = "SELECT * FROM accounts"
            cursor.execute(sql_command)
            all_accounts = cursor.fetchall()
            return(all_accounts)

        except (Exception, psycopg2.Error) as error:
            print("Error when fetching data ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def test_insert(self, text:str):
        try:
            connection = psycopg2.connect(host=DB_HOST, port=DB_PORT,database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
            cursor = connection.cursor()
            sql_command = "INSERT INTO teste (texto) VALUES (%s);"
            cursor.execute(sql_command, (text,))
            connection.commit()
            cursor.close()
            print("Closed")
        except (Exception, psycopg2.Error) as error:
            print("Failed to create account ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def test_select(self):
        try:
            connection = self.new_conn()
            cursor = connection.cursor()
            sql_command = "SELECT * FROM teste"
            cursor.execute(sql_command)
            all_accounts = cursor.fetchall()

            for row in all_accounts:
                print(row)
        except (Exception, psycopg2.Error) as error:
            print("Error when fetching data ", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

_inst = Conexao()
new_acc = _inst.insert_account
get_usr = _inst.select_all_account
