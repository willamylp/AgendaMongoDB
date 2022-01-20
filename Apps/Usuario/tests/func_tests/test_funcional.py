import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


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

    def sleep5(void):
        for i in range(5):
            time.sleep(1)

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('Jhones')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('jhones3000')
        self.assertIsNone(self.selenium.find_element_by_xpath(
            '//input[@value="login"]').click())

    def test_link_for_create_user_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        self.sleep5()
        self.selenium.find_element_by_link_text('cadastre-se').click()
        host = self.selenium.current_url[0:22]
        self.sleep5()
        self.assertEquals(self.selenium.current_url, host + "/new/")
