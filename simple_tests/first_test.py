#Simple assignment
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

##''' IE Browser '''
##options = webdriver.IeOptions()
##options.ignore_zoom_level = True
##options.ignore_protected_mode_settings = True
##options.ensure_clean_session = True
##with webdriver.Ie(options=options) as driver:



with webdriver.Chrome(ChromeDriverManager().install()) as driver:
    search_string = "tennis"
    try:
        driver.get("https://ca.sports.yahoo.com/")    
        search_bar = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.CSS_SELECTOR,".search-input"))
        search_bar.clear()   
        search_bar.send_keys(search_string)
        search_bar.send_keys(Keys.RETURN)
    
        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//a[contains(.,\'" + search_string.capitalize() + "\')]")))
        if (result_element):
            print("search result is not empty")
            print(result_element.get_attribute('innerHTML'))
    except BaseException as err:
        print(f"Unexpected exception: {err=} {type(err)=}")
    
    print(driver.title)
    print(driver.current_url)


