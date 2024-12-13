import time
import pandas as pd


#########################################
###     Function for data loading     ###
#########################################


"""
Load all the data files for the BA datasets

Parameters:
    None
Returns:
    The 4 dataframes that contains all informations of BA
"""
def load_data_BA(BA_DATA_PATH) :
    # create Dataframes for the BA cleaned data
    s_time = time.time()
    BA_cleaned = pd.read_csv(BA_DATA_PATH + 'BA_cleaned.csv', low_memory=False)
    e_time = time.time()
    print("Loading of BA data ended in " + str(e_time - s_time) + " seconds.")

    # loading extra data useful for "Data exploration"
    BA_beers = pd.read_csv(BA_DATA_PATH + 'beers.csv')
    BA_breweries = pd.read_csv(BA_DATA_PATH + 'breweries.csv')
    BA_users = pd.read_csv(BA_DATA_PATH + 'users.csv')

    return BA_cleaned, BA_beers, BA_breweries, BA_users
	

"""
Load all the data files for the RB datasets

Parameters:
    None
Returns:
    The 4 dataframes that contains all informations of RB
"""
def load_data_RB(RB_DATA_PATH) :
    # create Dataframes for the RB cleaned data
    s_time = time.time()
    RB_cleaned = pd.read_csv(RB_DATA_PATH + 'RB_cleaned.csv', low_memory=False)
    e_time = time.time()
    print("Loading of RB data ended in " + str(e_time - s_time) + " seconds.")
    
    # loading extra data useful for "Data exploration"
    RB_beers = pd.read_csv(RB_DATA_PATH + 'beers.csv')
    RB_breweries = pd.read_csv(RB_DATA_PATH + 'breweries.csv')
    RB_users = pd.read_csv(RB_DATA_PATH + 'users.csv')

    return RB_cleaned, RB_beers, RB_breweries, RB_users