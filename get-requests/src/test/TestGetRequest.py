from unittest import TestCase
from core.GetRequest import GetRequest
from core.ManageCsv import ManageCsv
from ddt import ddt, data, unpack


@ddt
class TestGetRequests(TestCase):
    manage_csv = ManageCsv()

    def setUp(self):
        self.get_request = GetRequest('https://jsonplaceholder.typicode.com')

    @data(*manage_csv.get_read_csv('../../files/input-file.csv'))
    @unpack
    def testGetRequests(self, exp_route, exp_status):
        actual_status_code = self.get_request.read_get(exp_route)
        self.assertEqual(actual_status_code, int(exp_status))
