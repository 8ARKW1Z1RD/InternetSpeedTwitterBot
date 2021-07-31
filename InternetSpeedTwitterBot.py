from selenium import webdriver
import tweepy

consumer_api_key = ""
consumer_api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = "C:/Users/{user_name}/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path= chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        click_go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        click_go.click()

    # generating the authenticating instance
    def Oauth(self) :
        try :
            auth = tweepy.OAuthHandler(consumer_key=consumer_api_key, consumer_secret=consumer_api_secret)
            auth.set_access_token(access_token, access_token_secret)
            return auth
        except Exception as e :
            return None



