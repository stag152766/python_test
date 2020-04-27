class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first)
        self.change_field_value("middlename", contact.middle)
        self.change_field_value("lastname", contact.last)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def return_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def modify_contact(self, new_contact_data):
        driver = self.app.driver
        self.return_home_page()
        driver.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name('update').click()
        self.return_home_page()
