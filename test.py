import unittest
from unittest import mock
from unittest.mock import MagicMock, patch
from api import getSongUrls, getSongTitles


class GetSongUrls(unittest.TestCase):
    def test_error_input(self):
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = getSongUrls(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
        mock_response = MagicMock()
        mock_response.tracks.return_value = {
            "tracks": [{"preview_url": "Response"}, {"preview_url": "Response2"}]
        }
        with patch("api.authorization") as mock_spotify_create:
            mock_spotify_create.return_value = mock_response

            self.assertEqual(getSongUrls(["Test", "Test2"]), ["Response", "Response2"])


class GetSongTitles(unittest.TestCase):
    def test_error_input(self):
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = getSongTitles(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
        mock_response = MagicMock()
        mock_response.tracks.return_value = {
            "tracks": [{"name": "Response"}, {"name": "Response2"}]
        }
        with patch("api.authorization") as mock_spotify_create:
            mock_spotify_create.return_value = mock_response

            self.assertEqual(
                getSongTitles(["Test", "Test2"]), ["Response", "Response2"]
            )


if __name__ == "__main__":
    unittest.main()
