"""
Module provide Data base operations
"""
import sqlite3
from time import sleep


class DBFunctions():
    """
    Class Provide CRUD functional with DB

    to create new DB:
         x = DBFunctions()
        x._create_new_db() - Create DB with table New_table and columns Name, Phone
        :return: "Data Base created Successfully" in first start


    to create new Data in table:
        x = DBFunctions()
        x.create_data_db(data = [Name, Phone])
        return "Data created"

    to read Data from DB:
        x = DBFunctions()
        x.read_db()
        :return: data.__str__()

    to update Data in DB:
        x = DBFunctions()
        x.update_db(Name, new_Phone)
        :return: 'Data updated successfully'

    to delete specified Data from DB:
        x = DBFunctions()
        x.delete_db(delete: str = None)
        :return: 'Data was Deleted'

    """
    CON = 'my_dear_db.db'  # DB file

    def _create_new_db(self):
        """
        ._create_new_db() - Create DB with table New_table and columns Name, Phone
        :return: "Data Base created Successfully" in first start
        """
        con = sqlite3.connect(DBFunctions.CON)  # connect to db
        try:
            cur = con.cursor()
            cur.execute('''CREATE TABLE New_table
             (Name varchar(128) UNIQUE, Phone varchar(128))''')
            con.commit()
        except sqlite3.OperationalError as error:
            con.close()
            return f'Oh, sims {error}'
        con.close()
        return "Data Base created Successfully"

    def create_data_db(self, data: list or tuple = None, **kwargs):
        """Create new data in New_table
        x = DBFunctions(data = [Name, Phone]
        x.create_data_db()
        """
        con = sqlite3.connect(DBFunctions.CON)  # connect to db
        try:
            cur = con.cursor()
            sql = f'''
            INSERT INTO New_table
            VALUES ('{data[0]}', '{data[1]}');
            '''
            cur.execute(sql)
            con.commit()
        except sqlite3.IntegrityError as error:
            con.close()
            return f'A little bird told me {error}'
        con.close()
        return f'{data[0]}:  {data[1]}  Successfully added to base'

    def read_db(self, **kwargs):
        """Read data in DB
        x = DBFunctions()
        x.read_db()
        :return: data.__str__()
        """
        con = sqlite3.connect(DBFunctions.CON)  # connect to db
        try:
            cur = con.cursor()
            sql = 'SELECT * FROM New_Table;'
            cur.execute(sql)
            data: list = cur.fetchall()
        finally:
            con.close()
        return data.__str__()

    def update_db(self, name, new_phone, **kwargs):
        """Update data in DB
        x = DBFunctions()
        x.update_db(Name, new_Phone)
        :return: 'Data updated successfully'
        """
        con = sqlite3.connect(DBFunctions.CON)  # connect to db
        try:
            cur = con.cursor()
            sql = f'''
            UPDATE New_table
            SET Phone = '{new_phone}'
            WHERE Name = '{name}';
            '''
            cur.execute(sql)
            con.commit()
        finally:
            con.close()
        return f'{name} Data successfully updated to {new_phone}'

    def delete_db(self, delete: str = None, **kwargs):
        """Delete specified data in DB
        x = DBFunctions()
        x.delete_db(delete: str = None)
        :return: 'Data was Deleted'
        """

        con = sqlite3.connect(DBFunctions.CON)  # connect to db
        try:
            if type(delete) != str:
                raise TypeError
            cur = con.cursor()
            sql = f'''
            DELETE FROM New_table WHERE Name == '{delete}';
            '''
            cur.execute(sql)
            con.commit()
        except TypeError as error:
            con.close()
            return f'Invalid type {error}'
        con.close()
        return f'For {delete} data was Deleted'


class DBOperator(DBFunctions):
    """
    Provide main simple main functional for CRUD ideology with DB

    Main functional:

    set_db(self, flag: str = '-r', [name=None, new_phone=None, [delete=None]])
    only 4 flag for all:'-c','-r','-u','-d'

    ENJOY!..Sorrrry)

    Create new DB:
        new_db = DBOperator()
        result = new_db._create_new_db()

    Create new Data in DB:
        new_data = DBOperator()
        result = new_data.set_db('-c', data=("Valley", '+262 656 6859'))


    Read DB:
        read_data = DBOperator()
        result = read_data.set_db()


    Update new DB:
        old_data = DBOperator(data=("Smith", '025-5556 6859'))
        old_data.set_db('-c')

        result = old_data.set_db('-u', name="Smith", new_phone='+038 653658 59 59')

    Delete data from DB:
        old_data = DBOperator(data=("Kapitan Morshina", '025-55'))
        old_data.set_db('-c')

        result = old_data.set_db('-d', delete='Kapitan Morshina')


    """

    def set_db(self, flag: str = '-r', data: list or tuple = None,
               name: str = None, new_phone: str = None, delete: str = None):
        """
        Function set operations with DB
        :param flag: only 4 flag for all:'-c','-r','-u','-d'
        :param data: data=("Valley", '+262 656 6859') (create)
        :param name: Name for which changes are being made (update)
        :param new_phone: New Phone (update)
        :param delete: Name for which data will be deleted
        """
        sleep(0.5)
        operations_set: dict = {'-c': self.create_data_db,
                                '-r': self.read_db,
                                '-u': self.update_db,
                                '-d': self.delete_db}
        try:
            result = operations_set[flag](data=data,
                                          name=name,
                                          new_phone=new_phone,
                                          delete=delete)
            return result
        except KeyError as error:
            return f'Invalid input Data {error}'


if __name__ == '__main__':
    ...
