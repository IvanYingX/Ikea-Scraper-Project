
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class GetLinks:

    def get_links(self) -> list:

        """
        This method finds the container with all the sofas inside.
        This finds the container embedded in the webpage for the variables 
        we've selected (the sofas), and attaches a common HTML identifier to find each item.
        """
        self.driver = webdriver.Chrome()
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.BY = By
        
        self.sofa_items = self.driver.find_elements(self.BY.XPATH,".//div[@data-testid='plp-product-card']")

        #sofa link list 
        self.item_links_list = []
        self.image_links = []
        for sofa in self.sofa_items:
            a_tag = sofa.find_element(By.TAG_NAME,'a')
            sofa_link = a_tag.get_attribute('href')
            self.item_links_list.append(sofa_link)

            image_tag = sofa.find_element(self.BY.TAG_NAME, 'img')
            self.image_links.append(image_tag.get_attribute('src'))

            return self.item_links_list