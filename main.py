import tweepy
import pyyoutube
import ffmpeg
import random
import datetime
import keys


def get_date():
    # Get the current date of youtube video and returns amount of days since upload.
    api = pyyoutube.Api(api_key=keys.youtube_api)
    video = api.get_video_by_id(video_id='nZETPn1NoCM').items[0]
    upload_date = video.snippet.publishedAt
    current_date = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
    upload_date = datetime.datetime.strptime(upload_date, '%Y-%m-%dT%H:%M:%SZ')
    return str((current_date - upload_date).days)


def post_tweet():
    # Creates a tweet with the video and uploads it to twitter.
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    upload_result = api.media_upload('output.gif')
    api.update_status(status="", media_ids=[upload_result.media_id_string])
        

def create_video():
    # Creates a video and edits date ontop of it.
    stream = ffmpeg.input('video.mp4', ss=random.randint(0,1200), t=7)
    stream = ffmpeg.drawtext(stream, text=f'CC hasnt uploaded in {get_date()} days.', x=35, y=40,
                           fontfile='font.ttf', fontsize=30, fontcolor='white')

    stream = ffmpeg.output(stream, 'output.gif')
    ffmpeg.run(stream, overwrite_output=True)

print('waiting...')
while True:
    if datetime.datetime.now().strftime('%H:%M:%S') == '00:00:00':
        create_video()
        post_tweet()
        print('Tweeted!')



