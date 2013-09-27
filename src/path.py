
from os.path import dirname, normpath, join

def get(rel):
    project_root = dirname(dirname(__file__))
    return normpath(join(project_root, rel))

#get('/data/movielens-1m')
