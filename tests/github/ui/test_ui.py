import requests
import src.config.config
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_api():
    print('testing parameters getter')
    response = requests.get(src.config.config.config_all.get("URLTEST"))

    assert response.status_code == src.config.config.config_all.get("response_ok")

def test_github_login_negative():
#github login wrong SELENIUM
    
    # create webdriver object
    driver = webdriver.Firefox()
    driver.get('https://www.github.com/login')
    
    # enter wring credentils
    login_field = driver.find_element(By.ID, 'login_field')
    login_field.send_keys('wrong_email')
    
    pass_field = driver.find_element(By.CSS_SELECTOR, '#password')
    action = ActionChains(driver)
    action.move_to_element(pass_field).send_keys('wrong_pass')

    # click button
    pass_field_click = driver.find_element(By.NAME, 'commit')
    pass_field_click.click()

    # check error msg
    error_msg = driver.find_element(By.ID, 'js-flash-container')
    print(f'error msg: {error_msg}')
    time.sleep(5)
    assert error_msg is not None

    driver.close()
    

    