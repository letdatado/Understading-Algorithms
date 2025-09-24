# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

import unittest
from data_loader import try_hash, verify_y_values


class TestDataLoader(unittest.TestCase):
    def test_try_hash(self):
        # Tests whether the SHA256 hash function returns the correct output
        # ... for a known input string.
        self.assertEqual(
            try_hash("test"),
            "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        )

    def test_verify_y_values(self):
        # Tests whether correctly validates the provided dataset and does 
        # ... not raise an error when the data and hash are correct
        test_values = [20, 93, 72, 35, 54, 95, 25, 37, 29, 72,
                       65, 66, 49, 43, 35, 61, 97, 66, 64, 22,
                       83, 69, 19, 21, 69, 40, 35, 81, 15, 41,
                       74, 12, 3, 65, 31, 12, 48, 68, 41, 40,
                       99, 13, 70, 30, 20, 35, 84, 96, 1, 93,
                       61, 83, 24, 27, 93, 86, 96, 43, 10, 51,
                       27, 87, 40, 35, 83, 44, 15, 89, 71, 79,
                       25, 84, 43, 49, 66, 0, 88, 80, 4, 3,
                       74, 10, 41, 45, 75, 34, 41, 44, 50, 99,
                       41, 37, 26, 6, 94, 94, 76, 48, 32, 42]

        test_string = ''.join(str(v) for v in test_values)
        test_hash = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"
        
        # Run validation and ensure no assertion is raised
        try:
            verify_y_values(test_string, test_hash, test_values)
        except AssertionError:
            self.fail("verify_y_values() should not raise an AssertionError")
