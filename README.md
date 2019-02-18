# InstagramBot
Instagram bot that only likes ❤️ because fake comments and follow/unfollows are annoying 👎

## Installation

Install Selenium with pip3:
```bash
pip3 install selenium
```

Then, download the [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads). Next, clone this repository:
```bash
git clone https://github.com/tobyjamesthomas/instagram-bot.git
cd instagram-bot
```

### For weather

*Note: As of January 3, 2019, weather-api is now retired and needs to be replaced.*

[instagram_bot_weather.py](./instagram_bot_weather.py) uses Yahoo's weather API:
```bash
pip3 install weather-api
```

Lookup your city's WOEID [here](https://www.yahoo.com/news/weather/). (Change location to your city, and WOEID should be in URL)

## Usage

```python
from instagram_bot import InstagramBot

ig = InstagramBot()
```

### Like Post
Like a post given the post's url:
```python
url = 'https://www.instagram.com/p/Bjhav3XFUyd/'
ig.like(url)
```

### Like user
Like a user's three most recent posts given their username:
```python
username = 'tobytrek'
ig.like_user(username)
```

### Like hashtag
Like the five most recent posts of a given hashtag, then like each post's user (see above):
```python
hashtag = 'theofficememes'
ig.like_hashtag(hashtag)
```

### Update bio

```python
# Get your current bio
current_bio = ig.get_bio()

# Set your bio
new_bio = "Why waste time say lot word when few word do trick?"
ig.set_bio(new_bio)
```

Note: You can change the number of posts / users / hastags liked. See [instagram_bot_example.py](./instagram_bot_example.py) for full usage.

## Known Issues

- Yahoo's weather-api is currently retired as of January 3, 2019.

## Contribute!

Feel free to fork this project and add to it 😊
