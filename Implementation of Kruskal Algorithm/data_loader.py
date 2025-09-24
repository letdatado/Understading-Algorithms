# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Necessary Imports
import hashlib
from typing import List


# ------------ 1. Checking Validity of Data ... ------------

# Given y_values:
Y_VALUES = [20, 93, 72, 35, 54, 95, 25, 37, 29, 72,
            65, 66, 49, 43, 35, 61, 97, 66, 64, 22,
            83, 69, 19, 21, 69, 40, 35, 81, 15, 41,
            74, 12, 3, 65, 31, 12, 48, 68, 41, 40,
            99, 13, 70, 30, 20, 35, 84, 96, 1, 93,
            61, 83, 24, 27, 93, 86, 96, 43, 10, 51,
            27, 87, 40, 35, 83, 44, 15, 89, 71, 79,
            25, 84, 43, 49, 66, 0, 88, 80, 4, 3,
            74, 10, 41, 45, 75, 34, 41, 44, 50, 99,
            41, 37, 26, 6, 94, 94, 76, 48, 32, 42]


# Given string and hash
GIVEN_STRING = '20937235549525372972656649433561976664228369192169403581154174123653112486841409913703020358496193618324279386964310512787403583441589717925844349660888043741041457534414450994137266949476483242'
GIVEN_HASH = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"


def try_hash(word: str) -> str:
    # The hex digest from the input string
    return hashlib.sha256(word.encode()).hexdigest() 


def verify_y_values(given_string: str = GIVEN_STRING, 
                    given_hash: str = GIVEN_HASH, 
                    y_values: List = Y_VALUES):
    
    # Recreate the string
    string_parts = []
    for value in y_values:
        string_parts.append(str(value).strip())
    obtained_string = ''.join(string_parts)
    
    # Compare the results with existing hash
    assert given_string == obtained_string, "Mismatch in stringified values"
    assert try_hash(given_string) == given_hash, "Hash check failed"
    print("Data and hash are confirmed.")
