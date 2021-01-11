from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_driver_path = r'chromedriver.exe'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.instagram_pwd = os.environ["INSTAGRAM_PWD"]
        self.instagram_email = os.environ["INSTAGRAM_EMAIL"]
        self.instagram_url = "https://www.instagram.com"
        self.follower_buttons = []

    def login(self):
        self.driver.get(f"{self.instagram_url}/accounts/login/")
        base_window = self.driver.window_handles[0]
        try:
            #cookie_window = self.driver.window_handles[1]
            #self.driver.switch_to.window(cookie_window)
            accept_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
            accept_button.click()
            #self.driver.switch_to.window(base_window)
        except:
            pass
        time.sleep(4)
        self.email_input = self.driver.find_element_by_name("username")
        self.email_input.send_keys(self.instagram_email)
        self.password_input = self.driver.find_element_by_name("password")
        self.password_input.send_keys(self.instagram_pwd)
        time.sleep(2)
        self.password_input.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            # Handle "Save your login info?" pop-up
            not_now_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
            not_now_button.click()
        except:
            pass
        time.sleep(2)
        try:
            # Handle "Turn on Notifications" pop-up
            not_now_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            not_now_button.click()
        except:
            pass


    def find_followers(self, account_to_follow):
        self.driver.get(f"{self.instagram_url}/{account_to_follow}/")
        time.sleep(3)
        href_string = f"/{account_to_follow}/followers/"
        follower_button = self.driver.find_element_by_xpath(f"//*[@href='{href_string}']")
        follower_button.click()
        time.sleep(2)
        self.follower_buttons = self.driver.find_elements_by_css_selector("div .PZuss li button")

    def follow(self):
        for button_x in self.follower_buttons:
            time.sleep(3)
            button_x.click()

    def close_follower_window(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()