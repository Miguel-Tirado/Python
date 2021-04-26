import unittest
import test_python_repos as pr 

class PythonReposTestCase(unittest.TestCase):
    """Test for test_python_repos"""

    def setUp(self):
        """Call all the functions here, and test elements seperatlty"""
        self.r = pr.get_responce()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = pr.get_project_data(self.repo_dicts)
    
    def test_get_responce(self):
        """Test that we get a valid response"""
        self.assertEqual(self.r.status_code, 200)
    
    def test_repo_dicts(self):
        """Test that we're getting the data we think we are."""
        # note that response_dicts has a total of 30 items by when the request was made 
        self.assertEqual(len(self.repo_dicts),30)

        required_keys = ['name','owner','stargazers_count','html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()