import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from selenium.webdriver.common.keys import Keys
import argparse

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)  # Optional argument, if not specified will search path.
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=False, help="Please provide URL")
    args = parser.parse_args()
    if args.url:
        url = args.url
    else:
        url = 'https://praison.com/django-task-browser-app/'  
    driver.get(url);
    iframe = driver.find_elements_by_tag_name('iframe')
    for frame in iframe:
        print(frame.size)
        print(frame.text)
        # print(frame.screenshot_as_png('/var/www/html/adsdetector')) Option to save as PNG
    print(driver.title)
    driver.quit()



class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)   

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    main()
    unittest.main()
