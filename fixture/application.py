from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        # конструирование помощника
        # помощник получает ссылку на саму фикстуру (объект класса Application)
        # это дает возможность в одном помощнике обратиться к другому, через объект класса Application
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

