from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.jd.com/')

    btn_rush = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.LINK_TEXT, "秒杀")))
    btn_rush.click()
