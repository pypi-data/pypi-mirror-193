import json

docs = []

with open('/Users/Yasas/Downloads/tweets-hurricane-ian-sample-3k.jsonl', 'r', encoding='utf-8') as fp:
    for line in fp.readlines():
        tweet = json.loads(line)
        video_urls = []
        for media in tweet['meta']['attachments']['media']:
            if media['type'] == 'video':
                url = None
                for variant in media['variants']:
                    if variant['content_type'] == 'video/mp4':
                        url = variant['url']
                if url is not None:
                    video_urls.append(url)
        docs.append({
            'id': tweet['id'],
            'text': tweet['text'],
            'lang': tweet['meta']['lang'],
            'videos': video_urls
        })

with open('docs.json', 'w', encoding='utf-8') as fp:
    json.dump(docs, fp)
