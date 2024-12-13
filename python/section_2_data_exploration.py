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
Plot the country representation

Parameters:
    BA (pandas.Series): The country data for BA.
    RB (pandas.Series): The country data for RB.
    scale (String): Specify which scale to use for the plot (log or linear)
Returns:
    None, it just show the plots
"""
def ploting_country_representation(BA, RB, scale):

    sns.set_theme(style="whitegrid")
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6), sharey=True)

    # bar plot for BA
    BA.plot(kind = 'bar', ax = axes[0], color = sns.color_palette("Blues", n_colors = len(BA))[::-1])
    axes[0].set_xlabel('Countries', fontsize=12)
    axes[0].set_ylabel('Number of Ratings', fontsize=10)
    axes[0].set_title('Top 25 Countries by Ratings (BeerAdvocate) in log scale', fontsize = 14)
    axes[0].set_yscale(scale)

    # add text that define the value
    for index, value in enumerate(BA):
        axes[0].text(index, value, f'{value}', ha = 'center', va = 'bottom', fontsize = 8)

    # bar plot for RB
    RB.plot(kind = 'bar', ax = axes[1], color = sns.color_palette("Reds", n_colors=len(RB))[::-1])
    axes[1].set_xlabel('Countries', fontsize=10)
    axes[1].set_title('Top 25 Countries by Ratings (RateBeer) in log scale', fontsize = 14)
    axes[1].set_yscale(scale)

    # add text that define the value
    for index, value in enumerate(RB):
        axes[1].text(index, value, f'{value}', ha = 'center', va = 'bottom', fontsize = 8)

    # placing the labels
    for ax in axes:
        ax.tick_params(axis = 'x', rotation = 90)
        ax.grid(axis = 'y', linestyle = '--', alpha = 0.7)

    plt.tight_layout()
    plt.show()


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
Plot the #ratings by users

Parameters:
    BA_ratings_bins (pandas.Series): The #ratings by users data for BA.
    RB_ratings_bins (pandas.Series): The #ratings by users data for RB.
Returns:
    None, it just show the plots
"""
def ploting_user_ratings_distribution(BA_ratings_bins, RB_ratings_bins):
	
	plt.figure(figsize=(15, 6))

	# add the data for BA in plot
	BA_ratings_bins.plot(kind = 'bar', color = 'skyblue', edgecolor = 'black', alpha = 1, label = "BA Users", position = 1, width = 0.4)

	# add the data for RB in plot
	RB_ratings_bins.plot(kind = 'bar', color = 'salmon', edgecolor = 'black', alpha = 1, label = "RB Users", position = 0, width = 0.4)

	# define labels, legend and titles
	plt.title("Distribution of users by number of ratings", fontsize = 14)
	plt.xlabel("# Ratings", fontsize = 12)
	plt.ylabel("# Users", fontsize = 12)
	plt.yscale("log")
	plt.yticks([1, 10, 100, 1000, 10000, 100000], ['1', '10', '100', '1000', '10000', '100000'])  # Define y-ticks
	plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))  # Format y labels
	plt.legend()

	# rotate and define size for ticks
	plt.xticks(rotation = 90)
	plt.xticks(fontsize = 10)
	plt.yticks(fontsize = 11)

	# little change on placement
	plt.tight_layout()
	plt.xlim(-0.7)
	
	# show the plot
	plt.show()


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
    display(ratings_by_country_sorted.T)
	

"""
Compute the #ratings by beer and group them in bins.

Parameters:
    BA_cleaned : BA DataFrame
    RB_cleaned : RB DataFrame
Returns:
    The two bins with data.
"""
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


"""
Compute the #ratings by user and group them in bins.

Parameters:
    BA_cleaned : BA DataFrame
    RB_cleaned : RB DataFrame
Returns:
    The two bins with data.
"""
def number_ratings_by_user(BA_cleaned, RB_cleaned):

	# Computing the #ratings by users, and grouping them in bins of size 1000
	BA_ratings_by_user = BA_cleaned.groupby('user_id').size().reset_index(name='#ratings')
	BA_ratings_bins = pd.cut(BA_ratings_by_user['#ratings'], bins=np.arange(0, BA_ratings_by_user['#ratings'].max() + 1000, 1000))
	BA_ratings_bins = BA_ratings_bins.value_counts().sort_index()

	RB_ratings_by_user = RB_cleaned.groupby('user_id').size().reset_index(name='#ratings')
	RB_ratings_bins = pd.cut(RB_ratings_by_user['#ratings'], bins=np.arange(0, RB_ratings_by_user['#ratings'].max() + 1000, 1000))
	RB_ratings_bins = RB_ratings_bins.value_counts().sort_index()

	# Only show the minial value of the bins in the graph
	BA_ratings_bins.index = [f'{int(bin.left)}' for bin in BA_ratings_bins.index]
	RB_ratings_bins.index = [f'{int(bin.left)}' for bin in RB_ratings_bins.index]
	
	return BA_ratings_bins, RB_ratings_bins, RB_ratings_by_user

