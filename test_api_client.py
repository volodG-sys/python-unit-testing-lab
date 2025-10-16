import unittest
from unittest.mock import patch
from api_client import get_weather

class TestAPIClient(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_get_weather_ok(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"temp": 15}
        result = get_weather("Kyiv")
        self.assertIn("temp", result)

    @patch('api_client.requests.get')
    def test_get_weather_fail(self, mock_get):
        mock_get.return_value.status_code = 500
        with self.assertRaises(ConnectionError):
            get_weather("Kyiv")
