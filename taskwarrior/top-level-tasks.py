#!/bin/env python
import os
import os.path
import subprocess
import sys

TOP_DIR = os.getenv("HOME")
TASK_COMMAND = ["/bin/env", "task"]

def walk_up(start, end):
  current_path = start

  while True:
    if current_path == end:
      return

    yield current_path

    current_path = os.path.normpath(os.path.join(current_path, ".."))


def exists_up(start, end, path):
  for current_path in walk_up(start, end):
    if os.path.exists(os.path.join(current_path, path)):
      return current_path

if __name__ == '__main__':
  path = exists_up(os.getcwd(), TOP_DIR, ".task")
  path = path and os.path.join(path, ".task")

  command = TASK_COMMAND + sys.argv[1:]

  if path:
    command.insert(len(TASK_COMMAND), "rc.data.location:%s" % (path,))

  subprocess.call(command)
