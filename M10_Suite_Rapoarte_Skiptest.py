#checkboxsuite
import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from self import self
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
class CheckBoxTest(TestCase):
    CHECKBOXLINK =(By.LINK_TEXT,'Checkboxes')
    HEADERCSS = (By.CSS_SELECTOR, 'h3')

    def setUp(self):
        self.firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.firefox.maximize_window()
        self.firefox.get('https://the-internet.herokuapp.com/')
        self.firefox.find_element(*self.CHECKBOXLINK).click()
        #self.firefox.implicitly_wait(3)
        sleep(3)


    def tearDown(self):
        self.firefox.quit()

    def testCheckUrl(self):
        actual = self.firefox.current_url
        expected =  'https://the-internet.herokuapp.com/'
        self.assertEqual(actual,expected,'Url incorect')


    def testCheckheader(self):
        actual= self.firefox.find_element(*self.HEADERCSS).text
        expected = 'Checkboxes'
        self.assertEqual(expected,actual,'header gresit')

    def testCheckBoxSelected(self):
        box = self.firefox.find_element(*self.FRISTCHECKBOXPATH)
        box.click()
        self.assertTrue(box.is_selected(),'box unselected')
    def testCheckBoxUnselected(self):
        pass