"""
Plot the #ratings by beer

Parameters:
    BA_ratings_bins (pandas.Series): The #ratings by users data for BA.
    RB_ratings_bins (pandas.Series): The #ratings by users data for RB.
Returns:
    None, it just show the plots
"""
def ploting_beer_ratings_distribution(BA_ratings_bins, RB_ratings_bins):
	
	plt.figure(figsize=(15, 6))

	# add the data for BA in plot
	BA_ratings_bins.plot(kind = 'bar', color = 'skyblue', edgecolor = 'black', alpha = 1, label = "BA Users", position = 1, width = 0.4)

	# add the data for RB in plot
	RB_ratings_bins.plot(kind = 'bar', color = 'salmon', edgecolor = 'black', alpha = 1, label = "RB Users", position = 0, width = 0.4)

	# define labels, legend and titles
	plt.title("Distribution of users by number of ratings", fontsize = 14)
	plt.xlabel("# Ratings", fontsize = 12)
	plt.ylabel("# Users", fontsize = 12)
	plt.yscale("log")
	plt.yticks([1, 10, 100, 1000, 10000, 100000], ['1', '10', '100', '1000', '10000', '100000'])  # Define y-ticks
	plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))  # Format y labels
	plt.legend()

	# rotate and define size for ticks
	plt.xticks(rotation = 90)
	plt.xticks(fontsize = 10)
	plt.yticks(fontsize = 11)

	# little change on placement
	plt.tight_layout()
	plt.xlim(-0.7)
	
	# show the plot
	plt.show()

"""
Plot the #ratings by months

Parameters:
    BA_ratings_by_month (pandas.Series): The #ratings by months data for BA.
    RB_ratings_by_month (pandas.Series): The #ratings by months data for RB.
    scale (String): Specify which scale to use for the plot (log or linear)
Returns:
    None, it just show the plots
"""
def ploting_ratings_by_month(BA_ratings_by_month, RB_ratings_by_month, scale):

	fig, axes = plt.subplots(1, 2, figsize = (15, 7))

	# define first graph (BA) parameters
	axes[0].plot(BA_ratings_by_month['rating_date'], BA_ratings_by_month['#ratings'], marker = '.', linestyle = 'None', color = 'blue', markerfacecolor = 'blue')
	axes[0].set_title('Number of ratings each month for BeerAdvocate (log scale)', fontsize = 14)
	axes[0].set_xlabel('Year', fontsize = 12)
	axes[0].set_ylabel('# ratings', fontsize = 12)
	axes[0].set_yscale(scale)
	axes[0].set_xlim(pd.to_datetime('01-1998'), pd.to_datetime('12-2017'))
	axes[0].set_xticks(pd.date_range('01-1998', '12-2017', freq = 'YS'))
	axes[0].set_xticklabels([str(date.year) for date in pd.date_range('01-1998', '12-2017', freq = 'YS')], rotation = 45)
	axes[0].grid(True, axis = 'x', linestyle = '--', linewidth = 0.5)
	axes[0].grid(True, axis = 'y', linestyle = '--', linewidth = 0.5)

	# define second graph (RB) parameters
	axes[1].plot(RB_ratings_by_month['rating_date'], RB_ratings_by_month['#ratings'], marker = '.', linestyle = 'None', color = 'blue', markerfacecolor = 'blue')
	axes[1].set_title('Number of ratings each month for RateBeer (log scale)', fontsize = 14)
	axes[1].set_xlabel('Year', fontsize = 12)
	axes[1].set_ylabel('# ratings', fontsize = 12)
	axes[1].set_yscale(scale)
	axes[1].set_xlim(pd.to_datetime('01-1998'), pd.to_datetime('12-2017'))
	axes[1].set_xticks(pd.date_range('01-1998', '12-2017', freq = 'YS'))
	axes[1].set_xticklabels([str(date.year) for date in pd.date_range('01-1998', '12-2017', freq = 'YS')], rotation = 45)
	axes[1].grid(True, axis = 'x', linestyle = '--', linewidth = 0.5)
	axes[1].grid(True, axis = 'y', linestyle = '--', linewidth = 0.5)

	# little change on placement
	plt.tight_layout()

	# show the plots
	plt.show()
