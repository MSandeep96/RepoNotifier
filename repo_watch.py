from details import get_details

class RepoWatch:
	repo_url = ""
	stars = -1
	forks = -1
	watchers = -1

	def __init__(self,repo_url):
		self.repo_url = repo_url
		stars,forks,watchers = get_details(repo_url)

	def checkUpdates():
		message = ""
		nstars,nforks,nwatchers = get_details(repo_url)
		if (nstars==-1):
			return "Invalid"		#incase of error
		if(nstars==stars and nforks==forks and nwatchers==watchers):
			return "Invalid"
		if(nstars!=stars):
			message += f"Stars updated by {nstars-stars}\n"
		if(nforks!=forks):
			message += f"Forks updated by {nforks-forks}\n"
		if(nwatchers!=watcher):
			message += f"Watchers updated by {nwatchers-watchers}\n"
		stars = nstars
		forks = nforks
		watchers = nwatchers
		return message