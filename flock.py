"""
a simple python tool to lock the process base on python3

usage:
import flock

@process_lock
def your_func():
    your code
"""

try:
    import fcntl
except Exception as e:
    raise ImportError('import fcntl model error. check log file to resolve problem')


def process_lock(func):
    def lock(*args, **kwargs):
        with open('.python_lock_file', 'w+') as f:
            try:
                fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except Exception as e:
                raise RuntimeWarning('program has been started,  exit now')
            return func()

    return lock
