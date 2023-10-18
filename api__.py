"""
api test
"""
import requests
def github_api(user_id):
    """
    Methods to fetch number of repo and commits
    """
    r = requests
    r = r.get('https://api.github.com/users/'+user_id+'/repos', timeout=5)
    if r.status_code==200:
        repo_cnt=len(r.json())
        repo_list = []
        for i in range(0,repo_cnt):
            repo_list.append(r.json()[i]['name'])
        if repo_cnt>1:
            print('There are '+str(repo_cnt)+' Repos\n')
        else:
            print('There is one Repo\n')
        for rn in repo_list:
            rc=requests.get('https://api.github.com/repos/'+user_id+'/'+rn+'/commits', timeout=5)
            commit_len=len(rc.json())
            print('Repo : ' + rn + '\nRepo URL: https://api.github.com/users/'+rn+'/repos\n')
            print('Number of Commits: ' +str(commit_len)+'\n')
            print('Commit URL: '+'https://api.github.com/repos/'+user_id+'/'+rn+'/commits\n')
    else:
        print("try again later")

github_api("Sanjan81")
