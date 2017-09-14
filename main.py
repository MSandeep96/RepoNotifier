from datetime import datetime as dt
from threading import Timer
from twilio.rest import Client
from repo_watch import RepoWatch
from datetime import datetime
from threading import Timer
#create myTwilio file with these details set
from myTwilio import account_id,auth_token,mob_no,from_no

user_name = "msandeep96"
repo_name = "soundkeys"
repo_url = f"https://api.github.com/repos/{user_name}/{repo_name}"

client = Client(account_id,auth_token)

repo_watcher = RepoWatch(repo_url)

def setTrigger():
	now = datetime.today()
	tom = now.replace(day=now.day+1,hour=16,minute=0,second=0,microsecond=0)

	time_diff = tom - now
	time_diff_secs = time_diff.seconds + 1

	trigger = Timer(time_diff_secs,update)
	trigger.start()


def update():
	msg = repo_watcher.checkUpdates()
	if(msg != "Invalid"):
		client.messages.create(
			to=mob_no,
			from_=from_no,
			body=msg
		)
	setTrigger()

setTrigger()