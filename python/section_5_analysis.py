import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from section_3_data_refinement import *
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

def beers_with_n_reviews(df_state,n,proportioned_n=False):
    state = df_state['user_state'].unique()
    old_n = n
    if proportioned_n:
        total_nb_review = len(df_state)
        nb_of_beers = df_state['beer_id'].nunique()
        n = total_nb_review//nb_of_beers #n as the mean of nb of reviews for the state
        print(f'{state}\nTotal nb of reviews:{total_nb_review},nb of beers:{nb_of_beers},threshold = {n}\n')

    counts = df_state.groupby('beer_id')['rating'].transform('count')
    df_state = df_state[counts >= n]

    return df_state

def create_df_weighted_counts(pd_top5_republican,pd_top5_democrat):
    # add weight in counts, from top1 to top5 : weights = [5,4,3,2,1]
    x = pd.Series(dtype='int')  # Initialize empty Series with dtype
    for i in range(pd_top5_republican.shape[0]):
        weight = 5 - i
        counts = pd_top5_republican.drop(['Top 5'], axis=1).loc[i].value_counts() * weight
        x = pd.concat([x, counts])

    y = pd.Series(dtype='int')  # Initialize empty Series with dtype
    for i in range(pd_top5_democrat.shape[0]):
        weight = 5 - i
        counts = pd_top5_democrat.drop(['Top 5'], axis=1).loc[i].value_counts() * weight
        y = pd.concat([y, counts])

    x = x.groupby(x.index).sum().sort_values(ascending=False)
    y = y.groupby(y.index).sum().sort_values(ascending=False)

    rep_top = pd.DataFrame({
        'Beer styles': x.index,
        'Weighted count': x.values,
    })
    dem_top = pd.DataFrame({
        'Beer styles': y.index,
        'Weighted count': y.values,
    })

    rep_top['State type'] = 'Republican'
    dem_top['State type'] = 'Democrat'

    df_combined = pd.concat([rep_top,dem_top]).sort_values(by = ['State type'],ascending=False)

    return df_combined

def all_styles_in_top(topn_republican,topn_democrat,pd_top5_republican,pd_top5_democrat):
    styles_rep = []
    styles_dem = []
    for col in topn_republican:
        styles_rep.append(list(pd_top5_republican[col].values))
    styles_rep = [item for sous_liste in styles_rep for item in sous_liste]
    #styles_rep = list(set(styles_rep))

    for col in topn_democrat:
        styles_dem.append(list(pd_top5_democrat[col].values))
    styles_dem = [item for sous_liste in styles_dem for item in sous_liste]
    #styles_dem = list(set(styles_dem))

    # keep the values that need to be added
    styles = list(set(styles_dem + styles_rep))

    return styles


