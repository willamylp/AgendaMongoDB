from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
# import time

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("username")
        # for i in range(5):
        #     time.sleep(1)
        username_input.send_keys('Jhones')
        password_input = self.selenium.find_element_by_name("password")
        # for i in range(5):
        #     time.sleep(1)
        password_input.send_keys('jhones3000')
        self.assertIsNone(self.selenium.find_element_by_xpath('//input[@value="login"]').click())