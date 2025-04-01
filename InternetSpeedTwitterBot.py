from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
INTERNET_URL = "https://www.speedtest.net/pl"
TWITTER_URL = "https://x.com/home"
PROMISED_DOWN = int(os.environ["PROMISED_DOWN"])
PROMISED_UP = int(os.environ["PROMISED_UP"])
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(INTERNET_URL)
        time.sleep(1)
        reject_cookies = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        reject_cookies.click()

        start = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start.click()

        time.sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME,
                                             value="result-data-large.number.result-data-value.download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME,
                                             value="result-data-large.number.result-data-value.upload-speed").text)



    def speed_too_low(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            return True
        else:
            return False


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        time.sleep(3)
        email = self.driver.find_element(By.CLASS_NAME,
        value="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 "
              "r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7".replace(" ", "."))

        email.send_keys(TWITTER_EMAIL, Keys.ENTER)

        time.sleep(2)
        username = self.driver.find_element(By.CLASS_NAME,
        value="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj "
              "r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7".replace(" ", "."))

        username.send_keys(TWITTER_USERNAME, Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.CLASS_NAME,
        value="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf "
              "r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7".replace(" ", "."))

        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        time.sleep(5)
        reject_cookies = self.driver.find_element(By.CLASS_NAME,
        value="css-1jxf684 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo "
              "r-1ttztb7 r-qvutc0 r-poiln3 r-a023e6 r-rjixqe".replace(" ","."))
        reject_cookies.click()

        message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        time.sleep(1)
        tweet = self.driver.find_element(By.CLASS_NAME,
        value="public-DraftStyleDefault-block public-DraftStyleDefault-ltr".replace(" ", "."))
        tweet.send_keys(message)

        time.sleep(1)
        post = self.driver.find_element(By.CLASS_NAME,
        value="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-1cwvpvk r-2yi16 r-1qi8awa "
              "r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l".replace(" ","."))
        post.click()

        time.sleep(2)
        self.driver.quit()
