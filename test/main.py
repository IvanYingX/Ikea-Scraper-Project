
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import unittest
from links import GetLinks
from info import ExctractInfo
from page import SofaPage


class Scraper(unittest.TestCase):
    def setUp(self, url: str = "https://www.ikea.com/gb/en/"):
        self.GetLinks = GetLinks
        self.ExtractInfo = ExctractInfo
        self.SofaPage = SofaPage
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.BY = By
        self.driver = webdriver.Chrome() 
        self.driver.get(url)
        
        xpath = '//*[@id="onetrust-accept-btn-handler"]'
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable((self.BY.XPATH, xpath))).click()


    def test_navigate_to_items(self):
        self.SofaPage.navigate_to_items()
        cuurent_page_url = self.driver.current_url()
        
        exp_url = "https://www.ikea.com/gb/en/cat/sofas-fu003/"
        self.assertEquals(exp_url, cuurent_page_url)
       

    def test_get_links(self):
        self.GetLinks.get_links()

        self.assertGreater(self.GetLinks.get_links(), 1)

    def test_extract_info(self):
        self.ExtractInfo.extract_info()

        self.assertGreater(len(ExctractInfo.extract_info(['Image'])), 1)
   
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
