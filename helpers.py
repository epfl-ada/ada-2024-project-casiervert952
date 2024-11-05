import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns

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

    # If the file already exist, just delete it
    if os.path.exists(file_csv):
        os.remove(file_csv)

    # Let start by oppening the input and output files
    with open(file_txt, 'r', encoding='utf-8') as file:
        with open(file_csv, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Start by writing the features row
            writer.writerow(features)

            # Take line by line
            for line in file:
                line = line.strip()

                # If the line is empty, change the rating element
                if line == "":

                        # Write the rating elements each 10'000
                        if iteration % 10000 == 0:
                            writer.writerows(data)
                            data = []
                        else:
                            data.append(data_line)
                        
                        iteration += 1
                        print(f"Iteration : {iteration}")
                        data_line = []
                # Else add the feature to the in growing line, and supress the feature prefix
                else:
                    parts = line.split(": ")
                    if parts[0] == "text:":
                        data_line.append("")
                    else:
                        data_line.append(parts[1])
            # Add the remaining data to the csv file
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

    # Bar plot for BA
    BA.plot(kind='bar', ax=axes[0], color=sns.color_palette("Blues", n_colors=len(BA))[::-1])
    axes[0].set_xlabel('Countries', fontsize=12)
    axes[0].set_ylabel('Number of Ratings', fontsize=12)
    axes[0].set_title('Top 25 Countries by Ratings (BeerAdvocate)', fontsize=14)
    axes[0].set_yscale(scale)

    # Add text that define the value
    for index, value in enumerate(BA):
        axes[0].text(index, value, f'{value}', ha='center', va='bottom', fontsize=8)

    # Bar plot for RB
    RB.plot(kind='bar', ax=axes[1], color=sns.color_palette("Reds", n_colors=len(RB))[::-1])
    axes[1].set_xlabel('Countries', fontsize=12)
    axes[1].set_title('Top 25 Countries by Ratings (RateBeer)', fontsize=14)
    axes[1].set_yscale(scale)

    # Add text that define the value
    for index, value in enumerate(RB):
        axes[1].text(index, value, f'{value}', ha='center', va='bottom', fontsize=8)

    # Placing the labels
    for ax in axes:
        ax.tick_params(axis='x', rotation=90)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
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
