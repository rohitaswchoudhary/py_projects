from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome("chromedriver")
 
 
LOGIN_URL = 'https://www.facebook.com/login.php'
 
class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
 
 
    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
 
 
if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='rohitaswchoudhary@gmail.com', password='RohitaswChoudhary@2002', browser='Chrome')
    fb_login.login()


browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Happy Birthday !'

element = browser.find_elements_by_xpath("//*[@class ='enter_submit\
	uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea\
				inlineReplyTextArea mentionsTextarea textInput']")

cnt = 0

for el in element:
	cnt += 1
	element_id = str(el.get_attribute('id'))
	XPATH = '//*[@id ="' + element_id + '"]'
	post_field = browser.find_element_by_xpath(XPATH)
	post_field.send_keys(feed)
	post_field.send_keys(Keys.RETURN)
	print("Birthday Wish posted for friend" + str(cnt))

# Close the browser
browser.close()
