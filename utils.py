from selenium.webdriver import Chrome, ChromeOptions
import os

#BASE_URL = 'http://localhost:8000'
BASE_URL = 'http://localhost:1234'


def get_driver():
    options = ChromeOptions()
    if os.environ.get('HEADLESS'):
        options.add_argument('--headless')
    driver =  Chrome(options=options)
    driver.implicitly_wait(5)
    return driver
