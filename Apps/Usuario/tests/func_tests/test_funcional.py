import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


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
        username_input = self.selenium.find_element(By.ID, "id_username")
        username_input.send_keys('Jhones')
        password_input = self.selenium.find_element(By.ID, "id_password")
        password_input.send_keys('jhones3000')
        self.sleep5
        self.assertIsNone(self.selenium.find_element(
            By.ID, "bt_entrar").click())

    def test_link_for_create_user_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        self.sleep5()
        self.selenium.find_element(By.LINK_TEXT, 'cadastre-se').click()
        self.sleep5()
        host = self.selenium.current_url[0:22]
        self.assertEqual(self.selenium.current_url, host + "/new/")
