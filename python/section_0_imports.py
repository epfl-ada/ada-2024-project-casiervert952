# import the basic requiered libraries
import os
import csv
import sys
import time
import warnings
import importlib
import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from collections import Counter
# path variables
BA_DATA_PATH = "data/BeerAdvocate/"
RB_DATA_PATH = "data/RateBeer/"

# import extrernal python fie
sys.path.append('python')
import helpers
import section_1_data_loading
import section_2_data_exploration
import section_3_data_refinement
import section_4_US_politics
import section_5_analysis