multijob
========
Use this python module to run a list of independent jobs unattended.
You can specify how many jobs can be run in parallel to take advantage of your multi-core CPUs.

Usage
----
Initialize the multijob object by specifying `max_jobs`: maximum number of jobs to run in parallel, and `poll_interval`: the interval in seconds for the scheduler to check if any of the jobs are finished.

```python
import multijob
scheduler = multijob.multijob(max_jobs=2, poll_interval=60)
```

To run the (long) jobs, just throw a list of commands at it by calling `run_job`.
It will run up to `max_jobs` at a time and checking every `poll_interval` seconds to see if there are any jobs finished so new jobs can be scheduled.
`run_job` is a blocking call so it will not return until the command you feed to it actually starts.
You can pass optional `nice` value to `run_job` (in unix-like system) to lower your job process' priority.

```python
cmds = [
  ["command1", "--option1", "optarg1"],
  ["command2", "--option2", "optarg2"],
  ["command3", "--option3", "optarg3"],
]
scheduler = multijob.multijob(max_jobs=2, poll_interval=1)
for c in cmds:
    scheduler.run_job(c, nice=10)
scheduler.wait_all()
```
Call `wait_all` to wait for all jobs to finish.
The object will call it automatically on deletion.
