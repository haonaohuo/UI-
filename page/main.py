from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        self.steps("..//page/main.yaml")