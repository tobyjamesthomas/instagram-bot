from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep

INSTAGRAM_FRONTPAGE = "https://www.instagram.com"
INSTAGRAM_USERNAME = "USERNAME"
INSTAGRAM_PASSWORD = "PASSWORD"

"""
TODO:
    - double_click clicks on any tags underneath
    - double_click doesn't work on videos
    - only like users & posts if they haven't been liked before
    - implement max like cap
    - use better variable names for like_hashtag and like_user
"""

class InstagramBot():

    hashtags_liked = []
    users_liked = []
    posts_liked = []

    start_time = time() # Log start time

    def __init__(self):
        # Create headless option
        self.options = Options()
        self.options.set_headless()
        assert self.options.headless

        # Create browser and navigate to Instagram
        self.browser = webdriver.Chrome(chrome_options = self.options)
        self.browser.get(INSTAGRAM_FRONTPAGE)
        assert "Instagram" in self.browser.title

        # Login to Instagram
        self.login()

    def login(self):
        '''
        Login to Instagram with credentials above
        '''
        print(f"Logging into {INSTAGRAM_USERNAME}'s account...")
        self.browser.get(INSTAGRAM_FRONTPAGE + '/accounts/login/')
        sleep(1) # Second, wait for page to load

        # Enter credentials
        username = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        password = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        username.send_keys(INSTAGRAM_USERNAME)
        password.send_keys(INSTAGRAM_PASSWORD, Keys.RETURN)

        sleep(3) # Seconds, wait for page to load
        assert "Instagram" in self.browser.title

    def like_hashtag(self, hashtag, u=5, p=3):
        '''
        Like the first p posts of the first u users
        on from a hashtag page give the hashtag,
        number of users and number of posts
        '''

        # Return if hashtag has already been liked
        if hashtag in self.hashtags_liked:
            print(f"Skipping {hashtag}, already liked...")
            return

        print(f"Liking #{hashtag}, {u} users, {p} posts...")
        self.browser.get(INSTAGRAM_FRONTPAGE + '/explore/tags/' + hashtag)

        # Find the post urls of a hashtag, and remove
        # the ones already liked from previous hashtags
        posts = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, ".//a[contains(@href,'/p/')]")
            )
        )
        posts = list(map(lambda p: p.get_attribute('href').split('?')[0], posts))
        posts = list(set(posts) - set(self.posts_liked))

        # Like u posts and record u users
        usernames = []
        for post in posts[9:(9+u)]: # First u posts after Top Posts
            usernames.append(self.like(post, return_user=True))
            sleep(2) # Seconds

        # Like users from above
        # TODO: users' posts will overlap with the ones liked above
        for user in usernames:
            self.like_user(user, p)
            sleep(2) # Seconds

        # Add hashtag to hashtags_liked
        self.hashtags_liked.append(hashtag)

    def like_user(self, username, p=3):
        '''
        Like a user's first p posts
        given their username and the number of posts
        '''

        # Return if user has already been liked
        if username in self.users_liked:
            print(f"Skipping {username}, already liked...")
            return

        print(f"Liking {username}'s first {p} posts...")
        self.browser.get(INSTAGRAM_FRONTPAGE + '/' + username)
        sleep(1) # Second

        # Find urls to user's posts
        posts = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, ".//a[contains(@href,'/p/')]")
            )
        )
        posts = list(map(lambda p: p.get_attribute('href').split('?')[0], posts))

        # Like posts
        for post in posts[:p]:
            self.like(post)
            sleep(2) # Seconds

        # Add username to users_liked
        self.users_liked.append(username)

    def like(self, url, return_user=False):
        '''
        Likes a post given the post's url
        Returns username if return_user
        '''

        # Return if post has already been liked
        if url in self.posts_liked:
            print(f"Skipping {url}, already liked...")
            return

        print(f"Liking {url}...")
        self.browser.get(url)
        sleep(1) # Second

        # Find post and double click (like)
        # TODO: double_click doesn't work on videos
        # TODO: double_click clicks on any tags in middle
        post = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//article/div/div[contains(@role,'button')]")
            )
        )
        ActionChains(self.browser).double_click(post).perform()

        # Add post url to posts_liked, without ? query
        self.posts_liked.append(url)

        # Return username if return_user
        if return_user:
            return WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, ".//header//a[contains(@class,'notranslate')]")
                )
            ).get_attribute('title')

    def get_bio(self):
        '''
        Get account's bio
        '''
        print(f"Getting account bio...")
        self.browser.get(INSTAGRAM_FRONTPAGE + "/accounts/edit/")

        bio = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//textarea[contains(@id,'pepBio')]")
            )
        )

        return bio.get_attribute("value")

    def set_bio(self, new_bio):
        '''
        Change account bio to new_bio
        '''
        print(f"Updating bio to:\n'{new_bio}'")
        self.browser.get(INSTAGRAM_FRONTPAGE + "/accounts/edit/")

        bio = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//textarea[contains(@id,'pepBio')]")
            )
        )

        # Clear current bio and add new_bio
        bio.clear()
        self.send_keys(bio, new_bio)
        bio.send_keys(" ", Keys.BACKSPACE) # Activate change

        # Save profile
        submit = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//button[text()='Submit']")
            )
        )
        submit.click()

    def send_keys(self, elem, text):
        '''
        Send text to elem, workaround for emojis
        '''
        print("Injecting text to elem...")

        # JS script to add text to elem
        js_script = """
            var elem = arguments[0], text = arguments[1];
            elem.value += text;
            elem.dispatchEvent(new Event('change'));
            """

        self.browser.execute_script(js_script, elem, text)

    def close(self):
        '''
        Close browser
        '''
        print("Closing browser...")
        self.browser.close()

    def __str__(self):
        '''
        InstagramBot to string
        '''
        time_elapsed = round(time() - self.start_time)
        avg_like_time = time_elapsed / len(self.posts_liked)
        return f"InstagramBot Summary:\n" \
                f"Time elapsed: {time_elapsed} seconds\n" \
                f"Hashtags liked: {self.hashtags_liked}\n" \
                f"Users liked: {self.users_liked}\n" \
                f"Posts liked: {self.posts_liked}\n" \
                f"Liked {len(self.hashtags_liked)} hashtags in {time_elapsed} seconds\n" \
                f"Liked {len(self.users_liked)} users in {time_elapsed} seconds\n" \
                f"Liked {len(self.posts_liked)} posts in {time_elapsed} seconds\n" \
                f"Average like time: {avg_like_time}"
