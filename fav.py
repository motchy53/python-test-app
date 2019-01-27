#お気に入り用
# Tweepyライブラリをインポート
import tweepy
# 各種キーをセット
CONSUMER_KEY = '9GQNywbju4zOhysiTiUdhnPTi'
CONSUMER_SECRET = 'W2sRkf7KgDl4R85mwRj8TKCTowG1fVHRfpgZ1qk9SFjCFzVU37'
ACCESS_TOKEN = '928845844727578625-KYhomYZfHTYCb1kb8bHF8LRRjgeLPZz'
ACCESS_SECRET = 'RDob88Ou1bSGbeLg949pMHffDdt5UqrnPJv5Iyr9L9TAB'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#APIインスタンスを作成
api = tweepy.API(auth,wait_on_rate_limit=True)#wait_on_rate_limit=True。これを指定するとAPIの使用制限にひかかったときに待ちます。

search_results = api.search(q= "橋本ありな", count=100,lang="ja")

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    print(user_id)
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(user_id)  #ファヴォる
        print(user)
        print("をファボしました")
    except:
        print("もうすでにふぁぼかフォローしてますわ")
    print("##################")