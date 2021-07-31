from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time
import tweepy

PROMISED_DOWN = 200
PROMISED_UP = 200

check_internet_speed = InternetSpeedTwitterBot()

try:
    check_internet_speed.get_internet_speed()
    time.sleep(60)
    down_speed = check_internet_speed.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    up_speed = check_internet_speed.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
except Exception:
    print("error")
else:
    oauth = check_internet_speed.Oauth()
    api = tweepy.API(oauth)
    api.update_status(f"#testing pls ignore. Hey @Actcorp, the current download speed of ({down_speed.text})  and upload speed of ({up_speed.text}) is way less than your advertised.Fix it pls.#100daysofcode #python ")
    print(down_speed.text)
    print(up_speed.text)



