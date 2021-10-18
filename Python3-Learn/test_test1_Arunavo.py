# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(696, 706)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("amazon")
    self.driver.find_element(By.CSS_SELECTOR, ".sbre .wM6W7d > span").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cfxYMc")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,111.19999694824219)")
    self.driver.find_element(By.CSS_SELECTOR, ".g:nth-child(1) > div:nth-child(2) > .tF2Cxc .LC20lb").click()
    element = self.driver.find_element(By.LINK_TEXT, "Best Sellers")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".hm-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".hmenu > li:nth-child(8) div").click()
    element = self.driver.find_element(By.LINK_TEXT, "Amazon Prime Video")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "All-new Fire TV Stick (3rd Gen)").click()
  
