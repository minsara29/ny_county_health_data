from unittest import TestCase
from unittest.mock import patch
from health_data import CovidHealthAPI

URL = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD'

class TestHealthDataAPI(TestCase):
    def setUp(self):
        self.page = CovidHealthAPI(URL)

    def test_make_request(self):
        with patch("requests.get") as mocked_get:
            response = self.page.get_data()
            print(response)
            mocked_get.assert_called()

    # def test_content_returned(self):
    #     fake_content = "Hello"
    #
    #     class FakeResponse:
    #         def __init__(self):
    #             self.content = fake_content
    #
    #     with patch("requests.get", return_value=FakeResponse()) as mocked_get:
    #         result = self.page.get_data()
    #         print(result)
    #         # self.assertEqual((result, fake_content))


