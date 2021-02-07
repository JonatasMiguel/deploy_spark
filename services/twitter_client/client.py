from tweepy import OAuthHandler, Stream, StreamListener
import json
import sys
import socket
import os

ACCESS_TOKEN = '911753131087851520-uJbfaAOeIboiKdlBZ8A9yQVqOJWshcN'
ACCESS_SECRET = '8xPzdiw6ECuWnTGMcdA4BOlATS2AkjPUNBQhLW7U7yRm8'
CONSUMER_KEY = '2hnglcuJB8L5NHvBeeiwDWx4w'
CONSUMER_SECRET = '2KC4Y2PwjEF5WJW6meNesBei74PcdV71ugvmkuvZqMn6brfAnM'
HEADERS = {
    "Content-type": "application/json",
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMjPMAEAAAAA%2B4%2B3RgyTxBq6lQEY3qClJP%2FJczo%3D35hA06N9kJl7zRP8eYL9MZmMrEK3JzYozs2MIGXZPECbLMo4RG"
}

TWITTER_IP = "TWITTER_IP"
TWITTER_PORT = "TWITTER_PORT"

class StdOutListener(StreamListener):
    def __init__(self, api=None, *, ip, port):
        super().__init__(api=api)

        TCP_IP = ip
        TCP_PORT = port
        conn = None
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        print("Aguardando uma conexão TCP...")
        self.conn, self.addr = s.accept()

        print("Conectado... Começando a coletar tweets...")

    def on_data(self, data):
        try:
            full_tweet = json.loads(data)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print("------------------------------------------")
            b = bytes(tweet_text + '\n', 'utf-8')
            self.conn.send(b)
        except Exception as e:
            print(f"Error: {e}")
        return True

    def on_error(self, status):
        print(status)
        return False


if __name__ == "__main__":
    track = None
    lang = None

    args = sys.argv

    try:
        for i in range(1, len(args)):
            if args[i] == '--help':
                print("Twitter Client Tool")
                print("------------------------")
                print("Usage <python client.py [OPTIONS] [ARGUMENTS]>")
                print("------------------------")
                print("[OPTIONS]")
                print("--help : See the client usage tutorial")
                print(
                    "--track : Set the track for tweets extraction. The tracks need to be separeted by comma.")
                print("--lang : Set the language in twitter extraction api.\n")
                sys.exit(1)
            if args[i] == '--track':
                track = args[i+1]
                i += 1
            if args[i] == '--lang':
                lang = args[i+1]
                i += 1
    except IndexError as e:
        print("Wrong usage. Execute with --help to see more.")
        sys.exit(1)
        
    track = track.split(',') if track else ['bbb', 'bbb21', "Big brother", "reality"]
    lang = [lang if lang else "pt"]

    listener = StdOutListener(ip=os.environ[TWITTER_IP], port=os.environ[TWITTER_PORT])
    auth = OAuthHandler(consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=track, languages=lang)
