import sqlite3
from time import sleep


class DBFunctions():
    CON = 'my_dear_db.db'

    def __init__(self, data: list or tuple = None):
        self.data = data

    def _create_new_db(self):
        con = sqlite3.connect(DBFunctions.CON)
        try:
            cur = con.cursor()
            cur.execute(f'''CREATE TABLE New_table (Name varchar(128) UNIQUE, Phone varchar(128))''')
            con.commit()
        except sqlite3.OperationalError as error:
            con.close()
            return f'Oh, sims {error}'
        con.close()
        return "Data Base created Successfully"

    def create_data_db(self, **kwargs):
        """Create new data in DB"""
        con = sqlite3.connect(DBFunctions.CON)
        try:
            cur = con.cursor()
            sql = f'''
            INSERT INTO New_table
            VALUES ('{self.data[0]}', '{self.data[1]}');
            '''
            cur.execute(sql)
            con.commit()
        except sqlite3.IntegrityError as error:
            con.close()
            return f'A little bird told me {error}'
        con.close()
        return "Data created"

    def read_db(self, **kwargs):
        """Read data in DB"""
        con = sqlite3.connect(DBFunctions.CON)
        try:
            cur = con.cursor()
            sql = 'SELECT * FROM New_Table;'
            cur.execute(sql)
            data = cur.fetchall()
        finally:
            con.close()
        return data.__str__()

    def update_db(self, name, new_phone, **kwargs):
        """Update data in DB"""
        con = sqlite3.connect(DBFunctions.CON)
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
        return 'Data updated successfully'

    def delete_db(self, delete: str = None, **kwargs):
        """Delete specified data in DB"""
        con = sqlite3.connect(DBFunctions.CON)
        try:
            cur = con.cursor()
            sql = f'''
            DELETE FROM New_table WHERE Name == '{delete}';
            '''
            cur.execute(sql)
            con.commit()
        finally:
            con.close()
        return 'Data was Deleted'


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
        new_data = DBOperator(data=("Valley", '+262 656 6859'))
        result = new_data.set_db('-c')


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

    def __init__(self, data: list or tuple = None):
        super().__init__()
        self.data = data

    def set_db(self, flag: str = '-r', name=None, new_phone=None, delete=None):
        sleep(0.5)
        operations_set: dict = {'-c': self.create_data_db,
                                '-r': self.read_db,
                                '-u': self.update_db,
                                '-d': self.delete_db}

        return operations_set[flag](name=name,
                                    new_phone=new_phone,
                                    delete=delete)


if __name__ == '__main__':
    ...
