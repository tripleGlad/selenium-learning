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
import os
import ast











