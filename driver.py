import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('https://praison.com/django-task-browser-app/');
iframe = driver.find_element_by_tag_name('iframe')
print(iframe)
print(driver.title)
driver.quit()

