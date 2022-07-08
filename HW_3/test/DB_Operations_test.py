from unittest import TestCase, main

from HW_3.utils import DBOperator, DBFunctions


class DBO_test(TestCase):

    def test_create_new_db(self):
        """Test case: Create new db with table"""
        new_db = DBFunctions()
        result = new_db._create_new_db()
        self.assertEqual(result, "Oh, sims table New_table already exists")

    def test_create_data_db(self):
        """Test case: create new data"""
        new_data = DBOperator()
        result = new_data.set_db('-c', data=("Valley", '+262 656 6859'))
        self.assertEqual(result, "A little bird told me "
                                 "UNIQUE constraint failed: New_table.Name")

    def test_read_db(self):
        """Test case: read data"""
        read_data = DBOperator()
        result = read_data.set_db()
        self.assertIn("Valley", result)
        self.assertNotIn("Vall11ey", result)

    def test_update_db(self):
        """Test case: update data"""
        old_data = DBOperator()
        old_data.set_db('-c', data=("Smith", '025-5556 6859'))
        result = old_data.set_db('-u', name="Smith", new_phone='+038 653658 59 59')
        self.assertEqual(result, 'Smith Data successfully updated to +038 653658 59 59')

    def test_delete_data_db(self):
        """Test case: delete data"""
        old_data = DBOperator()
        old_data.set_db('-c', data=("Kapitan Morshina", '025-55'))
        result = old_data.set_db('-d', delete='Kapitan Morshina')
        self.assertEqual(result, 'For Kapitan Morshina data was Deleted')

    def test_delete_data_2_db(self):
        """Test case: invalid Input"""
        old_data = DBOperator()
        old_data.set_db('-c', data=("Kapitan Morshina", '025-55'))
        result = old_data.set_db('-d', delete=1)
        self.assertEqual(result, 'Invalid type ')

    def test_set_db(self):
        """Test case: invalid flag"""
        new_data = DBOperator()
        result = new_data.set_db('l')
        self.assertEqual(result, "Invalid input Data 'l'")


if __name__ == '__main__':
    main()
