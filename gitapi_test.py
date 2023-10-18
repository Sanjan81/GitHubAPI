"""
unit testcases for github api
"""
import unittest
import requests
#from api import github_api


class GitapiTests(unittest.TestCase):
    """
    testcases for api
    """

    def test_api(self):
        """
        testcases for the url response 
        """
        user_id="Sanjan81"
        rp = requests.get('https://api.github.com/users/'+user_id, timeout=5)
        self.assertEqual(rp.status_code,200)
        print("Test 1 Response Code: ",rp.status_code)

        repo = rp.json()
        #print(rp.json())
        self.assertEqual(repo["login"],user_id)
        print("test 2 Username: ",repo["login"])
    def test_repo(self):
        """
        testcases 
        """
        user_id = "Sanjan81"
        rp = requests.get('https://api.github.com/users/'+user_id, timeout=5)
        self.assertEqual(rp.status_code,200)


if __name__ == '__main__':
    #user_id = "Sanjan81"
    unittest.main()
