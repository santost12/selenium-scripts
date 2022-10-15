from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

driver.get("https://whatsmyua.info/")

user_agent_box = driver.find_element(By.CSS_SELECTOR, "#custom-ua-string")

print(user_agent_box.text)

driver.quit()