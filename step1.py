#Dynamic

""" 1s simulation ( time_steps*steps ) of a 15 nm water box only at room temperature with an equilibration phase of approximately
10ps ( verify by plotting Temperature as a function of time )"""


#MODULES
import os
import openmm
import numpy as np
import openmm.app as app

from openmm import LangevinIntegrator
from openmm.app import *
from openmm import *
from openmm.unit import *

from sys import stdout

#DIRECTORY
