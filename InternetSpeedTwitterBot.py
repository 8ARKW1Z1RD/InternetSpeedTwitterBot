from selenium import webdriver
import tweepy

consumer_api_key = "ex7BY58VASQXRVeiLFeSNKqOB"
consumer_api_secret = "7JgEs9p18zH73SMnp55ONvTqluW8jUrD6mCipdFsnjEb8QP980"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMl6RwEAAAAA4lPWrn77X2CYGiqx2AGg%2BSqyd9I%3DViUwNjyzaOIpbDNRRAbokXqsQEeFNwbDQ3ys7h82kLvSb8E9rC"
access_token = "182242770-URjGZtmtAnSDr7y7g68HZ2NVorFUna4UGGwQcMBE"
access_token_secret = "cDPoC5bXkl5WJSqf12CvEzsN8YZhYEN4RDcwC6O0uwIeb"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = "C:/Users/rajesh_kumar_v1/chromedriver_win32/chromedriver.exe"
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



