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
def logarithmic(x, max_stability_threshold):
    return np.minimum(1, np.log10(x + 1) / np.log10(max_stability_threshold))

def show_reduction_function(max_stability_threshold):
	x = np.linspace(0, 120, 500)
	y_log = logarithmic(x, max_stability_threshold)

	# plotting
	plt.figure(figsize=(10, 6))
	plt.plot(x, y_log, label="Logarithmique", linewidth=2)
	plt.xlabel("Number of rating")
	plt.ylabel("Value")
	plt.title("Reduction function f(N)")
	plt.legend()
	plt.grid(True)
	plt.show()

def calculate_stability_threshold(ratings, tolerance=0.1, window_size=10):
    cumulative_means = np.cumsum(ratings) / np.arange(1, len(ratings) + 1)
    
    # check the stability on the window
    for i in range(len(cumulative_means) - window_size + 1):
        window = cumulative_means[i:i + window_size]
        if max(window) - min(window) <= tolerance:
            return i + window_size
    
    # return 0 si no window satisfying the tolerance on the window_size is found
    return 0


def calculate_max_stability_threshold_on_all_beers(grouped_rating_by_beer, tolerance=0.1, window_size=10):
    # saving the stability thresholds
    stability_thresholds = {}

    # iterate on all beers
    for beer_id, group in grouped_rating_by_beer:
        ratings = group['rating'].values
        if len(ratings) >= 5:
            threshold = calculate_stability_threshold(ratings, tolerance, window_size)
            stability_thresholds[beer_id] = threshold
        else:
            stability_thresholds[beer_id] = 0

    # return the maximal value of the thresholds found.
    return max(stability_thresholds.values())