"""Init file """
__version__= '0.0.13'

import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import dreem.demultiplex.main as demultiplexing
import dreem.align.main as alignment
import dreem.vector.main as vectoring
import dreem.cluster.main as clustering
import dreem.aggregate.main as aggregation
import dreem.draw.main as drawer
from dreem.draw.study import Study

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
