from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Firefox("geckodriver")
b.get('https://www.seleniumhq.org/')

# element = b.find_element_by_link_text('Download')
# element.click()
b.set_page_load_timeout(10)
element = b.find_element_by_id('email')
element.send_keys('helloworld@gamil.com')

element2 = b.find_element_by_id('pass')
element2.send_keys('mypassword')



button = b.find_element_by_id('u_0_b')
button.click()
# element.send_keys(Keys.ENTER)