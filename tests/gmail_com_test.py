import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.page import InboxPage

class TestGmailCom():

    def setup(self):
        selenium_grid_node_url = 'http://192.168.0.102:45168/wd/hub'

        self.options = webdriver.ChromeOptions()   
        self.options.add_argument('--disable-web-security')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--user-data-dir=D:\\dev\\python\\test_gmail_com\\resources')

        capabilities = DesiredCapabilities.CHROME
        capabilities['platform'] = 'WINDOWS'
        capabilities['version'] = '10'

        self.driver = webdriver.Remote( desired_capabilities=capabilities,
                                        command_executor=selenium_grid_node_url,
                                        options=self.options)


    @allure.feature('Подсчет сообщений')
    @allure.story('Поиск сообщений от farit.valiahmetov@simbirsoft.com')
    @allure.severity('critical')
    def test_for_check_messages(self):
        driver = self.driver
        driver.get('https://mail.google.com')

        self.inbox_page = InboxPage(driver)
        self.inbox_page.search_messages_count()

    @allure.feature('Отправка сообщения')
    @allure.story('Отправка сообщения от farit.valiahmetov@simbirsoft.com')
    @allure.severity('blocker')
    def test_for_send_messages(self):
        driver = self.driver
        driver.get('https://mail.google.com')

        self.inbox_page = InboxPage(driver)
        self.inbox_page.search_messages_count()
        self.inbox_page.send_message()


    def teardown(self):
        self.driver.close()