from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

class RegistrationFormAutomation:
    def __init__(self):
        self.web = self.initialize_webdriver()

    def initialize_webdriver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        web = webdriver.Chrome(options=options)
        return web

    def open_registration_page(self):
        self.web.get('https://www.wplay.co/apuestas/registro')
        time.sleep(2)

    def fill_personal_info(self):
        first_name_content = 'Joe'
        second_name_content = 'N'
        last_name_content = 'Doe'
        second_surname_content = 'T'

        first_name_field = self.web.find_element(By.ID, 'formEl_173')
        second_name_field = self.web.find_element(By.ID, 'formField_14')
        last_name_field = self.web.find_element(By.ID, 'formEl_540')
        second_surname_field = self.web.find_element(By.ID, 'formField_25')

        first_name_field.send_keys(first_name_content)
        second_name_field.send_keys(second_name_content)
        last_name_field.send_keys(last_name_content)
        second_surname_field.send_keys(second_surname_content)

    def fill_birth_info(self):
        select_day = Select(self.web.find_element(By.ID, 'day'))
        select_day.select_by_index(2)
        select_month = Select(self.web.find_element(By.ID, 'month'))
        select_month.select_by_value('02')
        select_year = Select(self.web.find_element(By.ID, 'year'))
        select_year.select_by_value('2000')

    def fill_address_info(self):
        address = self.web.find_element(By.ID, 'formField_18')
        address.send_keys('Calle 1 # 23 - 4')

    def click_second_step_button(self):
        second_step_button = self.web.find_element(By.XPATH, '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[3]/button')
        second_step_button.click()

    def fill_citizenship_info(self):
        nationality_element = self.web.find_element(By.XPATH, '//*[@id="nationality"]')
        department_cc = self.web.find_element(By.XPATH, '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[2]/form/div/div[1]/fieldset[1]/div[2]/span/select')
        municipio_cc = self.web.find_element(By.XPATH, '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[2]/form/div/div/fieldset[2]/div[2]/span/select')

        cedula_number = self.web.find_element(By.ID, 'formField_8')
        expedicion_date_day = self.web.find_element(By.ID, 'day_idIssueDate')
        expedicion_date_month = self.web.find_element(By.ID, 'month_idIssueDate')
        expedicion_date_year = self.web.find_element(By.ID, 'year_idIssueDate')

        nationality_selection = Select(nationality_element)
        nationality_selection.select_by_value('CO')

        department_cc_selection = Select(department_cc)
        department_cc_selection.select_by_value('05')

        municipio_cc_selection = Select(municipio_cc)
        municipio_cc_selection.select_by_value('MEDELLÍN')

        cedula_number.send_keys('1029320123')

        exp_date_selection_day = Select(expedicion_date_day)
        exp_date_selection_day.select_by_value('05')

        exp_date_selection_month = Select(expedicion_date_month)
        exp_date_selection_month.select_by_value('06')

        exp_date_selection_year = Select(expedicion_date_year)
        exp_date_selection_year.select_by_value('2018')

    def click_third_step_button(self):
        third_step_button = self.web.find_element(By.XPATH, '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[3]/button')
        third_step_button.click()

    def fill_contact_info(self):
        email_creation = self.web.find_element(By.ID, 'formField_4')
        number_creation = self.web.find_element(By.ID, 'phone-field')
        pass_creation = self.web.find_element(By.ID, 'formEl_3508')

        email_creation.send_keys('your_test_email')
        number_creation.send_keys('3221234567')
        pass_creation.send_keys('12345aBc')

    def close_browser(self):
        self.web.quit()

    def execute_registration(self):
        self.open_registration_page()
        self.fill_personal_info()
        self.fill_birth_info()
        self.fill_address_info()
        self.click_second_step_button()
        self.fill_citizenship_info()
        self.click_third_step_button()
        self.fill_contact_info()

if __name__ == "__main__":
    registration = RegistrationFormAutomation()
    registration.execute_registration()
