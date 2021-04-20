import requests 

# Make an API call and store the responce 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store API responce in a variable 
# convert from json format to python dictionary format
responce_dict = r.json()
print(f"Total repositories: {responce_dict['total_count']}")

# Explore information about the repositories 
repo_dicts = responce_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]

print("\nSelected information about the first repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")

print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Process results
# when working with more complex API's its important to check 'incomplete_results'
# note that incomplte_results = False means the request was sucessful since (its not incomplete)
incomplete_results = responce_dict['incomplete_results']
print(responce_dict.keys())

# checking to see if incomplete_results is true or false?
# false means were the request was sucessful 
# Note that sometimes if incomplte_results is true doesnt always mean the infor is incomplete
# Git API documentation states that it could be reaching a timeout or the request has already been 
# made before 
print(incomplete_results)
