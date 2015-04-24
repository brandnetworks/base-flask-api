import unittest
import json
from api import create_app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_root_health(self):
        response = self.test_client.get('/health/')
        data = json.loads(response.get_data().decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertIsInstance(data['db_connected'], bool)
        self.assertIsInstance(data['mem_total_percent_used'], float)
        self.assertIsInstance(data['mem_proc_percent_used'], float)
        self.assertIsInstance(data['num_api_processes'], int)

if __name__ == '__main__':
    unittest.main()
