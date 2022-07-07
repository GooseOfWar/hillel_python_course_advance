from unittest import TestCase, main
from HW_3.utils import DBOperator, DBFunctions


class DBO_test(TestCase):

    def test_create_new_db(self):
        new_db = DBFunctions()
        result = new_db._create_new_db()
        self.assertEqual(result, "Oh, sims table New_table already exists")

    def test_create_data_db(self):
        new_data = DBOperator(data=("Valley", '+262 656 6859'))
        result = new_data.set_db('-c')
        self.assertEqual(result, "A little bird told me "
                                 "UNIQUE constraint failed: New_table.Name")

    def test_read_db(self):
        read_data = DBOperator()
        result = read_data.set_db()
        self.assertIn("Valley", result)
        self.assertNotIn("Vall11ey", result)

    def test_update_db(self):
        old_data = DBOperator(data=("Smith", '025-5556 6859'))
        old_data.set_db('-c')
        result = old_data.set_db('-u', name="Smith", new_phone='+038 653658 59 59')
        self.assertEqual(result, 'Data updated successfully')

    def test_delete_data_db(self):
        old_data = DBOperator(data=("Kapitan Morshina", '025-55'))
        old_data.set_db('-c')
        result = old_data.set_db('-d', delete='Kapitan Morshina')
        self.assertEqual(result, 'Data was Deleted')


if __name__ == '__main__':
    main()
