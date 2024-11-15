import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

#########################################
###    Function for data analysis     ###
#########################################

"""
Compute the consumtion type preferances by states.

Parameters:
    BA_usa : DataFrame containing all US ratings.
Returns:
    The preferances of each states for local, national and international.
"""
def compute_consumtion_type_states_preferances(BA_usa):
	# compute the average rating for each consumption (Local, National, International) type for each state
	state_consumption_stats = BA_usa.groupby(['user_state', 'consumption_type']).agg(
		count = ('rating', 'size'),
		consumption_type_avg_rating = ('rating', 'mean')
	).reset_index()

	# compute total consumption count per state to see the % of each consumption type
	total_counts_per_state = state_consumption_stats.groupby('user_state')['count'].transform('sum')
	state_consumption_stats['percentage'] = (state_consumption_stats['count'] / total_counts_per_state) * 100

	# compute overall average rating for each state
	state_avg_rating = BA_usa.groupby('user_state')['rating'].mean().reset_index(name = 'state_avg_rating')

	# merge overall average state rating into the main dataframe
	state_consumption_stats = state_consumption_stats.merge(state_avg_rating, on = 'user_state')


	# states that prefer local beers
	local_preference = state_consumption_stats[state_consumption_stats['consumption_type'] == 'Local']
	# states that prefer national beers
	national_preference = state_consumption_stats[state_consumption_stats['consumption_type'] == 'National']
	# states that prefer international beers
	international_preference = state_consumption_stats[state_consumption_stats['consumption_type'] == 'International']
	
	return local_preference, national_preference, international_preference