from unittest import TestCase

import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEqual(expected, actual, 'Url incorect')
    #
    # def test_search_City(self):
    #     self.chrome.implicitly_wait(2)
    #     searchbar=self.chrome.find_element(By.ID, 'select2-hotel_city-container')
    #     searchbar.click()
    #     search1=self.chrome.find_element(By.CLASS_NAME , 'select2-search__field')
    #     searchbar.send_keys('Bucharest')
    #     self.chrome.implicitly_wait(3)
    #     expected_values = 'Bucharest, Romania'
    #     result = self.chrome.find_element(By.CLASS_NAME,'select2-results__option selects2-results__option--highlightd')
    #     actual = result.test
    #     self.assertEqual(expected_values,actual,'Rezultat Incorect')

    def test_addremovelinktxt(self):
        self.chrome.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/add_remove_elements/'
        self.assertEqual(expected,actual,'Url incorect')

    def test_header_addremoveelement(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual= self.chrome.find_element(By.CSS_SELECTOR,'h3').text
        expected = 'Add/Remove Elements'
        self.assertEqual(expected,actual,'text incorect')
    def test_press_add_elementbutton(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        actual = self.chrome.find_element(By.ID, 'elements').text
        expected ='Delete'
        self.assertEqual(expected,actual,'text incorect')
    def test_compareaddelement_delete(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        actual = self.chrome.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        expected = 3
        self.assertEqual(expected,len(actual),'Nr de elemente nu corespunde')