# pylint: disable=missing-module-docstring
import unittest
from unittest.mock import MagicMock, patch
from api import get_song_urls, get_song_titles
from app import app


class GetSongUrls(unittest.TestCase):
    """Get song urls unnit tests"""

    def test_error_input(self):
        """Test for default"""
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = get_song_urls(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
        """Tests that function accuratley gets url"""
        mock_response = MagicMock()
        mock_response.tracks.return_value = {
            "tracks": [{"preview_url": "Response"}, {"preview_url": "Response2"}]
        }
        with patch("api.authorization") as mock_spotify_create:
            mock_spotify_create.return_value = mock_response

            self.assertEqual(
                get_song_urls(["Test", "Test2"]), ["Response", "Response2"]
            )


class GetSongTitles(unittest.TestCase):
    """tests get song titles funtction"""

    def test_error_input(self):
        """Tests default"""
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = get_song_titles(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
        """Tests that function accuratley gets song name"""
        mock_response = MagicMock()
        mock_response.tracks.return_value = {
            "tracks": [{"name": "Response"}, {"name": "Response2"}]
        }
        with patch("api.authorization") as mock_spotify_create:
            mock_spotify_create.return_value = mock_response

            self.assertEqual(
                get_song_titles(["Test", "Test2"]), ["Response", "Response2"]
            )


if __name__ == "__main__":
    unittest.main()
