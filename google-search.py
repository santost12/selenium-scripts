from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

search_query = "cats"
driver.get("https://www.google.com/")

google_logo = driver.find_element(By.CSS_SELECTOR, ".lnXdpd")
search_box = driver.find_element(By.CSS_SELECTOR,".gLFyf")
search_button = driver.find_element(By.CSS_SELECTOR, ".FPdoLc > center:nth-child(1) > input:nth-child(1)")

search_box.click()
search_box.send_keys(search_query)
google_logo.click()
search_button.click()

time.sleep(20)

driver.quit()