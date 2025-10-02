from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ContactUsPage:
    CONTACT_US_BUTTON = (By.XPATH, "//span[text()='Contact  Us']")
    NAME_FIELD = (By.XPATH, '//*[@id="form-field-name"]')
    COMPANY_FIELD = (By.XPATH, '//*[@placeholder="Enter your company name"]')
    EMAIL_FIELD = (By.XPATH, '//*[@placeholder="Enter your email"]')
    PHONE_FIELD = (By.XPATH, '//*[@placeholder="Enter your contact number"]')
    MSG_FIELD = (By.XPATH, '//*[@id="form-field-message"]')
    CONT_ICON = (By.XPATH,'//*[@class="iti__selected-country-primary"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Click on Contact Us button")
    def go_to_contact_us(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_US_BUTTON)).click()

    @allure.step("Fill the contact form")
    def fill_form(self, name, company, email, phone_number, message):
        with allure.step(f"Enter Name: {name}"):
            self.wait.until(EC.presence_of_element_located(self.NAME_FIELD)).send_keys(name)
        with allure.step(f"Enter Company: {company}"):
            self.wait.until(EC.presence_of_element_located(self.COMPANY_FIELD)).send_keys(company)
        with allure.step(f"Enter Email: {email}"):
            self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD)).send_keys(email)
        with allure.step(f"Enter Phone Number: {phone_number}"):
            self.wait.until(EC.presence_of_element_located(self.PHONE_FIELD)).send_keys(phone_number)
        with allure.step(f"Enter Message"):
            self.wait.until(EC.presence_of_element_located(self.MSG_FIELD)).send_keys(message)
