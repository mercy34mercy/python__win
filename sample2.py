# coding:utf-8
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get('https://google.co.jp/')
    
    searchElement = driver.find_element_by_name("q")
    searchElement.send_keys('selenium')

    searchElement.submit()
    driver.quit()