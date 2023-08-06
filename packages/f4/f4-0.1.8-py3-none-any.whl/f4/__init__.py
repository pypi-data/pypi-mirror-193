#TODO:
#  https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#  https://medium.com/@skylar.kerzner/publish-your-first-python-package-to-pypi-8d08d6399c2f
#TODO
#import asyncio
import datetime
#TODO
print(f"got here init 0 - {datetime.datetime.now()}")
import fastnumbers
import glob
import gzip
from itertools import chain
#TODO
#from joblib import Parallel, delayed
import math
import mmap
import msgspec
# #TODO:
#import multiprocessing
import operator
from operator import itemgetter
import os
import re
import shutil
import sys
import tempfile
import zstandard

print(f"got here init 1 - {datetime.datetime.now()}")

#from . Builder import testme

#print("got here2")

from f4.Utilities import *
from f4.Builder import *
from f4.Filters import *
from f4.IndexBuilder import *
from f4.IndexSearcher import *
from f4.Parser import *

print(f"got here init 2 - {datetime.datetime.now()}")