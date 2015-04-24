import unittest
from api import create_app
from model import Health


# class TestVersionHistory(unittest.TestCase):
#
#     def setUp(self):
#         # self.vh = VersionHistory()
#         self.app = create_app()
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_db_connection(self):
#         self.assertTrue(VersionHistory.is_connected())


class TestHealth(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.health = Health()

    def tearDown(self):
        self.health = None

    def test_data_collection(self):
        data = self.health.get_data()
        self.assertIsInstance(data['db_connected'], bool)
        self.assertIsInstance(data['mem_total_percent_used'], float)
        self.assertIsInstance(data['mem_proc_percent_used'], float)
        self.assertIsInstance(data['num_api_processes'], int)
