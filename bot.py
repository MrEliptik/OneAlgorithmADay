import tweepy
import csv

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = 'X'
ACCESS_SECRET = 'X'
CONSUMER_KEY = 'X'
CONSUMER_SECRET = 'X'

class Twitter():

    def __init__(self):
        self.api = self.connect_to_twitter_OAuth()

    # Setup access to API
    def connect_to_twitter_OAuth(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)
        return api

    def tweet(self, msg):
        self.api.update_status(status = msg)

def main():
    # Create API object
    print('[INFO] Connecting to twitter..')
    bot = Twitter()
    print('[INFO] Connected!')

    # Get the last line used and increment
    with open('last_line.txt', 'r') as f:
        data = f.read().strip()
        line = int(data) + 1

    # Write back to file
    with open('last_line.txt', 'w') as f:
        f.write(str(line))

    # Open CSV and get the corresponding line
    with open('algorithms_shuffled.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i == line:
                tweet = "Today's algorithm: "
                for j, elem in enumerate(row):
                    if elem != '':
                        tweet += elem
                        elem.strip()
                        if j != 6:
                            tweet += ', '
                print(tweet)

    
    print('[INFO] Tweeting..')
    bot.tweet(tweet)
    print('[INFO] Finished tweeting!')
    

if __name__ == "__main__":
    main()