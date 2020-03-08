from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # конструирование помощника
        # помощник получает ссылку на саму фикстуру (объект класса Application)
        # это дает возможность в одном помощнике обратиться к другому, через объект класса Application
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.driver.quit()
