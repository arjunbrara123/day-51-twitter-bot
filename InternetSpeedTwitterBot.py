from selenium import webdriver
from time import sleep
from os import environ

CHROME_DRIVER_PATH = "chromedriver.exe"
TWITTER_USERNAME = environ['TWITTER_USERNAME']
TWITTER_PASSWORD = environ['TWITTER_PASSWORD']
PROMISED_UP = 150
PROMISED_DOWN = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = None
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        cookies_consent = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        cookies_consent.click()
        sleep(2)
        cookie_warning = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/a')
        cookie_warning.click()
        btn_go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        btn_go.click()
        sleep(60)
        speed_down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = speed_down.text
        speed_up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = speed_up.text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://twitter.com/login?lang=en-gb")
        sleep(3)
        input_username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        input_username.send_keys(TWITTER_USERNAME)
        input_password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        input_password.send_keys(TWITTER_PASSWORD)
        btn_signin = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
        btn_signin.click()
        msg = f"Hey ISP, why is my internet speed {self.down} down / {self.up} up, when I was promised 50 down / 10 up?"
        sleep(3)
        tweet_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(msg)