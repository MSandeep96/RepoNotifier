from details import get_details
from datetime import datetime as dt
from threading import Timer
from twilio.rest import Client
#create myTwilio file with acc_id and auth_tokn set
from myTwilio import account_id,auth_token,mob_no,from_no

user_name = "msandeep96"
repo_name = "soundkeys"
repo_url = f"https://api.github.com/repos/{user_name}/{repo_name}"

client = Client(account_id,auth_token)

stars,forks,watchers = get_details(repo_url)
msg_body = "Present status:\n" + "Star count: {}\n".format(stars) + "Forks count: {}\n".format(forks) + "Watchers count: {}".format(watchers)

client.messages.create(
	to=mob_no,
	from_=from_no,
	body=msg_body
	)