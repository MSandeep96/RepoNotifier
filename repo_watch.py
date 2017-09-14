from details import get_details

class RepoWatch:

	def __init__(self,repo_url):
		self.repo_url = repo_url
		self.stars,self.forks,self.watchers = get_details(repo_url)

	def checkUpdates(self):
		message = ""
		nstars,nforks,nwatchers = get_details(self.repo_url)
		if (nstars==-1):
			return "Invalid"		#incase of error
		if(nstars==self.stars and nforks==self.forks and nwatchers==self.watchers):
			return "Invalid"
		if(nstars!=self.stars):
			message += f"Stars updated by {nstars-self.stars}\n"
		if(nforks!=self.forks):
			message += f"Forks updated by {nforks-self.forks}\n"
		if(nwatchers!=self.watchers):
			message += f"Watchers updated by {nwatchers-self.watchers}\n"
		self.stars = nstars
		self.forks = nforks
		self.watchers = nwatchers
		return message