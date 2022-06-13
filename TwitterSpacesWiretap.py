import requests
import json

if __name__ == "__main__":
    import argparse


class TwitterSpace:
    def __init__(self):
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        self.AUTHORIZATION = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        self.session = requests.session()
        self.x_guest_token = self.__get_guest_token()

    def __get_guest_token(self):
        headers = {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
        }
        response = self.session.post(
            "https://api.twitter.com/1.1/guest/activate.json", headers=headers
        ).json()
        return response["guest_token"]

    def __get_headers(self):
        return {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
            "Content-type": "application/json",
            "x-guest-token": self.x_guest_token,
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "ja",
        }

    def AudioSpaceById(self, url):
        id = url.split("?")[0].split("/")[-1]
        params = {
            "variables": json.dumps(
                {
                    "id": id,
                    "isMetatagsQuery": True,
                    "withSuperFollowsUserFields": True,
                    "withBirdwatchPivots": False,
                    "withDownvotePerspective": False,
                    "withReactionsMetadata": False,
                    "withReactionsPerspective": False,
                    "withSuperFollowsTweetFields": True,
                    "withReplays": True,
                    "withScheduledSpaces": True,
                }
            )
        }
        response = self.session.post(
            "https://twitter.com/i/api/graphql/Uv5R_-Chxbn1FEkyUkSW2w/AudioSpaceById",
            headers=self.__get_headers(),
            params=params,
        ).json()
        self.content = response
        return self

    def live_video_stream(self, media_key):
        params = {
            "client": "web",
            "use_syndication_guest_id": False,
            "cookie_set_host": "twitter.com",
        }
        response = self.session.get(
            "https://twitter.com/i/api/1.1/live_video_stream/status/" + media_key,
            headers=self.__get_headers(),
            params=params,
        ).json()
        self.content = response
        return self


if __name__ == "__main__":
    space = TwitterSpace()

    argpar = argparse.ArgumentParser(
        prog="TwitterSpacesWiretap",
        usage="https://github.com/fa0311/TwitterSpacesWiretap",
        description="Twitter Spaces Wiretap Tool",
    )
    argpar.add_argument("--url", default=False)
    arg = argpar.parse_args()
    if not arg.url:
        print(
            "Please enter the URL of the spaces:(e.g. https://twitter.com/i/spaces/xxxxxxxxxxx)"
        )
        arg.url = input()
    media_key = space.AudioSpaceById(arg.url).content["data"]["audioSpace"]["metadata"][
        "media_key"
    ]
    print(space.live_video_stream(media_key).content["source"]["location"])
