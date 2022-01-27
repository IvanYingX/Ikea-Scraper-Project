from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class SofaPage:
    
     def navigate_to_items(self):
        """
        This mathod navigates to the sofa category.
        This navigates to the desired web page - in this case, the one displaying all the sofas - through
        clicking a series of nested links one at a time, waiting an adequate amount of time between each click.
        
        The "Show More" button obtains more items and clicks it until as many items as we need are displayed.
        In this instance, there are 23 items on page 1, and 24 items on all other pages.
        """ 
        self.driver = webdriver.Chrome()
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.BY = By

        menu_button = '/html/body/header/div/div/div/ul/li[7]/button/span'
        products_button = '/html/body/aside/div[3]/nav[1]/ul[1]/li[1]/a'
        furniture_button = '/html/body/aside/div[3]/nav[2]/ul/li[6]/a'
        sofas_button = '/html/body/aside/div[3]/nav[2]/ul/li[6]/nav/ul/li[5]/a'

        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable((self.BY.XPATH, menu_button))).click()
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable((self.BY.XPATH, products_button))).click()
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable((self.BY.XPATH, furniture_button))).click()
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable((self.BY.XPATH, sofas_button))).click()         
        
        for i in range(0):
            try:
                show_more_button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div/div/div[5]/div[1]/div/div[3]/a')))
                self.driver.execute_script("arguments[0].click();", show_more_button)
            except TimeoutException:
                pass   