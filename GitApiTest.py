import unittest
import requests
from api import GitHubAPI


class GitApi_Tests(unittest.TestCase):
    
    def test_api(self):
        varInputUserID="Sanjan81"
        rp = requests.get('https://api.github.com/users/'+varInputUserID)
        self.assertEqual(rp.status_code,200)
        print("Test 1 Response Code: ",rp.status_code)
    
        repo = rp.json()
        #print(rp.json())
        self.assertEqual(repo["login"],varInputUserID)
        print("test 2 Username: ",repo["login"])
    def test_repo(self):
        varInputUserID="Sanjan81"
        rp = requests.get('https://api.github.com/users/Sanjan81')
    
  
if __name__ == '__main__':
    #varInputUserID = "Sanjan81"
    unittest.main()