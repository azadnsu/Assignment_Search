import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

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

    @classmethod
    def tearDownClass(cls):
        """
        This runs at the last of suite run
        :return:
        """
        #cls.driver.quit()

    # def test_logout(self): # logout code
    #     click_avatar = self.driver.find_element_by_class_name('gravatar').click()
    #     click_logout = self.driver.find_element_by_xpath('//*[@id="navbar"]/div/div/div/ul/li[4]/ul/li[5]/a').click()
    #     time.sleep(2)


    def setUp(self):
        """
        This method run at the begining of each test case
        :return:
        """

        self.driver.get(self.base_url)

    # def tearDown(self):
    #     """
    #     This method runs at last of each test case
    #     :return:
    #     """
    #     pass


    def test_login(self):
        """
        Click on Login button and then enter username and password
        :return:
        """
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

        click_search_field = self.driver.find_element(*Locators.SEARCH_FIELD)
        click_search_field.send_keys("Selenium")

        self.driver.find_element(*Locators.SEARCH_ICON).click()
        time.sleep(2)

        course_lists = self.driver.find_elements(*Locators.COURSE_LISTS)
        course_prices = self.driver.find_elements(*Locators.COURSE_PRICES)

        num_of_courses = len(course_lists)

        for course in range(num_of_courses):
            print(course_lists[course].text + ': ' + course_prices[course].text)

        click_avatar = self.driver.find_element(*Locators.CLICK_AVATAR).click()
        time.sleep(1)
        click_logout = self.driver.find_element(*Locators.LOGOUT_LINK).click()


    # def test_search_selenium(self):
    #     time.sleep(2)
    #     click_search_field = self.driver.find_element(*Locators.SEARCH_FIELD)
    #     click_search_field.send_keys()
    #
    #     enter_search_query = click_search_field.send_keys("Selenium")
    #
    #     click_search_icon = self.driver.find_element(*Locators.SEARCH_ICON).click()
    #     time.sleep(2)
    #
    #     check_div_list = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]')
    #     print(check_div_list.text)
    #     # course_listing_title = self.driver.find_elements(*Locators.SELENIUM_WEBDRIVER_TEXT)
    #     # course_listing_price =
    #     # print(course_listing_title)



if __name__ == '__main__':
     unittest.main()
