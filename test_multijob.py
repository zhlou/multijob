import unittest
import multijob
import time
try:
    import psutil
    has_psutil = True
except ImportError:
    has_psutil = False
class TestMultiJobTiming(unittest.TestCase):
    def test_timing(self):
        cmds = [
            ["python", "-c", "import time; time.sleep(0.5)"],
            ["python", "-c", "import time; time.sleep(0.3)"],
            ["python", "-c", "import time; time.sleep(0.1)"],
        ]
        m = multijob.multijob(2,0.1)
        start = time.time()
        for c in cmds:
            m.run_job(c)
        m.wait_all()
        spent = time.time() - start
        self.assertGreater(spent, 0.5)
        self.assertLess(spent, 0.6)
    @unittest.skipIf(not has_psutil, "psutil not installed")
    def test_nice(self):
        cmd = ["python", "-c", "import time; time.sleep(0.1)"]
        m = multijob.multijob(1,0.1)
        m.run_job(cmd, nice=10)
        pid = m.jobs[0].pid
        p = psutil.Process(pid)
        self.assertEqual(p.nice(), 10)
        m.wait_all()
    def test_dtor(self):
        def in_scope():
            cmd = ["python", "-c", "import time; time.sleep(0.2)"]
            m = multijob.multijob(1,0.1)
            m.run_job(cmd)
        start = time.time()
        in_scope()
        spent = time.time() - start
        self.assertGreater(spent, 0.2)

if __name__ == '__main__':
    unittest.main()
