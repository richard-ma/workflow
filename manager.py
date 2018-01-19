import unittest
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)

    command = sys.argv[1]

    if command == "test":
        tests = unittest.TestLoader().discover(
            'tests', pattern='*_tests.py')
        unittest.TextTestRunner(verbosity=1).run(tests)
