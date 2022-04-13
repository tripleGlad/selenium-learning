from selenium.webdriver.common.by import By

class MainPageLocator(object):
##  Regular Fucnctions (1.Refresh, 2.Post New, 3.Change Category, 4.Search, 5.Choice Topics, 6.New Topics, 7.Sign in)

##  1. Refresh Part
    REFRESH_PAGE_BUTTON = (By.XPATH, '//button[contains(@onclick,"refreshForumUnit(0, 50, 5100);")]//span')

##  4. Search Part
    OPEN_SEARCH_MODAL_BUTTON = (By.XPATH, '//button[@class="btn btn-default hidden-xs"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')      # There are two elements found and default returned the first one
    SIMPLE_SEARCH_KEY_WORD = (By.NAME, 'q')
    SIMPLE_SEARCH_POST_NUMBER= (By.NAME, 'p')

##  3. Change Category Part
    CHANGE_CATEGORY_BUTTON = (By.XPATH, '//button[@data-target="#forumCtgListModal"]')
    SOCIAL_POLICE_LINK = (By.XPATH, '//div[@class="modal-content"]//a[text()="社会政治"]')
    CHANGE_CATEGORY_2_BUTTON = (By.XPATH, '//span[@class="hidden-sm hidden-xs with-icon"]')


##  2. Post New Part
    OPEN_NEW_POST_FORUM_CHANGE_BUTTON = (By.XPATH, '//span[@id="pe-btn-change-forum"]')    
    PUBLISH_BUTTON = (By.XPATH, '//span[text()="发表"]')
    NEW_POST_TITLE = (By.ID, 'title')
    NEW_POST_CONTENT_IFRAME = (By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')
    NEW_POST_CONTENT_IFRAME_P = (By.XPATH, '/html/body/p')
    NEW_POST_FORUM = (By.ID, 'fno-65') ## fno-65: 水坛
    NEW_POST_SUBMIT_BUTTON = (By.XPATH, '//button[@class="nav-button btn submit btn-success"][text()="提交"]')
    NEW_POST_CANCEL_BUTTON = (By.XPATH, '//i[@class="fa fa-times btn btn-default mr20"]')
    NEW_POST_PRESENTATION_SPAN = (By.XPATH, '//li[@class="post  "][@data-author="{0}"]') # '//li[@class="post  "][@data-author="{0}"]//span[text()="{1}"]')
    NEW_POST_PRESENTATION_DROPDOWN_BUTTON = (By.XPATH, '//li[@class="post  "][@data-author="{0}"]//button[@class="btn dropdown-toggle ctxBtnCaret"]')
    NEW_POST_PRESENTATION_DELETE_LINK = (By.XPATH, '//li[@class="post  "][@data-author="{0}"]//a[text()="删除帖子"]')
   

##  7. Sign in Part
    OPEN_SIGN_IN_BUTTON = (By.XPATH, '//a[@class="btn btn-default signIn"]')
    USER_ID = (By.ID, 'signonuserid')
    USER_PASSWORD = (By.ID, 'signonpassword')
    USER_STAY_IN = (By.NAME, 'staySignedIn')
    SIGN_ON_BUTTON = (By.NAME, 'signonsubmit')
    OPEN_USER_MANAGEMENT_MENU_BUTTON = (By.XPATH, '//button[@class="btn btn-default dropdown-toggle"]')
    SIGN_OFF_BUTTON = (By.XPATH, '//span[text()="退出"]')
    GO_BACK_BUTTON = (By.XPATH, '//a[text()="Go Back"]')
    

class SearchResultsLocator(object):
    SEARCH_RESULTS_SEARCH_STRING_INPUT = (By.ID, 'gsc-i-id1')


    

    

    
       
