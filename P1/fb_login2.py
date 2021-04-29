from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import string


#Open  FB 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
userid="rohitaswchoudhary@gmail.com"
pwd="RohitaswChoudhary@2002"
time.sleep(5)

#Login To FB
emailelement= driver.find_element_by_xpath('.//*[@id="email"]')
emailelement.send_keys(userid)
passwordfield= driver.find_element_by_xpath('.//*[@id="pass"]')
passwordfield.send_keys(pwd)

login_box = driver.find_element_by_name('login')
login_box.click()

time.sleep(5)

driver.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)
birthdays= driver.find_element_by_id("birthdays_content")
containers=birthdays.find_elements_by_css_selector("[class='_4-u3']")
print(len(containers))
birthdaystoday= containers[0]


birthdayslist= birthdaystoday.find_elements_by_css_selector("[class='_tzm']")
#Looping through today's birthdays 
for b in birthdayslist:
    try:
        name= b.find_element_by_tag_name("a")
        firstname=((name.get_attribute("title")).split())[0]
        textbox=b.find_element_by_tag_name("textarea")
        message= "Happy Birthday " + firstname + " 🎁🎁🎁🎁🎁 !!!!"
        textbox.send_keys(message)
        textbox.send_keys(Keys.ENTER)
    except NoSuchElementException:
        pass

time.sleep(5)
#Closing the session
driver.close()

