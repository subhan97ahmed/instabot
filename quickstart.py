# imports
from time import sleep
from selenium import webdriver as w
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
# login credentials
insta_username = 'username'
insta_password = 'password'

# chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
# driver = w.Chrome(options=chrome_options)
driver = w.Chrome()
def login():
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(5)
    xpath_usernametxt ='//*[@id="loginForm"]/div/div[1]/div/label/input'
    xpath_passwordtxt ='//*[@id="loginForm"]/div/div[2]/div/label/input'
    xpath_logintbn = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]'
    # finding elements on the page
    # print(driver.page_source)
    usernametxt = driver.find_element_by_xpath(xpath_usernametxt)
    passwordtxt = driver.find_element_by_xpath(xpath_passwordtxt)
    loginbtn = driver.find_element_by_xpath(xpath_logintbn)
    action = ActionChains(driver)
    action.click(usernametxt)
    action.send_keys(insta_username)
    sleep(5)
    action.click(passwordtxt)
    action.send_keys(insta_password)
    sleep(2)
    action.click(loginbtn)
    action.perform()
    driver.implicitly_wait(5)
    xpath_not = '//*[@id="react-root"]/section/main/div/div/div/div/button'
    xpath_not2 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    notbtn = driver.find_element_by_xpath(xpath_not)
    notbtn.click()
    driver.implicitly_wait(2)
    notbtn2 = driver.find_element_by_xpath(xpath_not2)
    notbtn2.click()
    sleep(10)

def profile_view():
    xpath_profilepic = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'
    xpath_profile ='/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div'
    profilepicbtn = driver.find_element_by_xpath(xpath_profilepic)
    profilepicbtn.click()
    sleep(5)
    profilebtn = driver.find_element_by_xpath(xpath_profile)
    profilebtn.click()
    sleep(4)

def like_by_tag(tags, nooflikes):
    # try:    
        for tag in tags:
            r = randint(1,10)
            print('sleeping for secs')
            sleep(r)
            xpath_searchtxt = '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'
            searchtxt = driver.find_element_by_xpath(xpath_searchtxt)
            action = ActionChains(driver)
            action.click(searchtxt)
            action.pause(4)
            action.send_keys(tag)
            action.pause(5)
            action.send_keys(Keys.RETURN)
            action.pause(5)
            action.send_keys(Keys.RETURN)
            action.perform()
            driver.implicitly_wait(5)
            xpath_firstpost ='/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[2]'
            firstpost = driver.find_element_by_xpath(xpath_firstpost)
            firstpost.click()
            no = 0
            while no < nooflikes:
                sleep(5)
                css_likebtn= 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button'
                likebtn = driver.find_element_by_css_selector(css_likebtn)
                likebtn.click()
                sleep(5)
                xpath_nextbtn = 'body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow'
                nextbtn = driver.find_element_by_css_selector(xpath_nextbtn)
                nextbtn.click()
                no= no +1
    # except :
    #     print('Problem in like by tags function')
    #it will follow the people for the followers of the users
def follow_the_followers_of(username, no):
    css_searchtxt = '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input'
    searchtxt = driver.find_element_by_css_selector(css_searchtxt)
    action = ActionChains(driver)
    action.click(searchtxt)
    action.pause(4)
    action.send_keys(username)
    action.pause(5)
    action.send_keys(Keys.RETURN)
    action.pause(5)
    action.send_keys(Keys.RETURN)
    action.perform()
    driver.implicitly_wait(5)
    css_followers='#react-root > section > main > div > header > section > ul > li:nth-child(2) > a'
    followers = driver.find_element_by_css_selector(css_followers)
    followers.click()
    driver.implicitly_wait(4)
    css_first ='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child(1) > div'
    first = driver.find_element_by_css_selector(css_first)
    first.click()
    action = ActionChains(driver)
    action.send_keys(Keys.DOWN)
    q=0
    while q <10:
        action.perform()
        q= q+1
    q=0
    act2 = ActionChains(driver)
    act2.send_keys(Keys.UP)
    while q <10:
        act2.perform()
        q= q+1
    r = 1
    while r<no:
        css_follow='body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({}) > div > div.Pkbci > button'.format(r)
        follow = driver.find_element_by_css_selector(css_follow)
        follow.click()
        action = ActionChains(driver)
        action.send_keys(Keys.DOWN)
        action.perform()
        tem = randint(1,5)
        print('sleeping for {}'.format(tem))
        sleep(tem)
        r=r+1
login()

# profile_view()
# like_by_tag(['#fails'], 5)
follow_the_followers_of('kirankhanmakeup', 40)
