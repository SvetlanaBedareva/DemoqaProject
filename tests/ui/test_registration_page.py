import time
from pages.registration_page import RegistrationPage
from pages.settings import URL_REGISTRATION_PAGE


def test_registration_of_student(browser):
    """ Registration of a new student """
    test_data = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'email': 'test@gmail.com',
        'gender': 'Male',
        'mobile_number': '9053333333',
        'date_of_birth': '20 November,1990',
        'subjects': 'English',
        'hobbies': {
            'Sports': False,
            'Reading': True,
            'Music': True
        },
        'cur_address': 'Moscow, Kirova 1, 2',
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
    