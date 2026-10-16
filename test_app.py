
import unittest
from app import get_response


class TestApplication(unittest.TestCase):

    def test_message(self):
        data = get_response()
        self.assertEqual(
            data["message"],
            "Hello CI/CD Pipeline 2!"
        )

    def test_version(self):
        data = get_response()
        self.assertEqual(
            data["version"],
            "2.0.0"
        )

    def test_status(self):
        data = get_response()
        self.assertEqual(
            data["status"],
            "running"
        )


if __name__ == "__main__":
    unittest.main()
