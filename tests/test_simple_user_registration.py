import datetime

from demoga_tests.data.user import User
from demoga_tests.pages.registration_page import RegistrationPage


def test_simple_user_registration():
    registration_page = RegistrationPage()

    mariya = User(first_name='Mariya', last_name='Zhurova', email='mzhurova4@mail.ru', gender='Female',
                  fhone_nomber='9234324557', date_of_birth=datetime.date(1990, 10, 4),
                  subjects='Maths', hobbies='Sports', picture='2012091208303549.png', address='Tomsk, Altayskaya',
                  state='Haryana', city='Panipat')

    registration_page.open()
    registration_page.register_user(mariya)
    registration_page.assert_registred_date(mariya)
