import os

import praw


class RedditClient:
    ENV_VAR = {
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET"),
        "password": os.environ.get("PASSWORD"),
        "user_agent": os.environ.get("USER_AGENT"),
        "username": os.environ.get("USERNAME")
    }

    def __init__(self):
        reddit = praw.Reddit(**self.ENV_VAR)
        print(reddit.user.me())