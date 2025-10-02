import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.contact_us_page import ContactUsPage
from utils.data_reader import get_test_data
from utils.Config import Config
from utils.screenshot_util import save_screenshot


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


# Read test data from Excel
test_data = get_test_data("Test_Data.xlsx")


@pytest.mark.parametrize("name, company, email, phone, message", test_data)
def test_fill_contact_us_form(browser, name, company, email, phone, message):
    with allure.step("Open the website"):
        browser.get(Config.BASE_URL)

    contact_page = ContactUsPage(browser)

    with allure.step("Navigate to Contact Us page"):
        contact_page.go_to_contact_us()

    with allure.step("Fill the contact form with Excel data"):
        contact_page.fill_form(
            name=name,
            company=company,
            email=email,
            phone_number=phone,
            message=message,
        )

    with allure.step("Take screenshot after form is filled"):
        save_screenshot(browser, name)

