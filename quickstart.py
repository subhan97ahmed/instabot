# imports
from selenium import webdriver as w
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
# login credentials
insta_username = 'fail_ass'
insta_password = 'subhan09ahmedilm'

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = w.Chrome(options=chrome_options)
# driver = w.Chrome()
def login():
    xpath_usernametxt ='//*[@id="loginForm"]/div/div[1]/div/label/input'
    xpath_passwordtxt ='//*[@id="loginForm"]/div/div[2]/div/label/input'
    xpath_logintbn = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]'
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(5)
    # finding elements on the page
    print(driver.page_source)
    # usernametxt = driver.find_element_by_xpath(xpath_usernametxt)
    # passwordtxt = driver.find_element_by_xpath(xpath_passwordtxt)
    # loginbtn = driver.find_element_by_xpath(xpath_logintbn)
    # action = ActionChains(driver)
    # action.click(usernametxt)
    # action.send_keys(insta_username)
    # sleep(5)
    # action.click(passwordtxt)
    # action.send_keys(insta_password)
    # sleep(2)
    # action.click(loginbtn)
    # action.perform()
    # driver.implicitly_wait(5)
    # xpath_not = '//*[@id="react-root"]/section/main/div/div/div/div/button'
    # xpath_not2 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    # notbtn = driver.find_element_by_xpath(xpath_not)
    # notbtn.click()
    # driver.implicitly_wait(2)
    # notbtn2 = driver.find_element_by_xpath(xpath_not2)
    # notbtn2.click()
    # sleep(10)

def main_fuc():
    xpath_profile = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'
    profilebtn = driver.find_element_by_xpath(xpath_profile)
    action = ActionChains(driver)
    action.click(profilebtn)

login()
# main_fuc()