def create_dfs_in_topn_on_metric(df_usa,topn_republican,topn_democrat,metric,top_m_beer,fct='rating',styles = False,filter=True,preference_score = False):
    # Democrats States
    #Create the correct length DataFrames
    if styles:
        pd_topm_democrat = pd.DataFrame({
            'Top '+ str(len(styles)+top_m_beer):np.arange(1,len(styles)+top_m_beer+1)
        })
    else:
        pd_topm_democrat = pd.DataFrame({
            'Top '+ str(top_m_beer):np.arange(1, top_m_beer+1)
        })
    

    for state in topn_democrat:
        BA_state = df_usa.copy()[df_usa['user_state'] == str(state)]

        
        #if we want to compare on the Pscore, compute it first
        if preference_score:
            filter = False #no filter as we integrate the low nb of rating in the score

            # compute the R, N for each beer
            R = BA_state.groupby('beer_id')['rating'].mean()
            N = BA_state.groupby('beer_id')['rating'].size()

            grouped_rating_by_beer = BA_state[['rating', 'beer_id']].groupby('beer_id')
            #Compute the max stability threshold
            max_stability_threshold = calculate_max_stability_threshold_on_all_beers(grouped_rating_by_beer, 0.05, 10)
            # compute the score for each beer
            score = R * logarithmic(N,max_stability_threshold)

            # adding the score to ratings dataframe
            BA_state['preference_score'] = BA_state['beer_id'].map(score)

        #If we want to keep only sufficiently rated beers
        if filter:
            # keep the beer if it has at least 10 ratings
            BA_state = beers_with_n_reviews(BA_state,10,proportioned_n=False)

        #Create the top of the state, depending on the value we compare
        if preference_score:
            topm_state = BA_state[['beer_name', 'beer_style', 'breweries_location', 'preference_score']].groupby(['beer_style']).agg({'preference_score': metric}).sort_values('preference_score', ascending = False)
            
        else:
            #Take the topm beer styles depending on ratings for each state
            topm_state = BA_state[['beer_name', 'beer_style', 'breweries_location', 'rating']].groupby(['beer_style']).agg({'rating': metric}).sort_values('rating', ascending = False)

        

        if styles:
            # check that every style has ratings on it, else add it with None for the mean ratings
            for style in styles:
                if style in topm_state.index:
                    pass
                else:
                    topm_state.loc[style] = None
            topm_state = pd.concat([topm_state.head(top_m_beer), topm_state.loc[styles]])#(has duplicates that will be removed)

            #Insert top m beer styles + other styles in the df 
            pd_topm_democrat[state] = topm_state.index

            # add ratings of each beer_styles
            if preference_score:
                pd_topm_democrat[state + '_'+fct] = topm_state['preference_score'].values 
            else:
                pd_topm_democrat[state + '_'+fct] = topm_state['rating'].values 
            

        else:
            #Insert top m beer styles in the df
            pd_topm_democrat[state] = topm_state[:top_m_beer].index


    # Republican States
    #Create the correct length DataFrames
    if styles:
        pd_topm_republican = pd.DataFrame({
            'Top '+ str(len(styles)+top_m_beer):np.arange(1,len(styles)+top_m_beer+1)
        })
    else:
        pd_topm_republican = pd.DataFrame({
            'Top '+ str(top_m_beer):np.arange(1, top_m_beer+1)
        })
    

    #Iterate through every state
    for state in topn_republican:
        BA_state = df_usa.copy()[df_usa['user_state'] == str(state)]

        #if we want to compare on the Pscore, compute it first
        if preference_score:
            filter = False #no filter as we integrate the low nb of rating in the score

            # compute the R, N for each beer
            R = BA_state.groupby('beer_id')['rating'].mean()
            N = BA_state.groupby('beer_id')['rating'].size()

            grouped_rating_by_beer = BA_state[['rating', 'beer_id']].groupby('beer_id')
            #Compute the max stability threshold
            max_stability_threshold = calculate_max_stability_threshold_on_all_beers(grouped_rating_by_beer, 0.05, 10)
            # compute the score for each beer
            score = R * logarithmic(N,max_stability_threshold)

            # adding the score to ratings dataframe
            BA_state['preference_score'] = BA_state['beer_id'].map(score)

        #If we want to keep only sufficiently rated beers
        if filter:
            # keep the beer if it has at least 10 ratings
            BA_state = beers_with_n_reviews(BA_state,10,proportioned_n=False)

        #Create the top of the state, depending on the value we compare
        if preference_score:
            topm_state = BA_state[['beer_name', 'beer_style', 'breweries_location', 'preference_score']].groupby(['beer_style']).agg({'preference_score': metric}).sort_values('preference_score', ascending = False)
            
        else:
            #Take the topm beer styles depending on ratings for each state
            topm_state = BA_state[['beer_name', 'beer_style', 'breweries_location', 'rating']].groupby(['beer_style']).agg({'rating': metric}).sort_values('rating', ascending = False)

        if styles:
            # check that every style has ratings on it, else add it with None for the mean ratings
            for style in styles:
                if style in topm_state.index:
                    pass
                else:
                    topm_state.loc[style] = None
            topm_state = pd.concat([topm_state.head(top_m_beer), topm_state.loc[styles]])#(has duplicates that will be removed)

            #Insert top m beer styles + other styles in the df
            pd_topm_republican[state] = topm_state.index
            # add ratings of each beer_styles
            if preference_score:
                pd_topm_republican[state + '_'+fct] = topm_state['preference_score'].values 
            else:
                pd_topm_republican[state + '_'+fct] = topm_state['rating'].values 

        else:
            #Insert top m beer styles in the df
            pd_topm_republican[state] = topm_state[:top_m_beer].index

    return pd_topm_republican,pd_topm_democrat

