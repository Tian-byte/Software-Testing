import logging
import unittest


from logging_use import init_log_config


def add(x,y):
    return x +y

class TestAdd(unittest.TestCase):
    init_log_config("add.log")
    def test01_add(self):
       resp = add(10,20)
       logging.debug(f"resp={resp}")
