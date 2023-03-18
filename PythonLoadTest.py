import requests
import unittest

class SecurityTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://example.com"  # Replace with the URL of the web application to test

    def test_no_sql_injection(self):
        # Test for SQL injection vulnerabilities
        payload = {"username": "admin'; DROP TABLE users; --", "password": "password"}
        response = requests.post(self.url, data=payload)
        self.assertNotEqual(response.status_code, 500)  # Check that the server did not encounter an internal error

    def test_no_xss_vulnerability(self):
        # Test for cross-site scripting (XSS) vulnerabilities
        payload = "<script>alert('XSS')</script>"
        response = requests.post(self.url, data=payload)
        self.assertNotIn(payload, response.text)  # Check that the payload did not appear in the response

if __name__ == "__main__":
    unittest.main()
