# -------------------------------------------------------------
# ------------- INSTAGRAM FOLLOWER BOT ------------------------
# -------------------------------------------------------------
from insta_follower import InstaFollower

INSTAGRAM_ACCOUNT_TO_FOLLOW = "kevinhart4real"

insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers(INSTAGRAM_ACCOUNT_TO_FOLLOW)
insta_follower.follow()
insta_follower.close_follower_window()


