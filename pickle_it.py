# pickle_it.py
# a shortcut to pickling binary Python objects

import pickle

def pickle_it(item, fname):
    with open(fname, 'wb') as f:
        pickle.dump(item, f)