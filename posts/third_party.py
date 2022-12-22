import urllib.request as request
import ssl, json

class PostApi:
    @staticmethod
    def get_posts(*args, **kwargs):
        posts_entities = []

        context = ssl._create_unverified_context()
        res = request.urlopen('https://dummyjson.com/posts', context=context)

        if res.status == 200:
            decoded = json.loads(res.read().decode())
            posts_entities = decoded['posts']

        return posts_entities