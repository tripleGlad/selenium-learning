from imports import *

class BasePageElement(object):    

    def __init__(self, driver): 
        self.driver = driver

    # locator_type 
    #   0:clickable element no need to be filled
    #   1:fillable element, like <input>
    #   2:unfillable element, like <p>
    #   3:clickable element but EC does not work, like <input type="radio">
  
    def locate_element(self, locator, locator_type):
        ##  Element based on self.locator_type, this change is for ActionChains usage
        self._element = None
        if locator_type == 0:
            _element = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(locator))
        elif locator_type == 1 or locator_type == 2:
            _element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(locator))
        elif locator_type == 3:
            _element = WebDriverWait(self.driver, 100).until(
                lambda d: d.find_element(*locator))
        return _element




