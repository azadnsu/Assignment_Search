from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # EC (Expected Condition) = user defined variable


class DriverWaits(object):

    def __init__(self, driver, timeout=10, poll_frequency=1):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)

    def wait_till_alert_is_present(self):
        self.wait.until(EC.alert_is_present(), 'Alert is not present')

    def wait_till_alert_is_dismissed(self):
        self.wait.until(EC.NoAlertPresentException, 'Alert does not get dismissed')
        #self.wait.until_not(EC.alert_is_present(), 'Alert is still present')

    def wait_till_element_is_visible(self):
        self.wait.until(EC.visibility_of_all_elements_located(),'Elements not loaded')
