# Thư viện unittest - test function
import unittest 
import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
      return name
    return "{} {}".format(result[2], result[1])

# assertEqual(a, b)         -> a == b
# assertNotEqual(a, b)      -> a != b

# assertTrue(x)             -> bool(x) is True
# assertFalse(x)            -> bool(x) is False

# assertIs(a, b)            -> a is b
# assertIsNot(a, b)         -> a is not b

# assertIsNone(x)           -> x is None
# assertIsNotNone(x)        -> x is not None

# assertIn(a, b)            -> a in b
# assertNotIn(a, b)         -> a not in b

# assertIsInstance(a, b)    -> isinstance(a, b)
# assertNotIsInstance(a, b) -> not isinstance(a, b)

def count_left_anything(str):
    result_num = re.search(r"\d",str)
    return "{}".format(result_num)

count_left_anything("Hôm nay là 1231023")

class TestRevengge(unittest.TestCase):
# tạo lớp kiểm trả kiểm tra.trường hợp
    def test_basic(self):
        testcase = r"\d"
        excepted =  r"\d"
        self.assertEqual(count_left_anything(testcase), excepted)

if __name__ == "__main__":
    unittest.main()

