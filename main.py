
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#To open your edge browser 
options = webdriver.EdgeOptions()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
edge_driver = webdriver.Edge(options=options)

#for random searches
string = ("ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstvwxyz")
edge_driver.get('https://www.bing.com/')
edge_driver.maximize_window()


# to make sure that u logged with your personal email or your targeted account
edge_driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d33376853255F4F8C87D26C1737277847%26wlsso%3d1%26wlexpsignin%3d1&src=EXPLICIT&sig=0E8FE6F01AD666CE018CF56C1BC267A0')
time.sleep(3)

#to run the code in loop
for i in range(30):
    search_input = edge_driver.find_element(By.ID, 'sb_form_q')
    a = random.sample(string, 6)
    b = "".join(a)
    search_input.send_keys(b)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5) # adjust this delay as you like
    edge_driver.back()
