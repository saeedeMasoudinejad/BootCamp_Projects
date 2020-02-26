import redis
import requests
import json
import time

r = redis.Redis()


def fetch_github_profile(username):
    data = requests.get("https://api.github.com/users/" + username)
    r.setex(username, 10, str(data.json()))
    return json.dumps({
        "cached": False,
        "profile": data.json()
    })


def get_github_profile(username):
    result = r.get(username)
    if result:
        return json.dumps({
            "cached": True,
            "profile": str(result)
        })

    else:
        return fetch_github_profile(username)


print(get_github_profile('saeedeMasoudinejad'))

