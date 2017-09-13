import json
import requests


"""
Returns tuple with stars,forks and watchers. 
"""

def get_details(repo_url):
	try:
		repo_details = requests.get(repo_url)
		repo_details = repo_details.json()
		return repo_details["stargazers_count"],repo_details["forks"],repo_details["subscribers_count"]
	except Exception as e:
		return -1,-1,-1