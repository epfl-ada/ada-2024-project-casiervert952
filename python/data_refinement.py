import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from collections import Counter

#########################################
###   Function for data refinement    ###
#########################################

# Logarithmique
def logarithmic(x):
    return np.minimum(1, np.log10(x + 1) / np.log10(100))

def show_reduction_function():
	x = np.linspace(0, 120, 500)
	y_log = logarithmic(x)

	# plotting
	plt.figure(figsize=(10, 6))
	plt.plot(x, y_log, label="Logarithmique", linewidth=2)
	plt.xlabel("Number of rating")
	plt.ylabel("Value")
	plt.title("Reduction function f(N)")
	plt.legend()
	plt.grid(True)
	plt.show()