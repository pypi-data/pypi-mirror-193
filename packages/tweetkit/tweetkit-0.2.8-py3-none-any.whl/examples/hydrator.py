import json
import os

from tqdm import auto as tqdm

from tweetkit.auth import BearerTokenAuth
from tweetkit.client import TwitterClient

with open('../secrets/bearer_token.txt', 'r', encoding='utf-8') as fp:
    auth = BearerTokenAuth(fp.read().strip())
    assert len(auth.bearer_token) > 0, 'Unable to load the bearer token.'

client = TwitterClient(auth=auth)

input_path = os.path.expanduser('~/Downloads/SOLID/task_a_distant.tsv')
output_path = os.path.expanduser('~/Downloads/SOLID/task_a_distant.jsonl')

tweet_ids = set()

with open(input_path, 'r', encoding='utf-8') as fp:
    for i, line in enumerate(fp.readlines()):
        if i == 0:
            continue
        fields = line.strip().split('\t')
        if len(fields) > 0:
            tweet_id = str(int(fields[0]))
            tweet_ids.add(tweet_id)

existing_tweet_ids = set()

with open(output_path, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()
    for line in lines:
        tweet = json.loads(line)
        if isinstance(tweet, dict):
            tweet_id = tweet['data']['id']
            existing_tweet_ids.add(tweet_id)

tweet_ids = [tweet_id for tweet_id in tweet_ids if tweet_id not in existing_tweet_ids]


def write_docs(path, docs):
    with open(path, 'a', encoding='utf-8') as fp:
        fp.write('\n'.join(map(json.dumps, docs)) + '\n')


tweets = []

for i in tqdm.trange(0, len(tweet_ids), 100):
    batch = tweet_ids[i:i + 100]
    reply = client.tweets.find_tweets_by_id(batch)
    tweets += reply.content
    if len(tweets) >= 1000:
        write_docs(output_path, tweets)
        tweets = []

if len(tweets) > 0:
    write_docs(output_path, tweets)
