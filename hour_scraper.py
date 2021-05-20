from selenium import webdriver
from datetime import datetime
import time
def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:/Users/e2008233/Downloads/chromedriver", options=options)
    driver.set_window_size(1120, 1000)

    now = datetime.now()

    month = now.strftime("%m")
    day = now.strftime("%d")

    url = "https://nventthermal.harvestapp.com/time/week/2021/"+month+"/"+ day +"/3754938"
    driver.get(url)

    WorkEmailStr = "Jiachen.Xu@nVent.com"
    PasswordStr = "Spring2021"

    email = driver.find_element_by_id('email')
    email.send_keys(WorkEmailStr)

    password = driver.find_element_by_id('password')
    password.send_keys(PasswordStr)

    SignInButton = driver.find_element_by_id('log-in')
    SignInButton.click()

    hours = []
    table = driver.find_elements_by_xpath('//input[@type="text"]')
    for i in table:
        a = i.get_attribute('value')
        if a == "":
            hours.append(0)
        else:
            hours.append(float(a))

    return hours