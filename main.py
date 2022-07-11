import tweepy
import pyyoutube
import ffmpeg
import random
import datetime

# Youtube API
api = pyyoutube.Api(api_key='AIzaSyDv6m8oF5fKe7BrRTkbulND8R-gJEX5LgY')
video = api.get_video_by_id(video_id='nZETPn1NoCM').items[0]
upload_date = video.snippet.publishedAt

# Date Handling
current_date = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
upload_date = datetime.datetime.strptime(upload_date, '%Y-%m-%dT%H:%M:%SZ')
time_since = str((current_date - upload_date).days)

# Media Creation
stream = ffmpeg.input('video.mp4', ss=random.randint(0,1200), t=10)
stream = ffmpeg.drawtext(stream, text=f'CC hasnt uploaded in {time_since} days.', x=35, y=40,
                        fontfile='font.ttf', fontsize=30, fontcolor='white')
stream = ffmpeg.output(stream, 'output.gif')
ffmpeg.run(stream, overwrite_output=True)


'''
consumer_key = "rkdJ8eQ9aAwlLlyKFof6PsrWv"

consumer_secret = "u7lcKeFiKjWBBW7JAeHDE1eNdogZGnCSykAL8dhse2EUmCkYiO"

access_token = "775898153245704192-Ggativa8GI8KL7XfXakxPnobvsWl0R3"

access_token_secret = "Wmsa2G2WWUiWzeKzKyD7MZ4pA7tRsDC23xSYktRNC5w4k"

auth = tweepy.OAuth1UserHandler(
consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    '''