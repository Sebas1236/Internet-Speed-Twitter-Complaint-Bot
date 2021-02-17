from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '1]/a/span[4]')
        go_button.click()

        # Wait 45 seconds before executing the next lines of code, depending of your internet speed.
        sleep(45)
        
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                      '2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f'Down: {self.down}')
        print(f'Up: {self.up}')

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                  '2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                     '2]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        
        sleep(2)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
                                                  '2]/div/div/div/div')

        tweet_message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                        f"{PROMISED_DOWN}down/{PROMISED_UP}up? "

        tweet.send_keys(tweet_message)

        sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)

        self.driver.quit()
        

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
