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


##########################################
###    Some helper lists for project   ###
##########################################

north_america_countries = [
    "United States", "Canada"
]

european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
    "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
    "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland",
    "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
    "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "England",
    "Vatican City"
]

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
