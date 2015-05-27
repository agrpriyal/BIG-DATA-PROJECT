#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ckey ='sIvN7ql6lymHxRbL0GKfCpvzR'
csecret ='a6iqCtd3CjAK4jnJwnhQxI5zs1fYqe3qT5SORYv5AVmwM9Hni0'
atoken ='3168483049-SlCgGi9FZGRRv7ZjttcD26GH31OWYfVW2xUVBw1' 
asecret ='w4F0PnKmFvuPYIOnGcBRi2EKnRO9VIZvNlXIcamBROH26'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status

if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)

#stream.filter(track=['php','python','cobol','javascript','ruby','java'])
stream.filter(track=['python','javascript','ruby'])

  