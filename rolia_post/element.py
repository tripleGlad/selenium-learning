from imports import *

class BasePageElement(object):    

    def __init__(self, driver): 
        self.driver = driver

    # locator_type 
    #   1:fillable element, like <input> {keep this}
    #       & unfillable element, like <div> and can fill it by javascript
    #   2:clickable element, like button (includng internal span)
    #       & disable button but can only locate_element() when its disable attribute is gone.
    #   3:clickable element but EC does not work, like <input type="radio">
    #   4:iframe element
  
    def locate_element(self, locator, locator_type):
        ##  Element based on self.locator_type, this change is for ActionChains usage
        _element = None
        if locator_type == 1:
            _element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator))
        elif locator_type == 2:
            _element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator))
        elif locator_type == 3:
            _element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(*locator))
        elif locator_type == 4:
            _element = WebDriverWait(self.driver, 30).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        return _element



