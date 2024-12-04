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
	

"""
Compute the top n republican/democrat states.

Parameters:
    n : Number of top stats in rep/dem lists.
Returns:
    The top n of each democrate and republican states.
"""
def top_n_rep_dem(n, dem_year_, dem_year_score_df, rep_year_, rep_year_score_df):

	# Define the n rep and dem lists
    top_n_republican = []
    top_n_democrat = []
    dem_y_ = dem_year_.reset_index()
    rep_y_ = rep_year_.reset_index()

    dem_year = dem_year_score_df.copy().sort_values(by = 'Average', ascending = False)
    dem_year = dem_year.drop(['DC']).reset_index() #DC is washington DC =/= state of washington
    rep_year = rep_year_score_df.copy().sort_values(by = 'Average', ascending = False)
    rep_year = rep_year.reset_index()

    dem_year = dem_year[:n]
    rep_year = rep_year[:n]

    for st_po in dem_year['state_po'].values:

        state = dem_y_[dem_y_['state_po'] == st_po]['state']
        top_n_democrat.append(state.values[0].title())
        
    for st_po in rep_year['state_po']:

        state = rep_y_[rep_y_['state_po'] == st_po]['state']
        top_n_republican.append(state.values[0].title())
    
    return top_n_democrat, top_n_republican