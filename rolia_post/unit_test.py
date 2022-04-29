from imports import *

import unittest
import page


class RoliaSearch(unittest.TestCase):    

    def setUp(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.rolia.net/f/list.php?f=0#modal')
        self.test_data_file = os.getcwd() + '\\test_data.txt'
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver) # initialize ActionChain object
        self.current_page = None
        self.previous_page = None        
        self.current_page_element_dict = {}


    def test_post_in_rolia_with_action_builder(self):

        post_credential = self.exec_load_test_data(self.test_data_file, '#Post sign in credential#')
        user_id = list(post_credential)[0][0]
        user_password = list(post_credential)[0][1]
        is_valid_credential = list(post_credential.values())[0]
        if not is_valid_credential:
            self.skipTest("invalid credential and expected result")

        
        self.exec_load_page(page.MainPage)        
        self.exec_sign_in_in_rolia_with_action_builder(user_id, user_password, is_valid_credential)
        
        test_data_expected_result = self.exec_load_test_data(self.test_data_file, '#Post content and expected result#')        
        for key_value in list(test_data_expected_result.items()):            
            
            elm_click_publish_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_publish_button'))
            self.actions.move_to_element(elm_click_publish_button)             \
                .click(elm_click_publish_button)                          \
                .pause(3)                                                     \
                .perform()

            time.sleep(3)

            elm_fill_new_post_title_textarea = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_new_post_title_textarea'))
            elm_open_new_post_forum_change_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_open_new_post_forum_change_button'))
            elm_click_new_post_forum_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_new_post_forum_button'))
            elm_click_new_post_cancel_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_new_post_cancel_button'))

            self.driver.execute_script("arguments[0].value = arguments[1];", elm_fill_new_post_title_textarea, key_value[0][0])
            self.actions.move_to_element(elm_fill_new_post_title_textarea)               \
                .send_keys(Keys.SPACE)                                              \
                .perform()

            elm_fill_new_post_iframe = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_new_post_iframe'))
            assert elm_fill_new_post_iframe, 'Can not locate and switch to iframe element'
            elm_fill_new_post_iframe_p = self.current_page.locate_element(self.current_page_element_dict.get('elm_fill_new_post_iframe_p'))
            assert elm_fill_new_post_iframe_p, 'Can not locate iframe p element'
           
            self.driver.execute_script("arguments[0].textContent = arguments[1];", elm_fill_new_post_iframe_p, key_value[0][1])
            self.driver.switch_to.default_content()

            time.sleep(3)
                        
            self.actions.move_to_element(elm_fill_new_post_title_textarea)               \
                .key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN)              \
                .pause(3)                                                       \
                .perform()

            time.sleep(3)
            
            self.actions.move_to_element(elm_open_new_post_forum_change_button)               \
                .click(elm_open_new_post_forum_change_button)                         \
                .pause(3)                                                       \
                .perform()

            self.actions.move_to_element(elm_click_new_post_forum_button).click().perform()

            time.sleep(3)
            
            if key_value[1]:
                elm_click_new_post_submit_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_click_new_post_submit_button'))
                assert elm_click_new_post_submit_button, 'Can not locate submit button!'

                self.actions.move_to_element(elm_click_new_post_submit_button).click().perform()
            else:
                self.actions.move_to_element(elm_click_new_post_cancel_button).click().perform()

            time.sleep(3)

            if key_value[1]:

                updated_locator = self.exec_fill_locator_argument(self.current_page_element_dict.get('elm_new_post_presentation_span'), user_id)
                elm_new_post_presentation_span = self.current_page.locate_element(updated_locator)
                assert elm_new_post_presentation_span, 'Failed to submit a post.'

                updated_locator = self.exec_fill_locator_argument(self.current_page_element_dict.get('elm_new_post_presentation_dropdown_button'), user_id)
                elm_new_post_presentation_dropdown_button = self.current_page.locate_element(updated_locator)

                self.actions.move_to_element(elm_new_post_presentation_dropdown_button)               \
                    .click(elm_new_post_presentation_dropdown_button)                                   \
                    .pause(3)                                                       \
                    .perform()

                time.sleep(3)

                updated_locator = self.exec_fill_locator_argument(self.current_page_element_dict.get('elm_new_post_presentation_delete_link'), user_id)
                elm_new_post_presentation_delete_link = self.current_page.locate_element(updated_locator)
                
                self.actions.move_to_element(elm_new_post_presentation_delete_link)               \
                    .click(elm_new_post_presentation_delete_link)                   \
                    .pause(3)                                                       \
                    .perform()

                time.sleep(1)

                alert = self.driver.switch_to.alert
                alert.accept()

                self.driver.switch_to.default_content()

            time.sleep(3)

            
        self.exec_sign_off_in_rolia_with_action_builder()

        
    def test_sign_in_and_sign_off_with_action_builder(self):

        test_data_expected_result = self.exec_load_test_data(self.test_data_file, '#Sign in credential and expected result#')

        self.exec_load_page(page.MainPage)
        for key_value in list(test_data_expected_result.items()):
        
            self.exec_sign_in_in_rolia_with_action_builder(key_value[0][0], key_value[0][1], key_value[1])
            if key_value[1]:
                self.exec_sign_off_in_rolia_with_action_builder()


        
    def test_search_in_rolia_with_action_builder(self):

        self.exec_load_page(page.MainPage)
                  
        test_data_expected_result = self.exec_load_test_data(self.test_data_file, '#Search content and expected result#')
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

            self.exec_load_page(page.SearchResultsPage)
            assert key_value[0] != self.current_page.locate_element(self.current_page_element_dict.get(    \
                'elm_search_result_search_string_input')).text,       \
                'Search result page is not shown'            
            assert not key_value[1] == self.current_page.is_results_found(),     \
                f'Actual result does not match with expected result of test data = {test_data_expected_result.get(key_value[0])}'

            time.sleep(3)
            saved_current_page = self.current_page

            if self.driver.back():
                self.current_page = self.previous_page
                self.previous_page = saved_current_page


        self.exec_load_page(page.MainPage)

                   

    def exec_sign_in_in_rolia_with_action_builder(self, user_id, user_password, is_valid_credential):

        assert user_id is not None and user_password is not None and is_valid_credential is not None, "miss credential and expected result"
        assert isinstance(self.current_page, page.MainPage), 'Please sign in from proper page.'
        assert self.current_page.is_sign_in_on_page(), 'Can not sign in becuase you have signed in already'
            
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
            .send_keys(user_id + Keys.ENTER)                                            \
            .move_to_element(elm_fill_user_password_input)               \
            .send_keys(user_password)                                     \
            .move_to_element(elm_click_user_stay_in_checkbox)               \
            .click(elm_click_user_stay_in_checkbox)                         \
            .pause(3)                                                       \
            .move_to_element(elm_sign_on_button)                     \
            .click(elm_sign_on_button)                               \
            .pause(5)                                               \
            .perform()

        time.sleep(3)

        assert self.current_page.is_sign_in_on_page() ^ is_valid_credential,   \
            f'Actual result of sign in does not match with expected result of test data = {is_valid_credential}'



    def exec_sign_off_in_rolia_with_action_builder(self):

        assert isinstance(self.current_page, page.MainPage), 'Please sign off from proper page.'
        assert not self.current_page.is_sign_in_on_page(), 'Sign off test can not be done because user has not signed in.'
        
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

        time.sleep(6)
        
        elm_go_back_button = self.current_page.locate_element(self.current_page_element_dict.get('elm_go_back_button'))            
        self.actions.move_to_element(elm_go_back_button)                     \
            .click(elm_go_back_button)                               \
            .pause(3)                                                   \
            .perform()


        assert self.current_page.is_sign_in_on_page(), 'Failed to sign off!'     



    def exec_load_page(self, page_class: page.BasePage):

        if self.current_page is not None:
            self.previous_page = self.current_page

        if page_class == page.MainPage:
            self.current_page = page.MainPage(self.driver)
            assert self.current_page.is_title_matches(), 'Main Page Is not matches'            
        elif page_class == page.SearchResultsPage:
            self.current_page = page.SearchResultsPage(self.driver)

        self.current_page_element_dict.update(dict((t[0], t[1]) for t in self.current_page.page_element_list))

        
    def exec_fill_locator_argument(self, locator, replaced_argument):

        if locator == () or replaced_argument is None:
            return locator_argument_fill_pair
        
        list_tuple_value = list(locator)
        list_inside_tuple_value = list(list_tuple_value[0])
        list_inside_tuple_value[1] = list_inside_tuple_value[1].format(replaced_argument)
        list_tuple_value[0] = tuple(list_inside_tuple_value)
        return tuple(list_tuple_value)

    def exec_load_test_data(self, path, model):

        with open(path, encoding="utf8") as f:
            lines = [line.rstrip('\n') for line in f]
            return ast.literal_eval(next(l.replace(model, "") for l in lines if model in l))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
