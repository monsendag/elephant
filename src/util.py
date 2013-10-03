
from os.path import dirname, normpath, join
from datetime import datetime


def path(rel):
    project_root = dirname(dirname(__file__))
    return normpath(join(project_root, rel))


def timer(func):
    start = datetime.now()
    func()
    end = datetime.now()
    return end-start
