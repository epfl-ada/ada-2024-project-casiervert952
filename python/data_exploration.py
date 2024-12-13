import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from collections import Counter

#########################################
###  Function for data exploration    ###
#########################################

"""
Compute the % of missing value for all field for both datasets

Parameters:
    BA_cleaned : BA DataFrame
    RB_cleaned : RB DataFrame
Returns:
    Two DataFrame with missing value for BA and RB
"""
def compute_missing_value_in_datsets(BA_cleaned, RB_cleaned):
	# compute missing values by columns
    missing_count_BA = BA_cleaned.isna().sum()
    missing_percentage_BA = (missing_count_BA / len(BA_cleaned)) * 100
    missing_count_RB = RB_cleaned.isna().sum()
    missing_percentage_RB = (missing_count_RB / len(RB_cleaned)) * 100
    
    # put results in a dataframe
    missing_data_BA = pd.DataFrame({
        'Column': BA_cleaned.columns,
        'Missing Values (BA)': missing_count_BA,
        '% (BA)': missing_percentage_BA
    })
    missing_data_RB = pd.DataFrame({
        'Column': RB_cleaned.columns,
        'Missing Values (RB)': missing_count_RB,
        '% (RB)': missing_percentage_RB
    })
    
    # sort by "%"
    missing_data_BA = missing_data_BA.sort_values(by = '% (BA)', ascending = False)
    missing_data_RB = missing_data_RB.sort_values(by = '% (RB)', ascending = False)
	
    return missing_data_BA, missing_data_RB


"""
Compute the % of ratings from EU and NA for both datasets

Parameters:
    country_comparison : The country data for BA.
    north_america_countries (list): The list of NA countries
    european_countries (list): The list of EU countries
Returns:
    None, it just print the results
"""
def computing_NA_EU_countries(country_comparison, north_america_countries, european_countries):
	# NA: compute total % of ratings for BeerAdvocate
	na_BA_percentage = country_comparison[country_comparison['Country (BA)'].isin(north_america_countries)]['% of Ratings (BeerAdvocate)'].sum()
	print('NA:\n   Total % of ratings (BA) :', round(na_BA_percentage,1), '%')

	# NA: compute total % of ratings for RateBeer
	na_RB_percentage = country_comparison[country_comparison['Country (RB)'].isin(north_america_countries)]['% of Ratings (RateBeer)'].sum()
	print('   Total % of ratings (RB) :', round(na_RB_percentage,1), '%')

	# EU: compute total % of ratings for BeerAdvocate
	BA_european_percentage = country_comparison[country_comparison['Country (BA)'].isin(european_countries)]['% of Ratings (BeerAdvocate)'].sum()
	print('\nEU:\n   Total % of ratings (BA) :', round(BA_european_percentage,1), '%')

	# EU: compute total % of ratings for RateBeer
	RB_european_percentage = country_comparison[country_comparison['Country (RB)'].isin(european_countries)]['% of Ratings (RateBeer)'].sum()
	print('   Total % of ratings (RB) :', round(RB_european_percentage,1), '%')

	# compute and print total loss of ratings coming from other continents for both datasets
	BA_total_loss = 100 - na_BA_percentage - BA_european_percentage
	print ("\nOther continents (loss):\n   Total % of ratings (BA) :", round(BA_total_loss,1), '%')
	RB_total_loss = 100 - na_RB_percentage - RB_european_percentage
	print ("   Total % of ratings (RB) :", round(RB_total_loss,1), '%')


"""
Compute the #ratings by contry for high rated users

Parameters:
    n : The number of ratings a high rated users made
Returns:
    None, it just print the results
"""
def high_rated_users_by_country(n, RB_ratings_by_user, RB_cleaned):
    # Keep only user with more than n ratings made
    high_rated_users = RB_ratings_by_user[RB_ratings_by_user["#ratings"] > n]
    
    ratings_by_rated_users = RB_cleaned[RB_cleaned['user_id'].isin(high_rated_users['user_id'])]
    RB_cleaned_with_ratings = ratings_by_rated_users.merge(high_rated_users[['user_id', '#ratings']], on='user_id', how='left')
    
    # Group by localisation user_country, count the #ratings and sort them
    ratings_by_country = RB_cleaned_with_ratings.groupby("user_country")["#ratings"].count().reset_index()

    ratings_by_country_sorted = ratings_by_country.sort_values(by="#ratings", ascending = False).reset_index().drop(columns=["index"])
    
    # Display the result
    display(ratings_by_country_sorted)
	

def number_ratings_by_beer(BA_cleaned, RB_cleaned):

	# Computing the #ratings by beer, and grouping them in bins of size 100
	BA_ratings_by_beer = BA_cleaned.groupby('beer_id').size().reset_index(name='#ratings')
	BA_ratings_bins = pd.cut(BA_ratings_by_beer['#ratings'], bins=np.arange(0, BA_ratings_by_beer['#ratings'].max() + 100, 100))
	BA_ratings_bins = BA_ratings_bins.value_counts().sort_index()

	RB_ratings_by_beer = RB_cleaned.groupby('beer_id').size().reset_index(name='#ratings')
	RB_ratings_bins = pd.cut(RB_ratings_by_beer['#ratings'], bins=np.arange(0, RB_ratings_by_beer['#ratings'].max() + 100, 100))
	RB_ratings_bins = RB_ratings_bins.value_counts().sort_index()

	# Only show the minial value of the bins in the graph
	BA_ratings_bins.index = [f'{int(bin.left)}' for bin in BA_ratings_bins.index]
	RB_ratings_bins.index = [f'{int(bin.left)}' for bin in RB_ratings_bins.index]
	
	return BA_ratings_bins, RB_ratings_bins