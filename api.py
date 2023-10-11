def GitHubAPI(varInputUserID):
    import requests
    varInputUserID = "Sanjan81"
    r = requests.get('https://api.github.com/users/'+varInputUserID+'/repos', auth=('user', 'pass'))
    if(r.status_code==200):
        RepoCnt=len(r.json())
        RepoList = []
        for i in range(0,RepoCnt):
            RepoList.append(r.json()[i]['name'])
        if(RepoCnt>1):
            print('There are '+str(RepoCnt)+' Repos\n')
        else:
            print('There is one Repo\n')
        for Rn in RepoList:
            rc=requests.get('https://api.github.com/repos/'+varInputUserID+'/'+Rn+'/commits', auth=('user', 'pass'))
            Commitlen=len(rc.json())
            print('Repo : ' + Rn + '\nRepo URL: https://api.github.com/users/'+Rn+'/repos'+ '\nNumber of Commits: ' +str(Commitlen)+'\nCommit URL: '+'https://api.github.com/repos/'+varInputUserID+'/'+Rn+'/commits\n')
    else:
        print("You made a boo-boo try later")

GitHubAPI("Sanjan81")