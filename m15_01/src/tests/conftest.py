import os


def pytest_generate_tests():
    os.environ['ENV_APP'] = 'STAGE'

