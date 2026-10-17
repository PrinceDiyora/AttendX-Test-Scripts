import unittest


def validate_login(username, password):
    """Demonstration login validation."""
    if not username or not password:
        return "Username and password are required"
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid username or password"


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            validate_login("admin", "admin123"),
            "Login successful"
        )

    def test_wrong_password(self):
        self.assertEqual(
            validate_login("admin", "wrong"),
            "Invalid username or password"
        )

    def test_empty_fields(self):
        self.assertEqual(
            validate_login("", ""),
            "Username and password are required"
        )

    def test_empty_username(self):
        self.assertEqual(
            validate_login("", "admin123"),
            "Username and password are required"
        )

if __name__ == "__main__":
    unittest.main()
