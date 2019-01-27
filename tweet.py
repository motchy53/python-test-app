import tweepy
import random
CONSUMER_KEY = '9GQNywbju4zOhysiTiUdhnPTi'
CONSUMER_SECRET = 'W2sRkf7KgDl4R85mwRj8TKCTowG1fVHRfpgZ1qk9SFjCFzVU37'
ACCESS_TOKEN = '928845844727578625-KYhomYZfHTYCb1kb8bHF8LRRjgeLPZz'
ACCESS_SECRET = 'RDob88Ou1bSGbeLg949pMHffDdt5UqrnPJv5Iyr9L9TAB'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)       
api = tweepy.API(auth,wait_on_rate_limit=True)#wait_on_rate_limit=True。これを指定するとAPIの使用制限にひかかったときに待ちます。
    

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PhantomJSのWebDriverオブジェクトを作成する。
driver = webdriver.PhantomJS()


# DMMのトップ画面を開く。
driver.get('http://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1032668/limit=30/sort=date/view=text/')

#driver.save_screenshot('search_results.png')
# 検索結果を表示する。
contents = [] 

for a in driver.find_elements_by_css_selector('p.ttl>a'):
        print(a.text)
        print(a.get_attribute('href'))
        content = a.text+"\n"+a.get_attribute('href')+"/fanza201901-001"+"\n"
        contents.append(content) # insert contents so slack can post only once
        contents
summary ="\n" 
for content in contents:
        summary = summary + content
        
tw= random.choice(contents)
api.update_status( "【新着】橋本ありな"+"\n" +tw)

print(tw)