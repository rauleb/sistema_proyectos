from django.test import TestCase

# Create your tests here.

class LoginViewTests (TestCase):
    def test_index(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)