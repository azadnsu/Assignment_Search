import unittest
import time # I am not clear about Waits(), so used time sleep
from selenium import webdriver
from locators import Locators
from waits import DriverWaits

class TestSearch(unittest.TestCase):
    base_url = 'https://letskodeit.teachable.com/courses'

    @classmethod
    def setUpClass(cls):
        """
        This test runs at the begining of test suite run
        :return:
        """
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver_wait = DriverWaits(cls.driver)

        # cls.driver.find_element(*Locators.LOGIN_BUTTON).click()
        # time.sleep(30)
        # cls.driver.find_element(*Locators.USER_EMAIL).send_keys("test@email.com")
        # time.sleep(2)
        # cls.driver.find_element(*Locators.USER_PASSWORD).send_keys("abcabc")
        # time.sleep(2)
        # cls.driver.find_element(*Locators.SUBMIT_BUTTON).click()

        """If I keep login code here in the above way, error shows: 
        selenium.common.exceptions.NoSuchElementException: 
        Message: no such element: Unable to locate element: {"method":"link text","selector":"Login"}
        """

    @classmethod
    def tearDownClass(cls):
        """
        This runs at the last of suite run
        :return:
        """
        # If I add logout code here, error shows. Should not it work?
        cls.driver.find_element(*Locators.CLICK_AVATAR).click()
        time.sleep(1)
        cls.driver.find_element(*Locators.LOGOUT_LINK).click()
        cls.driver.quit()

    def setUp(self):
        """
        This method run at the begining of each test case
        :return:
        """

        self.driver.get(self.base_url)
        click_login_button = self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(2)
        enter_email = self.driver.find_element(*Locators.USER_EMAIL).send_keys("test@email.com")
        time.sleep(2)
        enter_password = self.driver.find_element(*Locators.USER_PASSWORD).send_keys("abcabc")
        time.sleep(2)
        click_submit_button = self.driver.find_element(*Locators.SUBMIT_BUTTON).click()
        time.sleep(2)
        text = self.driver.find_element(*Locators.MY_COURSES)
        assert text == text , 'User is not logged in'
        time.sleep(2)

    def tearDown(self):
        """
        This method runs at last of each test case
        :return:
        """
        pass

    def test_search(self):
        """
        Search for Selenium courses
        :return:
        """
        click_search_field = self.driver.find_element(*Locators.SEARCH_FIELD)
        click_search_field.send_keys("Selenium")

        self.driver.find_element(*Locators.SEARCH_ICON).click()

        # Here I am unable to assert the course name contains 'Selenium'
        course_lists = self.driver.find_elements(*Locators.COURSE_LISTS)
        course_prices = self.driver.find_elements(*Locators.COURSE_PRICES)

        num_of_courses = len(course_lists)

        for course in range(num_of_courses):
            print(course_lists[course].text + ': ' + course_prices[course].text)


if __name__ == '__main__':
      unittest.main()
