import PIL as Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


websiteurl = "http://localhost:3000"
signinID = "test-sign-in"
emailinput = "prathamesh.rjpawar@gmail.com"
passwordinput = "pratham"
test_login = "test-login"
fooditem = "rice"
amount = 3
currency = "bowl"
productID = "6369eb9ceb83562a689f28a5"


def testing_links():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:3000/')
    links = driver.find_elements(By.CSS_SELECTOR, 'a')

    print("Testing links...")
    start = time.time()

    working_links = 0
    bad_links = 0
    bad_links_list = []
    for link in links:
        r = requests.head(link.get_attribute('href'))
        if r.status_code != 400:
            working_links += 1
        else:
            bad_links += 1
            bad_links_list.append((link.get_attribute('href'),
                                   r.status_code))
    context = {"working_links": working_links,
               "bad_links_list": bad_links_list, "bad_links": bad_links,
               "links_len": len(links), "time_links": round((time.time() - start), 3)}
    print(context)
    return context


def testing_imgs():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:3000/')
    links = driver.find_elements(By.CSS_SELECTOR, 'img')

    print("Testing Images...")
    start = time.time()

    working_links = 0
    bad_links = 0
    bad_links_list = []
    for link in links:
        r = requests.head(link.get_attribute('src'))
        if r.status_code != 400:
            working_links += 1
        else:
            bad_links += 1
            bad_links_list.append((link.get_attribute('href'),
                                   r.status_code))
    context = {"working_images": working_links,
               "bad_images_list": bad_links_list, "bad_images": bad_links,
               "links_len": len(links), "time_images": round((time.time() - start), 3)}
    print(context)
    print(" \n\n\n_______ Test Success ________\n\n\n")
    return context


def testing_workflow():
    # open website
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(websiteurl)

        print("testing working")
        time.sleep(3)
        # click on menu button
        driver.find_element(By.ID, 'menubutton').click()
        time.sleep(3)
        driver.get("http://localhost:3000/login")
        time.sleep(5)
        
        
        print("Signup Page opened")

        #fill login form
        driver.find_element(By.ID, 'emailinput').send_keys(emailinput)
        time.sleep(3)
        driver.find_element(By.ID, 'passwordinput').send_keys(passwordinput)
        time.sleep(3)
        print("entered user credentials")
        driver.find_element(By.ID, 'submitbutton').click()
        time.sleep(5)
        print("Login Success")
        
        driver.find_element(By.ID, 'menubutton').click()
        time.sleep(5)
        driver.find_element(By.ID, 'MY PROFILE2').click()
        time.sleep(5)
        print("Checking profile")
        
        driver.find_element(By.ID, 'menubutton').click()
        time.sleep(5)
        driver.find_element(By.ID, 'GET JOBS0').click()
        time.sleep(15)
        print("Job module automation success")
        
        driver.find_element(By.ID, 'menubutton').click()
        time.sleep(5)
        driver.find_element(By.ID, 'MY HEALTH0').click()
        time.sleep(5)
        print("Checking Health")
        
        # check calorie intake with an example
        driver.find_element(By.ID, 'whateat').send_keys(fooditem)
        time.sleep(3)
        driver.find_element(By.ID, 'howmucheat').send_keys(amount)
        time.sleep(3)
        driver.find_element(By.ID, 'currency').click()
        time.sleep(3)
        driver.find_element(By.ID, 'bowl').click()
        time.sleep(5)
        driver.find_element(By.ID, 'healthbutton').click()
        time.sleep(15)
        print("health module automation success")
        
        driver.find_element(By.ID, 'menubutton').click()
        time.sleep(5)
        driver.find_element(By.ID, 'closebutton').click()
        time.sleep(5)
        driver.get(websiteurl)
        time.sleep(5)

        print(" \n\n\n_______ Test Success ________\n\n\n")

    except:
        print(" \n\n\n_______ Test Failed ________\n\n\n")
        exit()

# testing_links()
# testing_imgs()

testing_workflow()