from imports import *

import unittest
import page


class RoliaSearch(unittest.TestCase):    

    def setUp(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        ##self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.get('https://www.rolia.net/f/list.php?f=0#modal')
        self.actions = ActionChains(self.driver) # initialize ActionChain object
        self.page_class = page.MainPage
        self.current_page = None
        self.previous_page = None
        self.current_page_element_dict = {}
        
####### fill in credential information format like {('user id', 'password'): True}, "True "means it is positive test scenaio
        self.sign_in_credential_and_expected_result = {}

    def test_search_in_rolia_with_action_builder(self):

        self.test_load_page()
           
        test_data_expected_result = {'车险':True, '~':False}
        for key_value in list(test_data_expected_result.items()):

            elm_open_search_modal_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_open_search_modal_button'))
            elm_fill_search_keyword_input = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_search_keyword_input'))
            elm_click_search_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_search_button'))

            self.actions.move_to_element(elm_open_search_modal_button)             \
                .click(elm_open_search_modal_button)                          \
                .pause(3)                                                     \
                .move_to_element(elm_fill_search_keyword_input)               \
                .click(elm_fill_search_keyword_input)                         \
                .key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE) \
                .send_keys(key_value[0])                                              \
                .move_to_element(elm_click_search_button)                     \
                .click(elm_click_search_button)                               \
                .pause(3)                                                       \
                .perform()

            self.page_class = page.SearchResultsPage
            self.test_load_page()
            assert key_value[0] != self.current_page.locate_element(self.current_page_element_dict.get(    \
                'elm_search_result_search_string_input')).text,       \
                'Search result page is not shown'            
            assert self.current_page.is_results_found(key_value[1]),   \
                f'Actual result does not match with expected result of test data = {test_data_expected_result.get(key_value[0])}'

            time.sleep(3)
            saved_current_page = self.current_page

            if self.driver.back():
                self.current_page = self.previous_page
                self.previous_page = saved_current_page

###### Call Sign In/Off from other module              
        if self.test_sign_in_in_rolia_with_action_builder():
            self.test_sign_off_in_rolia_with_action_builder()
        

    def test_sign_in_in_rolia_with_action_builder(self):

        if not self.sign_in_credential_and_expected_result:
            print('Please fill in your sign in credential and expected result.')
            return
        

        if not isinstance(self.current_page, page.MainPage):
            self.page_class = page.MainPage
            self.test_load_page()
            
        if not self.current_page.is_sign_in_on_page():
            print('Can not sign in becuase you have signed in already')
            return

        test_data_expected_result = self.sign_in_credential_and_expected_result
        for key_value in list(test_data_expected_result.items()):
            elm_open_sign_in_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_open_sign_in_button'))
            self.actions.move_to_element(elm_open_sign_in_button)             \
                .click(elm_open_sign_in_button)                          \
                .pause(3)                                                   \
                .perform()
           
            elm_fill_user_id_input = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_user_id_input'))
            elm_fill_user_password_input = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_user_password_input'))
            elm_click_user_stay_in_checkbox = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_user_stay_in_checkbox'))
            elm_sign_on_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_sign_on_button'))
            self.actions.move_to_element(elm_fill_user_id_input)               \
                .send_keys(key_value[0][0] + Keys.ENTER)                                            \
                .move_to_element(elm_fill_user_password_input)               \
                .send_keys(key_value[0][1])                                     \
                .move_to_element(elm_click_user_stay_in_checkbox)               \
                .click(elm_click_user_stay_in_checkbox)                         \
                .pause(3)                                                       \
                .move_to_element(elm_sign_on_button)                     \
                .click(elm_sign_on_button)                               \
                .pause(5)                                               \
                .perform()

            time.sleep(3)

            assert not self.current_page.is_sign_in_on_page() or key_value[1],   \
                f'Actual result of sign in does not match with expected result of test data = {test_data_expected_result.get(key_value[0][0])}'



    def test_sign_off_in_rolia_with_action_builder(self):
       
        if not isinstance(self.current_page, page.MainPage):
            self.page_class = page.MainPage
            self.test_load_page()
                  
        if self.current_page.is_sign_in_on_page():
            if not self.test_sign_in_in_rolia_with_action_builder():
                print('Sign off test can not be done because user has not signed in.')
                return
        
        elm_open_user_management_menu_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_open_user_management_menu_button')) 
        self.actions.move_to_element(elm_open_user_management_menu_button)             \
            .click(elm_open_user_management_menu_button)                          \
            .pause(3)                                                   \
            .perform()

        elm_sign_off_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_sign_off_button'))            
        self.actions.move_to_element(elm_sign_off_button)                     \
            .click(elm_sign_off_button)                               \
            .pause(3)                                                   \
            .perform()

        time.sleep(3)
        
        elm_go_back_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_go_back_button'))            
        self.actions.move_to_element(elm_go_back_button)                     \
            .click(elm_go_back_button)                               \
            .pause(3)                                                   \
            .perform()


        assert self.current_page.is_sign_in_on_page(), 'Failed to sign off!'

        time.sleep(3)        


    def test_load_page(self):

        if self.current_page is not None:
            self.previous_page = self.current_page

        if self.page_class == page.MainPage:
            self.current_page = page.MainPage(self.driver)
            assert self.current_page.is_title_matches(), 'Main Page Is not matches'            
        elif self.page_class == page.SearchResultsPage:
            self.current_page = page.SearchResultsPage(self.driver)

        self.current_page_element_dict.update(dict((t[0], t[1]) for t in self.current_page.page_element_list))
        

    def tearDown(self):
        self.driver.quit()

   


if __name__ == '__main__':
    unittest.main()
