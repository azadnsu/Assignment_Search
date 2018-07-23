from selenium.webdriver.common.by import By


class Locators(object):

    LOGIN_BUTTON = (By.XPATH,'//*[@id="navbar"]/div/div/div/ul/li[2]/a')
    USER_EMAIL = (By.ID,'user_email')
    USER_PASSWORD = (By.ID,'user_password')
    SUBMIT_BUTTON = (By.XPATH,'//*[@id="new_user"]/div[3]/input')
    MY_COURSES = (By.XPATH,'//*[@id="navbar"]/div/div/div/ul/li[1]/a')
    SEARCH_FIELD = (By.ID,'search-courses')
    SEARCH_ICON = (By.ID,'search-course-button')
    SELENIUM_WEBDRIVER_TEXT = (By.CLASS_NAME,'course-listing-title')
    COURSE_LISTS = (By.CLASS_NAME,'course-listing-title')
    COURSE_PRICES = (By.XPATH,'//div[@class="small course-price"]')
    CLICK_AVATAR = (By.CLASS_NAME,'gravatar')
    LOGOUT_LINK = (By.LINK_TEXT,'Log Out')