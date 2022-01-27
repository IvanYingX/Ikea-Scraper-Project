

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from links import GetLinks
import uuid

class ExctractInfo:
     def extract_info(self):
        
        self.driver = webdriver.Chrome()
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.BY = By
        
        """
        This method extracts all the data points for each item, adds a UUID, and concatenates them into a dictionary.
        Each sofa has 5 data points available to scrape from the desired website (its name, price, product ID, description, image ). This method takes all of this scraped data, 
        adds a UUID to each variable (Universally Unique Identifier) and stores all 5 of these keys and values in a dictionary.
        """

        self.sofa_dict = {'UUID(v4)':[],'Product ID':[],'Name':[],'Price':[],'Description':[], 'Image':[], 'Image URL':[]}
        

        # extract images
        self.sofa_dict['Image'] = (GetLinks.image_links)

        for link in GetLinks.item_links_list:
            self.driver.get(link)

            #product_ID
            product_id_outer = self.driver.find_element(self.BY.XPATH, '//*[@id="content"]/div/div/div/div[2]')
            sofa_ID = product_id_outer.get_attribute('data-product-id')
            if sofa_ID not in self.sofa_dict['Product ID']:
                self.sofa_dict['Product ID'].append(sofa_ID)
            else:
                pass

            #sofa name
            item_name_outer = self.driver.find_element(self.BY.CSS_SELECTOR,"h1.range-revamp-header-section")
            item_name = item_name_outer.find_element(self.BY.XPATH,"./div").text
            self.sofa_dict['Name'].append(item_name)

            #sofa price
            item_price_outer= self.driver.find_element(self.BY.CSS_SELECTOR,'#content > div > div > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__buy-module-container > div > div.js-price-package.range-revamp-pip-price-package > div.range-revamp-pip-price-package__wrapper > div.range-revamp-pip-price-package__price-wrapper')
            item_price = item_price_outer.find_element(self.BY.XPATH,'./div').text
            self.sofa_dict['Price'].append(item_price)

            #sofa description
            item_desc_outer = self.driver.find_element(self.BY.CSS_SELECTOR,"h1.range-revamp-header-section")
            item_description = item_desc_outer.find_element(self.BY.TAG_NAME,"span").text
            self.sofa_dict['Description'].append(item_description)

            #sofa UUID
            self.sofa_dict['UUID(v4)'].append(str(uuid.uuid4()))

        return self.sofa_dict