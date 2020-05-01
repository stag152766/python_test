from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()
        self.contact_cashe = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def return_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(new_contact_data, 0)

    def modify_contact_by_index(self, new_contact_data, index):
        driver = self.app.driver
        self.return_home_page()
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name('update').click()
        self.return_home_page()
        self.contact_cashe = None

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            driver = self.app.driver
            self.return_home_page()
            self.contact_cashe = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = row.find_element_by_name('selected[]').get_attribute("value")
                self.contact_cashe.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cashe)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.return_home_page()
        driver.find_elements_by_name('selected[]')[index].click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Delete 1 addresses?')
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutError:
            print('no alert')
        self.contact_cashe = None

    def count(self):
        driver = self.app.driver
        self.return_home_page()
        return len(driver.find_elements_by_name("entry"))