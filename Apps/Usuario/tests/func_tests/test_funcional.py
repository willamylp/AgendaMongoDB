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
        username_input.send_keys('caduzera')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('cadu3000')
        # for i in range(10):
        #     print("Tick")
        #     time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="login"]').click()



























# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Create your tests here.
# class PlayerFormTest(LiveServerTestCase):

#   def testform(self):
#     #webdriver.Chrome(service=service)
#     selenium = webdriver.Chrome()
#     #Choose your url to visit
#     selenium.get('http://127.0.0.1:8000/')
#     #find the elements you need to submit form
#     player_name = selenium.find_element_by_id('id_username')
#     player_password = selenium.find_element_by_id('id_password')

#     submit = selenium.find_element_by_id('submit')

#     #populate the form with data
#     player_name.send_keys('')
#     player_password.send_keys('')

#     #submit form
#     submit.send_keys(Keys.RETURN)

#     #check result; page source looks at entire html document
#     self.asserTrue('Lebron James' in selenium.page_source)