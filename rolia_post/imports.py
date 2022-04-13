from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from locator import MainPageLocator, SearchResultsLocator
from element import BasePageElement as Elm

from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time

##class Actions(ActionChains):        
##    def wait(self, time_s: float):
##        self._action.append(lambda: time.sleep(time_s))
##        return self
##
##    def exec_script(self, js_code: str):
##        print(f'before execute_script {self.driver}')
##        self._actions.append(lambda: self.driver.execute_script(js_code))
##        print(f'after execute_script {js_code}')
##        return self
##
##
##class ActionPlus(object):
##    @property
##    def actions(self):
##        return self._actions_plus
##    
##    def __init__(self, driver):
##        self._actions_plus.actions = Actions(driver)
##        self._actions_plus.driver = driver
        
    









