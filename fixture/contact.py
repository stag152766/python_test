class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middle)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last)
        # submit contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def return_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()
