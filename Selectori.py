from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    # chrome = webdriver.chrome

    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def elementByName(self,ID):
        fristName =self.chrome.find_element(By.ID, f'{ID}')
        fristName.send_keys('Andy')
        sleep(2)

    def elementByLinkText(self,linkText):
        self.chrome.get('https://formy-project.herokuapp.com')
        self.chrome.find_element(By.PARTIAL_LINK_TEXT,f'{linkText}').click()
        sleep(2)


    def elementByCss(self,css):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        return self.chrome.find_element(By.CSS_SELECTOR, f'{css}')
test = Form()
#test.elementByID('frist-name')
test.elementByLinkText('Auto')
test.elementByName('country')

cssSelector = test.elementByCss('input#frist-name')
sleep(2)
print(cssSelector.location)
cssSelector2 = test.elementByCss('input.form-control')
print(cssSelector2.location)
ex = test.elementByCss('Input[placeholder="Enter last name"].send_keys')