from instagram_bot import InstagramBot

# Initiate bot
ig = InstagramBot()

# Likes a post given the post's url
# Returns username if return_user
# (return_user = False by default)
url = 'https://www.instagram.com/p/BnZBdTVluBA/'
username = ig.like(url, return_user = True)

# Like a user's first p posts given
# their username and the number of posts
# (p = 3 by default)
username = 'tobytrek'
ig.like_user(username, p=5)

# Like the first p posts of the first u users
# on from a hashtag page given the hashtag,
# number of users and number of posts
# (u = 5, p = 3 by default)
hashtag = 'torontoclx'
ig.like_hashtag(hashtag, u=3, p=5)

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
