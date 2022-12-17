from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Form:
    #chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome = webdriver.Chrome()

    def __init__(self):
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()

    def elementByID(self, ID):
        firstName = self.chrome.find_element(By.ID, f'{ID}')
        firstName.send_keys('Andreea')
        sleep(5)

    def elementByLinkText(self, linkTxt):
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, f'{linkTxt}').click()
        sleep(5)

    def elementByName(self, name):
        self.chrome.get('http://www.seleniumframework.com/Practiceform/')
        self.chrome.find_element(By.NAME, f'{name}').send_keys('It Factory')
        sleep(2)

    def elementByCSS(self, css):
        self.chrome.get('https://the-internet.herokuapp.com/')
        return self.chrome.find_element(By.CSS_SELECTOR, f'{css}')

test = Form()
#test.elementByID('frist-name')
# test.elementByLinkText('Checkboxes')
test.elementByName('company')