# TwitterSpacesWiretap

ログイン: [TwitterFrontendFlow](https://github.com/fa0311/TwitterFrontendFlow) /
取得: [TweetURLtoData](https://github.com/fa0311/TweetURLtoData) /
スペース: [TwitterSpacesWiretap](https://github.com/fa0311/TwitterSpacesWiretap)

TwitterのSpacesをSpacesに参加せずに聞くことが出来ます<br>

## Using

```shell
python TwitterSpacesWiretap.py --url <URL>
```

返されるURLをffplayやffmpegなどに投げれば聞いたり保存したりも出来ます
```shell
ffplay <URL>
ffmpeg -i <URL> output.mp3
```
