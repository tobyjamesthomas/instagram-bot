from instagram_bot import InstagramBot

# Initiate bot
ig = InstagramBot()

# Like an image with a given url
# Returns the image's username
# if return_user = True (default False)
url = 'https://www.instagram.com/p/BnZBdTVluBA/'
username = ig.like(url, return_user = True)

# Likes a user's first p posts
# (p = 3 by default)
username = 'tobytrek'
ig.like_user(username, p = 5)

# Likes the u most recent posts with a given hashtag
# Then proceed to like the first u users' p posts
# (u = 5, p = 3 by default)
hashtag = 'torontoclx'
ig.like_hashtag(hashtag, u = 3, p = 3)

# Example usage over list of hashtags:
hashtags = ['bokeh_kings', 'moodygang', 'eclectic_shotz',
        'falltrapz', 'bokeh_shotz', 'moodygrams',
        'depthobsessed', 'bokehkillers', 'torontoclx',
        'filmtronic', 'depthofearth', 'heatercentral',
        'moodyfilm', 'houseoftones', 'visualambassadors',
        'under3kyo', 'shotz_fired', 'yngkillers',
        'dscvr_mood', 'omd_5k', 'celebratoryactionz',
        'visualmood', 'vibetones', 'creativetribez',
        'expofilm3k', 'trappingtones', 'agameof10k',
        'vnrchy', 'igtones5k', 'whatarethesehashtagseven']

for ht in hashtags[:20]:
    ig.like_hashtag(ht)

# Print summary at the end!
print(f"\n{ig}")

# Exit test
ig.close()
