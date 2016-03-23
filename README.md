multijob
========
A simple python module to run a list of commands with no more than `max_jobs` ones running at the same time.

Usage
----
```python
import multijob
cmds = [
  ["command1", "--option1", "optarg1"],
  ["command2", "--option2", "optarg2"],
  ["command3", "--option3", "optarg3"],
]
scheduler = multijob.multijob(max_jobs=2, poll_interval=1)
for c in cmds:
    scheduler.run_job(c)
scheduler.wait_all()
```
