from tweepy import OAuthHandler, Stream, StreamListener
import json
import sys
import socket
import os
import logging as log

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

        log.info("Aguardando uma conexão TCP...")
        self.conn, self.addr = s.accept()

        log.info("Conectado... Começando a coletar tweets...")

    def on_data(self, data):
        try:
            full_tweet = json.loads(data)
            tweet_text = full_tweet['text']
            log.info("Tweet Text: " + tweet_text)
            log.info("------------------------------------------")
            b = bytes(tweet_text + '\n', 'utf-8')
            self.conn.send(b)
        except Exception as e:
            log.info(f"Error: {e}")
        return True

    def on_error(self, status):
        log.info(status)
        return False


if __name__ == "__main__":
    track = None
    lang = None

    args = sys.argv

    try:
        for i in range(1, len(args)):
            if args[i] == '--help':
                log.info("Twitter Client Tool")
                log.info("------------------------")
                log.info("Usage <python client.py [OPTIONS] [ARGUMENTS]>")
                log.info("------------------------")
                log.info("[OPTIONS]")
                log.info("--help : See the client usage tutorial")
                log.info(
                    "--track : Set the track for tweets extraction. The tracks need to be separeted by comma.")
                log.info("--lang : Set the language in twitter extraction api.\n")
                sys.exit(1)
            if args[i] == '--track':
                track = args[i+1]
                i += 1
            if args[i] == '--lang':
                lang = args[i+1]
                i += 1
    except IndexError as e:
        log.info("Wrong usage. Execute with --help to see more.")
        sys.exit(1)
        
    track = track.split(',') if track else ['bbb', 'bbb21', "Big brother", "reality"]
    lang = [lang if lang else "pt"]

    listener = StdOutListener(ip=os.environ[TWITTER_IP], port=int(os.environ[TWITTER_PORT]))
    auth = OAuthHandler(consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=track, languages=lang)
