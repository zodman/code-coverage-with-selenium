from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils import BASE_URL



element = lambda selc,txt : (selc[0], selc[1].format(txt))


class TodoPage:
    input_text = By.XPATH, '//*[@data-reactid=".0.0.1"]' 
    text = By.XPATH, '//li/div/label[contains(text(),"{}")]'
    check_box_toggle = By.XPATH, '//li/div/label[contains(text(),"{}")]/parent::div/input'
    todo_is_completed  = By.XPATH, '//li[@class="completed"]/div/label[contains(text(), "{}")]'

    ElementNotFound = NoSuchElementException

    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
        self.open()
        
    def open(self):
        self.driver.get(BASE_URL)

    def add(self, task_text):
        self.driver.find_element(*self.input_text).click()
        self.driver.find_element(*self.input_text).send_keys(task_text+'\n')

    def completed(self, text):
        self.driver.find_element(*element(self.check_box_toggle, text)).click()
   
    def exists_todo(self, text):
        return self.driver.find_element(*element(self.text, text) ).is_displayed()
    
    def is_completed(self, text):
        return self.driver.find_element(*element(self.todo_is_completed, text)).is_displayed()





