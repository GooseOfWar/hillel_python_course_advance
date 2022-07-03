"""
some modul
"""

import random

from faker import Faker


class FakeMail:
    """
    Class create fake mail from Name and second name

        my_fake_email = FakeMail(First Name, Second Name)
    """
    first_domain_list: list = ['com', 'ua', 'net', 'info', 'org', 'me', 'so', 'to', 'biz', 'in']
    second_domain_list: list = ['mail', 'gmail', 'mail.yahoo', 'mail.rambler',
                                'ukr', 'hotmail', 'pochta', 'gmail.com']

    def __init__(self, first_name: str, second_name: str):
        self.first_name: str = first_name
        self.second_name: str = second_name

    def fake_mail_name(self) -> str:
        """
        Method concatenate number in range 0-999
        with second and first name in random str

        Random choice from:
        first_part: str = (First name, Second name, Number in range 0-999])
        separator: str = ('None', '_', 'None', '.', '_')
        second_part: str = (First name, Second name, Number in range 0-999])

        return first_part + separator + second_part
        """
        number_in_mail_1: str = str(random.randrange(1950, 2015))
        number_in_mail_2: str = str(random.randrange(1950, 2015))
        first_part: str = random.choice([self.first_name.lower(), self.first_name[0],
                                         self.second_name.lower(), self.second_name[0],
                                         number_in_mail_1])
        separator: str = random.choice(['', '_', '', '.', '_'])
        second_part: str = random.choice([self.first_name.lower(),
                                          self.second_name.lower(), number_in_mail_2])
        mail_name: str = first_part + separator + second_part
        return mail_name

    @classmethod
    def fake_mail_domain(cls) -> str:
        """
        Method make fake domain from random first and second domain
        :return:
        f'@{second_domain}.{first_domain}'
        """
        first_domain: str = random.choice(cls.first_domain_list)
        second_domain: str = random.choice(cls.second_domain_list)
        return f'@{second_domain}.{first_domain}'

    def fake_email(self) -> str:
        """
        Method return fake email address concatenated feke mail name and domain
        :return:
        self.fake_mail_name() + self.fake_mail_domain()
        """
        return self.fake_mail_name() + self.fake_mail_domain()


class FakeUserData:
    """
    Class use fake names for creating fake user data
    (name and email) in given range

    fake_data = FakeUserData(int(number))
        :return
        Kimberly 867buck@ukr.so
        Michael M_thomas@gmail.me
        etc.

    """

    def __init__(self, number=20):
        self.number: int = number

    @staticmethod
    def get_fake_user():
        """
        Generate one Fake user
        :return: f'{fake_name[0]} {my_fake_email.fake_email()}'
        """
        fake = Faker()
        fake_name: str = fake.name().split()
        my_fake_email = FakeMail(fake_name[0], fake_name[1])
        return f'{fake_name[0]} {my_fake_email.fake_email()}'

    def oh_so_many_fake_users(self) -> str:
        """
        Return str with fake users
        """
        fake_users_list: list = [self.get_fake_user() for i in range(self.number)]
        fake_users: str = '\n</br>'.join(fake_users_list)
        return fake_users


class AverageColumnValue:
    """
    Class return average value by column in file
     file_name: str             - Name of file
     is_header: bool = False    - True if table with header
     index: int = 0             - The number of column. Star 0 like a first
     splitter: str = ', '       - symbols that split columns
     res_type = float           - type of data that you expected
    """

    def __init__(self, file_name: str, is_header: bool = False, index: int = 0,
                 splitter: str = ', ', res_type=float):
        self.file_name = file_name
        self.is_header = is_header
        self.index = index
        self.splitter = splitter
        self.res_type = res_type

    @property
    def file_opener(self) -> list:
        """
        Make list from file. One line - one str
        cut it (like table). False as default
        :return: list
        """
        with open(self.file_name, mode='r', encoding='ascii') as f:
            file_content: list = f.read().split('\n')
        while "" in file_content:
            file_content.remove('')
        if self.is_header:
            file_content.remove(file_content[0])
        return file_content

    @property
    def seq_splitter(self) -> list:
        """
        Method split str to list and return given index in list
        :return: list with parameters by index
        """
        result = [i.split(self.splitter)[self.index] for i in self.file_opener]
        return result

    @property
    def str_to_converter(self) -> list[float]:
        """
        :return: list with converted value
        """
        result = list(map(self.res_type, self.seq_splitter))
        return result

    def __len__(self):
        """
        :return: length of column
        """
        return len(self.str_to_converter)

    def sumer(self):
        """
        :return: sum of values in column
        """
        return sum(self.str_to_converter)

    @property
    def averager(self):
        """
        :return: avarage value by column
        """
        average_value = round(self.sumer() / self.__len__(), 3)
        return average_value


if __name__ == '__main__':
    height = AverageColumnValue('hw.csv', is_header=True, index=1)
    weight = AverageColumnValue('hw.csv', is_header=True, index=2)
    height_average_inch = height.averager
    weight_average_lb = weight.averager
    height_averager_cm = round(height_average_inch * 2.54)
    weight_averager_kg = round(weight_average_lb * 0.453592)
    print(f'Average height is {height_averager_cm} in cm')
    print(f'Average weight is {weight_averager_kg} in kg')
    # print(weight_list_float)

