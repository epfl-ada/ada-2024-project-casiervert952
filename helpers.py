import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

#########################################
### Some helper functions for project ###
#########################################

"""
Generate CSV file from TXT file with the particular format of the beer's ratings.

Parameters:
    file_txt (String): The path to the TXT file to be converted.
    file_csv (String): The path to the wanted generated file.
    dataset (String): Indicator that say on which dataset the function is applied ("BA" or "RB").
Returns:
    None.
"""
def txt_to_csv(file_txt, file_csv, dataset):

    data = []
    data_line = []
    iteration = 0
    features = ["beer_name", "beer_id", "brewery_name", "brewery_id", "style", "abv", "date", "user_name", "user_id", "appearance", "aroma", "palate", "taste", "overall", "rating", "text"]
    if dataset == "BA":
         features.append("review")

    # if the file already exist, just delete it
    if os.path.exists(file_csv):
        os.remove(file_csv)

    # let start by oppening the input and output files
    with open(file_txt, 'r', encoding='utf-8') as file:
        with open(file_csv, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # start by writing the features row
            writer.writerow(features)

            # take line by line
            for line in file:
                line = line.strip()

                # if the line is empty, change the rating element
                if line == "":

                        # write the rating elements each 10'000
                        if iteration % 10000 == 0:
                            writer.writerows(data)
                            data = []
                        else:
                            data.append(data_line)
                        
                        iteration += 1
                        print(f"Iteration : {iteration}")
                        data_line = []
                # else add the feature to the in growing line, and supress the feature prefix
                else:
                    parts = line.split(": ")
                    if parts[0] == "text:":
                        data_line.append("")
                    else:
                        data_line.append(parts[1])
            # add the remaining data to the csv file
            if data:
                    writer.writerows(data)

        print("Data have been placed in : " + file_csv)

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
    BA.plot(kind='bar', ax=axes[0], color=sns.color_palette("Blues", n_colors=len(BA))[::-1])
    axes[0].set_xlabel('Countries', fontsize=12)
    axes[0].set_ylabel('Number of Ratings', fontsize=10)
    axes[0].set_title('Top 25 Countries by Ratings (BeerAdvocate) in log scale', fontsize=14)
    axes[0].set_yscale(scale)

    # add text that define the value
    for index, value in enumerate(BA):
        axes[0].text(index, value, f'{value}', ha='center', va='bottom', fontsize=8)

    # bar plot for RB
    RB.plot(kind='bar', ax=axes[1], color=sns.color_palette("Reds", n_colors=len(RB))[::-1])
    axes[1].set_xlabel('Countries', fontsize=10)
    axes[1].set_title('Top 25 Countries by Ratings (RateBeer) in log scale', fontsize=14)
    axes[1].set_yscale(scale)

    # add text that define the value
    for index, value in enumerate(RB):
        axes[1].text(index, value, f'{value}', ha='center', va='bottom', fontsize=8)

    # placing the labels
    for ax in axes:
        ax.tick_params(axis='x', rotation=90)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

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
	BA_ratings_bins.plot(kind='bar', color='skyblue', edgecolor='black', alpha=1, label="BA Users", position=1, width=0.4)

	# add the data for RB in plot
	RB_ratings_bins.plot(kind='bar', color='salmon', edgecolor='black', alpha=1, label="RB Users", position=0, width=0.4)

	# define labels, legend and titles
	plt.title("Distribution of users by number of ratings", fontsize=14)
	plt.xlabel("# Ratings", fontsize=12)
	plt.ylabel("# Users", fontsize=12)
	plt.yscale("log")
	plt.yticks([1, 10, 100, 1000, 10000, 100000], ['1', '10', '100', '1000', '10000', '100000'])  # Adjust y-ticks
	plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))  # Format y labels
	plt.legend()

	# rotate and define size for ticks
	plt.xticks(rotation=90)
	plt.xticks(fontsize=10)
	plt.yticks(fontsize=11)

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

	fig, axes = plt.subplots(1, 2, figsize=(15, 7))

	# define first graph (BA) parameters
	axes[0].plot(BA_ratings_by_month['rating_date'], BA_ratings_by_month['#ratings'], marker='.', linestyle='None', color='blue', markerfacecolor='blue')
	axes[0].set_title('Number of ratings each month', fontsize=14)
	axes[0].set_xlabel('Year', fontsize=12)
	axes[0].set_ylabel('# ratings', fontsize=12)
	axes[0].set_yscale(scale)
	axes[0].set_xlim(pd.to_datetime('01-1998'), pd.to_datetime('12-2017'))
	axes[0].set_xticks(pd.date_range('01-1998', '12-2017', freq='AS'))
	axes[0].set_xticklabels([str(date.year) for date in pd.date_range('01-1998', '12-2017', freq='AS')], rotation=45)
	axes[0].grid(True, axis='x', linestyle='--', linewidth=0.5)
	axes[0].grid(True, axis='y', linestyle='--', linewidth=0.5)

	# define second graph (RB) parameters
	axes[1].plot(RB_ratings_by_month['rating_date'], RB_ratings_by_month['#ratings'], marker='.', linestyle='None', color='blue', markerfacecolor='blue')
	axes[1].set_title('Number of ratings each month', fontsize=14)
	axes[1].set_xlabel('Year', fontsize=12)
	axes[1].set_ylabel('Year', fontsize=12)
	axes[1].set_yscale(scale)
	axes[1].set_xlim(pd.to_datetime('01-1998'), pd.to_datetime('12-2017'))
	axes[1].set_xticks(pd.date_range('01-1998', '12-2017', freq='AS'))
	axes[1].set_xticklabels([str(date.year) for date in pd.date_range('01-1998', '12-2017', freq='AS')], rotation=45)
	axes[1].grid(True, axis='x', linestyle='--', linewidth=0.5)
	axes[1].grid(True, axis='y', linestyle='--', linewidth=0.5)

	# little change on placement
	plt.tight_layout()

	# show the plots
	plt.show()


##########################################
### Some helper dictionary for project ###
##########################################

ratings_dict = {
    "date": "rating_date",
    "appearance": "rating_appearance",
    "aroma": "rating_aroma",
    "palate": "rating_palate",
    "taste": "rating_taste",
    "overall": "rating_overall"
}

beers_dict = {
    "style": "beer_style",
    "nbr_ratings": "beer_nbr_ratings",
    "nbr_reviews": "beer_nbr_reviews",
    "avg": "beer_avg",
    "ba_score": "beer_ba_score",
    "bros_score": "beer_bros_score",
    "abv": "beer_abv",
    "avg_computed": "beer_avg_computed",
    "zscore": "beer_zscore",
    "nbr_matched_valid_ratings": "beer_nbr_matched_valid_ratings",
    "avg_matched_valid_ratings": "beer_avg_matched_valid_ratings"
}

breweries_dict = {
    "location": "breweries_location",
    "nbr_beers": "breweries_nbr_beers"
}

users_dict = {
    "nbr_ratings": "user_nbr_ratings",
    "nbr_reviews": "user_nbr_reviews",
    "joined": "user_join_date",
    "location": "user_location"
}
