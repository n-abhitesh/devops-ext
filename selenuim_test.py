from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.service = Service(executable_path='./chromedriver.exe')
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://amazon.in")
        self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]' ).send_keys("Books")
        self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    def test_search_2(self):
        self.driver.get("https://amazon.in") 
        self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]' ).send_keys("Headphones")
        self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nmman/OneDrive/Desktop/ES_lab_internal/devops'))