def create_df_for_abv(df_usa,topn_republican,topn_democrat,top_m_beer,filter=True):
    
    #Democrats States
    pd_top_democrat_abv = pd.DataFrame({'Top '+ str(top_m_beer):np.arange(1, top_m_beer+1)})

    for state in topn_democrat:
        BA_state = df_usa.copy()[df_usa['user_state'] == str(state)]
        if filter:
            # keep the beer if it has at leat 10 ratings
            counts = BA_state.groupby('beer_id')['rating'].transform('count')
            BA_state = BA_state[counts >= 10]

        #Drop rows if missing values on beer_abv
        BA_state = BA_state.dropna(axis = 0,subset = ['beer_abv'])
        top_state_abv = BA_state[['beer_name', 'beer_style', 'beer_abv', 'rating']].groupby(['beer_name']).agg({'rating': 'mean', 'beer_abv': 'first'}).sort_values('rating', ascending = False)[:top_m_beer]
        #add beer names
        pd_top_democrat_abv[state] = top_state_abv.index
        pd_top_democrat_abv[state + '_abv'] = top_state_abv['beer_abv'].values #add avg of beer_name


    #Republican States
    pd_top_republican_abv = pd.DataFrame({'Top '+ str(top_m_beer):np.arange(1, top_m_beer+1)})
    
    for state in topn_republican:
        BA_state = df_usa.copy()[df_usa['user_state'] == str(state)]
        if filter:
            # keep the beer if it has at leat 10 ratings
            counts = BA_state.groupby('beer_id')['rating'].transform('count')
            BA_state = BA_state[counts >= 10]
        #Drop rows if missing values on beer_abv
        BA_state = BA_state.dropna(axis = 0,subset = ['beer_abv'])
        top_state_abv = BA_state[['beer_name', 'beer_style', 'beer_abv', 'rating']].groupby(['beer_name']).agg({'rating': 'mean','beer_abv': 'first'}).sort_values('rating', ascending = False)[:top_m_beer]
        #add beer names
        pd_top_republican_abv[state] = top_state_abv.index
        pd_top_republican_abv[state + '_abv'] = top_state_abv['beer_abv'].values #add avg of beer_name

    return pd_top_republican_abv,pd_top_democrat_abv

def create_df_combined_for_plot(df_republican,df_democrat,topn_republican,topn_democrat,list_rep_states,list_dem_states,str_case='Rating'):
    if str_case not in ['Rating','Count','Beer abv','Pscore']:
        print('str_case must be in :"Rating","Count", "Beer abv","Pscore"')
        return None
    # new long format to plot
    republican_long = pd.melt(df_republican, id_vars = [df_republican.columns[0]], value_vars = topn_republican, var_name = 'State', value_name = 'Beer style')
    democrat_long = pd.melt(df_democrat, id_vars = [df_democrat.columns[0]], value_vars = topn_democrat, var_name = 'State', value_name = 'Beer style')

    # create a new column Count
    republican_long[str_case] = pd.melt(df_republican, id_vars = [df_republican.columns[0]], value_vars = list_rep_states, var_name = 'State_rating', value_name = 'Count of rating')['Count of rating']
    democrat_long[str_case] = pd.melt(df_democrat, id_vars = [df_democrat.columns[0]], value_vars = list_dem_states, var_name = 'State_rating', value_name = 'Count of rating')['Count of rating']

    # add column 'state type'
    republican_long['State type'] = 'Republican'
    democrat_long['State type'] = 'Democrat'


    # combine the dfs
    df_combined = pd.concat([republican_long, democrat_long])
    if str_case=='Rating' or str_case=='Count' or str_case=='Pscore':
        df_combined = df_combined.drop_duplicates(subset = ('State', 'Beer style'))
    else:
        df_combined = df_combined.rename(columns={'Beer style': 'Beer name'})

    return df_combined

def special_year_df(df,year):
    """funtion that returns a sub df of the df with only reviews from the year(s) chosen"""
    if type(year) != list:
        raise ValueError('Error: year should be a list !')
    
    sub_df = pd.DataFrame({})
    for y in year:
        y = str(y)
        sub_df = pd.concat((sub_df,df.loc[df['rating_date'].str.contains(y)].copy()),ignore_index=True)
    
    return sub_df
