import os
import time
from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import StudentRegistrationFormLocators, StudentsDataFromFormLocators


class RegistrationPage(BasePage):
	def fill_form(self, data):
		self.fill_first_name(data['first_name'])
		self.fill_last_name(data['last_name'])
		self.fill_email(data['email'])
		self.select_gender(data['gender'])
		self.fill_mobile_number(data['mobile_number'])
		self.fill_date_of_birth(data['date_of_birth'])
		self.fill_subjects_field(data['subjects'])
		time.sleep(3)
		if data['hobbies']['Sports']:
			self.select_hobbies_sports()
		if data['hobbies']['Reading']:
			self.select_hobbies_reading()
		if data['hobbies']['Music']:
			self.select_hobbies_music()
		self.upload_picture(data['picture'])
		self.fill_current_address(data['cur_address'])
		self.select_state(data['state_name'])
		self.select_city(data['city_name'])
	
	def fill_first_name(self, first_name):
		first_name_field = self.browser.find_element(*StudentRegistrationFormLocators.FIRST_NAME)
		first_name_field.send_keys(first_name)
	
	def fill_last_name(self, last_name):
		last_name_field = self.browser.find_element(*StudentRegistrationFormLocators.LAST_NAME)
		last_name_field.send_keys(last_name)
	
	def fill_email(self, email):
		email_field = self.browser.find_element(*StudentRegistrationFormLocators.EMAIL)
		email_field.send_keys(email)
	
	def select_gender(self, gender_type):
		gender = None
		match gender_type:
			case 'Male':
				gender = self.browser.find_element(*StudentRegistrationFormLocators.GENDER_MALE)
			case 'Female':
				gender = self.browser.find_element(*StudentRegistrationFormLocators.GENDER_FEMALE)
			case 'Other':
				gender = self.browser.find_element(*StudentRegistrationFormLocators.GENDER_OTHER)
		self.browser.execute_script("arguments[0].click();", gender)
	
	def fill_mobile_number(self, mobile_number):
		mobile_number_field = self.browser.find_element(*StudentRegistrationFormLocators.MOBILE_NUMBER)
		mobile_number_field.send_keys(mobile_number)
	
	def fill_date_of_birth(self, date):
		date_list = date.replace(',', ' ').split(' ')
		day = date_list[0]
		month = date_list[1]
		year = date_list[2]
		date_of_birth = self.browser.find_element(*StudentRegistrationFormLocators.DATE_OF_BIRTH)
		self.browser.execute_script("arguments[0].click();", date_of_birth)
		month_field = self.browser.find_element(*StudentRegistrationFormLocators.MONTH_FIELD)
		month_field.click()
		month_dynamic_locator = StudentRegistrationFormLocators.MONTH_VALUE[1] % month
		month_value = self.browser.find_element(StudentRegistrationFormLocators.MONTH_VALUE[0], month_dynamic_locator)
		month_value.click()
		year_dynamic_locator = StudentRegistrationFormLocators.YEAR_VALUE[1] % year
		year_value = self.browser.find_element(StudentRegistrationFormLocators.YEAR_VALUE[0], year_dynamic_locator)
		year_value.click()
		day_dynamic_locator = StudentRegistrationFormLocators.DAY_VALUE[1] % day
		day_value = self.browser.find_element(StudentRegistrationFormLocators.DAY_VALUE[0], day_dynamic_locator)
		day_value.click()
		
	def fill_subjects_field(self, subjects):
		subjects_field = self.browser.find_element(*StudentRegistrationFormLocators.SUBJECTS_FIELD)
		subjects_field.send_keys(subjects)
		subjects_field.send_keys(Keys.RETURN)
	
	def select_hobbies_sports(self):
		hobbies_sports = self.browser.find_element(*StudentRegistrationFormLocators.HOBBIES_SPORTS)
		self.browser.execute_script("arguments[0].click();", hobbies_sports)
	
	def select_hobbies_reading(self):
		hobbies_reading = self.browser.find_element(*StudentRegistrationFormLocators.HOBBIES_READING)
		self.browser.execute_script("arguments[0].click();", hobbies_reading)
	
	def select_hobbies_music(self):
		hobbies_music = self.browser.find_element(*StudentRegistrationFormLocators.HOBBIES_MUSIC)
		self.browser.execute_script("arguments[0].click();", hobbies_music)
	
	def upload_picture(self, pic):
		picture = self.browser.find_element(*StudentRegistrationFormLocators.UPLOAD_PICTURE)
		pic_path = os.path.join(os.path.dirname(__file__), 'photo/' + pic)
		picture.send_keys(pic_path)
		time.sleep(3)
	
	def fill_current_address(self, cur_address):
		current_address = self.browser.find_element(*StudentRegistrationFormLocators.CURRENT_ADDRESS)
		current_address.send_keys(cur_address)
	
	def select_state(self, state_name):
		state = self.browser.find_element(*StudentRegistrationFormLocators.STATE)
		state.send_keys(Keys.DOWN)
		dynamic_locator = StudentRegistrationFormLocators.STATE_VALUE[1] % state_name
		value = self.browser.find_element(StudentRegistrationFormLocators.STATE_VALUE[0], dynamic_locator)
		self.browser.execute_script("arguments[0].click();", value)
	
	def select_city(self, city_name):
		city = self.browser.find_element(*StudentRegistrationFormLocators.CITY)
		city.send_keys(Keys.DOWN)
		dynamic_locator = StudentRegistrationFormLocators.CITY_VALUE[1] % city_name
		value = self.browser.find_element(StudentRegistrationFormLocators.CITY_VALUE[0], dynamic_locator)
		self.browser.execute_script("arguments[0].click();", value)
	
	def click_submit_button(self):
		submit_button = self.browser.find_element(*StudentRegistrationFormLocators.SUBMIT_BTN)
		self.browser.execute_script("arguments[0].click();", submit_button)
	
	def get_page_data(self):
		student_name = self.browser.find_element(*StudentsDataFromFormLocators.STUDENT_NAME).text
		student_email = self.browser.find_element(*StudentsDataFromFormLocators.STUDENT_EMAIL).text
		gender = self.browser.find_element(*StudentsDataFromFormLocators.GENDER).text
		mobile_number = self.browser.find_element(*StudentsDataFromFormLocators.MOBILE_NUMBER).text
		date_of_birth = self.browser.find_element(*StudentsDataFromFormLocators.DATE_OF_BIRTH).text
		subjects = self.browser.find_element(*StudentsDataFromFormLocators.SUBJECTS_FIELD).text
		hobbies = self.browser.find_element(*StudentsDataFromFormLocators.HOBBIES).text.split(", ")
		picture = self.browser.find_element(*StudentsDataFromFormLocators.PICTURE).text
		current_address = self.browser.find_element(*StudentsDataFromFormLocators.CURRENT_ADDRESS).text
		state_and_city = self.browser.find_element(*StudentsDataFromFormLocators.STATE_AND_CITY).text
		data = {
			'student_name': student_name,
			'student_email': student_email,
			'gender': gender,
			'mobile_number': mobile_number,
			'date_of_birth': date_of_birth,
			'subjects': subjects,
			'hobbies': {
				'Sports': 'Sports' in hobbies,
				'Reading': 'Reading' in hobbies,
				'Music': 'Music' in hobbies
			},
			'picture': picture,
			'current_address': current_address,
			'state_and_city': state_and_city
		}
		return data
	
	def compare_data(self, test_data, page_data):
		assert test_data['first_name'] + ' ' + test_data['last_name'] == page_data['student_name']
		assert test_data['email'] == page_data['student_email']
		assert test_data['gender'] == page_data['gender']
		assert test_data['mobile_number'] == page_data['mobile_number']
		assert test_data['date_of_birth'] == page_data['date_of_birth']
		assert test_data['subjects'] == page_data['subjects']
		assert test_data['picture'] == page_data['picture']
		assert test_data['cur_address'] == page_data['current_address']
		assert test_data['state_name'] + ' ' + test_data['city_name'] == page_data['state_and_city']
		assert test_data['hobbies'] == page_data['hobbies']
