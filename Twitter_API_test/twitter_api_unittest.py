import unittest
import twitter_api

class TestRequest(unittest.TestCase):

    # Test sending a search request
    def test_request(self):
        # Send a request
        request_status_code = twitter_api.send_request({'q':'codinginflow'})
        self.assertEqual(request_status_code, 200)
    
    # Test getting, setting and deleting rules
    def test_rules(self):
        # Show current rules
        current_rules = twitter_api.get_rules()
        # Delete current rules
        delete_response = twitter_api.delete_rules(current_rules)
        # Add some new rules, by now there should be 0 rules
        rules = [
            {"value": "NBA has:images has:media"},
            {"value": "from:codinginflow has:links"},
            {"value": "meme has:images"}
        ]
        new_rules = twitter_api.set_rules(rules)
        # By now there should be 3 rules
        rule_number = new_rules["meta"]["summary"]["valid"]
        self.assertEqual(rule_number, 3)


if __name__ == '__main__':
    unittest.main()