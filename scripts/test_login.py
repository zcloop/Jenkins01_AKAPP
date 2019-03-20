import os
import sys
sys.path.append(os.getcwd())

from time import sleep

from base.get_driver import get_driver


class TestLogin():
    def setup(self):
        self.driver = get_driver()

    def test01(self):
        print("test01被执行")

    def teardown(self):
        sleep(3)
        self.driver.quit()