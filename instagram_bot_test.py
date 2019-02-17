from instagram_bot import InstagramBot

# Initiate test
ig = InstagramBot()

# Test like
#  url = 'https://www.instagram.com/p/BnZBdTVluBA/'
#  ig.like(url)

# Test like user
#  username = 'tobytrek'
#  ig.like_user(username)

# Test like hashtag
#  hashtag = 'torontoclx'
#  ig.like_hashtag(hashtag)

# Test on multiple hashtags
hashtags = ['bokeh_kings', 'moodygang', 'eclectic_shotz', 'falltrapz', 'bokeh_shotz', 'moodygrams', 'depthobsessed', 'bokehkillers', 'torontoclx', 'filmtronic', 'depthofearth', 'heatercentral', 'moodyfilm', 'houseoftones', 'visualambassadors', 'under3kyo', 'shotz_fired', 'yngkillers', 'dscvr_mood', 'omd_5k', 'celebratoryactionz', 'visualmood', 'vibetones', 'creativetribez', 'expofilm3k', 'trappingtones', 'agameof10k', 'vnrchy', 'igtones5k']

for ht in hashtags[:20]:
    ig.like_hashtag(ht)

# Print summary
print(f"\n{ig}")

# End test
ig.close()
