from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        self.open_contact_to_edit_by_index(new_contact_data, 0)

    # def open_contact_to_edit_by_index(self, new_contact_data, index):
    #     driver = self.app.driver
    #     self.open_home_page()
    #     driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
    #     self.fill_contact_form(new_contact_data)
    #     driver.find_element_by_name('update').click()
    #     self.open_home_page()
    #     self.contact_cache = None

    def open_contact_to_view_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name('firstname').get_attribute('value')
        lastname = driver.find_element_by_name('lastname').get_attribute('value')
        id = driver.find_element_by_name('id').get_attribute('value')
        homephone = driver.find_element_by_name('home').get_attribute('value')
        workphone = driver.find_element_by_name('work').get_attribute('value')
        mobilephone = driver.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = driver.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        row = driver.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    contact_cache = None 

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        driver.find_elements_by_name('selected[]')[index].click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Delete 1 addresses?')
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutError:
            print('no alert')
        self.contact_cache = None

    def count(self):
        driver = self.app.driver
        self.open_home_page()
        return len(driver.find_elements_by_name("entry"))

    def get_contact_info_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_to_view_by_index(index)
        text = driver.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)