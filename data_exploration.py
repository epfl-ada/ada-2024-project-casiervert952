import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

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