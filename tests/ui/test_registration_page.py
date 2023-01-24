import time
from pages.registration_page import RegistrationPage
from pages.settings import URL_REGISTRATION_PAGE
from faker import Faker
fake = Faker()


def test_registration_of_student(browser):
    """ Registration of a new student """
    test_data = {
        'first_name': fake.first_name_male(),
        'last_name': fake.last_name_male(),
        'email': fake.email(),
        'gender': 'Male',
        'mobile_number': fake.random_number(digits=10),
        'date_of_birth': fake.day_of_month() + ' ' + fake.month_name() + ',' + fake.year(),
        'subjects': 'English',
        'hobbies': {
            'Sports': False,
            'Reading': True,
            'Music': True
        },
        'cur_address': fake.street_address(),
        'state_name': 'NCR',
        'city_name': 'Delhi',
        'picture': 'cat.jpg'
    }
    link = URL_REGISTRATION_PAGE
    page = RegistrationPage(browser, link)
    page.open()
    page.fill_form(test_data)
    page.click_submit_button()
    time.sleep(1)
    page_data = page.get_page_data()
    page.compare_data(test_data, page_data)
    