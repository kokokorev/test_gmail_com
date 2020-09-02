import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InboxPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        self.searched_messages      = 'farit.valiahmetov'
        self.older_button_xpath     = '//div[@data-tooltip="Older"]'

        self.compose_button_xpath   = '//*[contains(text(), "Compose")]'
        self.to_textbox_name        = 'to'
        self.subject_textbox_name   = 'subjectbox'
        self.message_body_xpath     = '//div[@aria-label="Message Body"]'
        self.send_button_xpath      = '//div[@aria-label="Send ‪(Ctrl-Enter)‬"]'
    
    
    def get_messages_count(self) -> int:
        """
        прохождение по страницам во 'входящих', если такие есть. 
        подсчет количества нужных сообщений
        """
        self.driver.implicitly_wait(5)
        self.count_msg = int(len(self.driver.find_elements_by_name('farit.valiahmetov')))
        try:
            self.driver.find_element_by_xpath(self.older_button_xpath).click()
            self.count_msg += self.search_messages_count()
        except:
            print('Страниц больше нет или не удалось перейти на следующую')

        return self.count_msg


    def search_messages_count(self):
        try:
            self.count = self.get_messages_count()
        except:
            print('Не удалось подсчитать сообщения')

        if self.count != 0:
            self.count /= 2
        else:
            self.count = None
    

    def send_message(self):
        self.driver.find_element_by_xpath(self.compose_button_xpath).click()

        self.wait.until(EC.presence_of_element_located((By.NAME, self.to_textbox_name)))
        self.driver.find_element_by_name(self.to_textbox_name).send_keys('farit.valiahmetov@simbirsoft.com')
        self.driver.find_element_by_name(self.subject_textbox_name).send_keys('Тестовое задание. Кокорев')

        if self.count is not None:
            self.driver.find_element_by_xpath(self.message_body_xpath).send_keys(f'Количество сообщение: {int(self.count)}')
        else:
            self.driver.find_element_by_xpath(self.message_body_xpath).send_keys('Сообщений нет')

        self.driver.find_element_by_xpath(self.send_button_xpath).click()
        time.sleep(5)