import subprocess
import time

class multijob(object):
    def __init__(self, max_jobs, poll_interval):
        self.max_jobs = max_jobs
        self.poll_interval = poll_interval
        self.jobs = []
    def run_job(self, args):
        while not (len(self.jobs) < self.max_jobs or self.poll_jobs()):
            time.sleep(self.poll_interval)
        self.jobs.append(subprocess.Popen(args))
    def wait_all(self):
        for child in self.jobs:
            child.wait()
            self.jobs.remove(child)
    def poll_jobs(self):
        for child in self.jobs:
            res = child.poll()
            if res is not None:
                self.jobs.remove(child)
                return True
        return False