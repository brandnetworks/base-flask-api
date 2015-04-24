import unittest
import json
from api import create_app


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.test_client.get('/')
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(data['status'], 'ok')

    def test_404(self):
        response = self.test_client.get('/dne')
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(data['error'], 'not found')

if __name__ == '__main__':
    unittest.main()
