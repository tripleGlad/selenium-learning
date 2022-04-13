from imports import *

class BasePage(object):    
    def __init__(self, driver, page_element_list: list):
        self.driver = driver
        self.element = Elm(self.driver)
        self._page_element_list = page_element_list


    def locate_element(self, locator_locator_type_pair):
        return self.element.locate_element(locator_locator_type_pair[0], locator_locator_type_pair[1])

    @property
    def page_element_list(self):
        return self._page_element_list
    
class MainPage(BasePage):

    def __init__(self, driver):

        _page_element_list = []
        
##      Search Part        
        _page_element_list.append(('elm_open_search_modal_button', (MainPageLocator.OPEN_SEARCH_MODAL_BUTTON, 2)))
        _page_element_list.append(('elm_fill_search_keyword_input', (MainPageLocator.SIMPLE_SEARCH_KEY_WORD, 1)))
        _page_element_list.append(('elm_click_search_button', (MainPageLocator.SEARCH_BUTTON, 3)))

##      Change Category Part
        _page_element_list.append(('elm_click_change_category_button', (MainPageLocator.CHANGE_CATEGORY_BUTTON, 2)))

##      Sign In Part
        _page_element_list.append(('elm_open_sign_in_button', (MainPageLocator.OPEN_SIGN_IN_BUTTON, 2)))
        _page_element_list.append(('elm_fill_user_id_input', (MainPageLocator.USER_ID, 1)))
        _page_element_list.append(('elm_fill_user_password_input', (MainPageLocator.USER_PASSWORD, 1)))
        _page_element_list.append(('elm_click_user_stay_in_checkbox', (MainPageLocator.USER_STAY_IN, 2)))
        _page_element_list.append(('elm_sign_on_button', (MainPageLocator.SIGN_ON_BUTTON, 2)))        
        _page_element_list.append(('elm_open_user_management_menu_button', (MainPageLocator.OPEN_USER_MANAGEMENT_MENU_BUTTON, 2)))
        _page_element_list.append(('elm_sign_off_button', (MainPageLocator.SIGN_OFF_BUTTON, 2)))
        _page_element_list.append(('elm_go_back_button', (MainPageLocator.GO_BACK_BUTTON, 2)))

##      Post New Part
        _page_element_list.append(('elm_open_new_post_forum_change_button', (MainPageLocator.OPEN_NEW_POST_FORUM_CHANGE_BUTTON, 2)))
        _page_element_list.append(('elm_click_publish_button', (MainPageLocator.PUBLISH_BUTTON, 2)))
        _page_element_list.append(('elm_fill_new_post_title_textarea', (MainPageLocator.NEW_POST_TITLE, 1)))
        _page_element_list.append(('elm_fill_new_post_iframe', (MainPageLocator.NEW_POST_CONTENT_IFRAME, 4)))
        _page_element_list.append(('elm_fill_new_post_iframe_p', (MainPageLocator.NEW_POST_CONTENT_IFRAME_P, 1)))
        _page_element_list.append(('elm_click_new_post_forum_button', (MainPageLocator.NEW_POST_FORUM, 3)))
        _page_element_list.append(('elm_click_new_post_submit_button', (MainPageLocator.NEW_POST_SUBMIT_BUTTON, 2)))
        _page_element_list.append(('elm_click_new_post_cancel_button', (MainPageLocator.NEW_POST_CANCEL_BUTTON, 2)))
        _page_element_list.append(('elm_new_post_presentation_span', (MainPageLocator.NEW_POST_PRESENTATION_SPAN, 1)))        
        _page_element_list.append(('elm_new_post_presentation_dropdown_button', (MainPageLocator.NEW_POST_PRESENTATION_DROPDOWN_BUTTON, 2)))
        _page_element_list.append(('elm_new_post_presentation_delete_link', (MainPageLocator.NEW_POST_PRESENTATION_DELETE_LINK, 2)))
        
       

        super().__init__(driver, _page_element_list)     

        
    def is_title_matches(self):
        return '枫下论坛主坛 p1 @枫下论坛 The Rolia Forum' in self.driver.title


    def is_sign_in_on_page(self):
        return 'Sign In' in self.driver.page_source

        
class SearchResultsPage(BasePage):    

    def __init__(self, driver):   

        _page_element_list = []
        _page_element_list.append(('elm_search_result_search_string_input',     \
            (SearchResultsLocator.SEARCH_RESULTS_SEARCH_STRING_INPUT, 1)))        
        super().__init__(driver, _page_element_list)


    def is_results_found(self):
        
            return 'No Results' in self.driver.page_source

   



        

