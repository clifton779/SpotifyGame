import unittest
from unittest.mock import MagicMock, patch
from api import get_song_urls, get_song_titles
from app import app


class GetSongUrls(unittest.TestCase):
    def test_error_input(self):
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = get_song_urls(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
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
    def test_error_input(self):
        test_input = None
        expected_output = "Error: No Genre Chosen"
        actual_output = get_song_titles(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_regular_input(self):
        mock_response = MagicMock()
        mock_response.tracks.return_value = {
            "tracks": [{"name": "Response"}, {"name": "Response2"}]
        }
        with patch("api.authorization") as mock_spotify_create:
            mock_spotify_create.return_value = mock_response

            self.assertEqual(
                get_song_titles(["Test", "Test2"]), ["Response", "Response2"]
            )


class FlaskTest(unittest.TestCase):
    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # checks if user is loaded on to page
    @patch("flask_login.utils._get_user")
    def test_current_user(self, current_user):
        user = MagicMock()
        user.__repr__ = lambda self: "Mr Mocked"
        current_user.return_value = user
        client = app.test_client()
        response = client.get("/profilePage")
        data = response.data.decode("utf-8")


if __name__ == "__main__":
    unittest.main()
