import unittest
import multijob
import time
class TestMultiJobTiming(unittest.TestCase):
    def test_timing(self):
        cmds = [
            ["python", "-c", "import time; time.sleep(5)"],
            ["python", "-c", "import time; time.sleep(3)"],
            ["python", "-c", "import time; time.sleep(1)"],
        ]
        m = multijob.multijob(2,1)
        start = time.time()
        for c in cmds:
            m.run_job(c)
        m.wait_all()
        spent = time.time() - start
        self.assertGreater(spent, 5)
        self.assertLess(spent, 6)
if __name__ == '__main__':
    unittest.main()