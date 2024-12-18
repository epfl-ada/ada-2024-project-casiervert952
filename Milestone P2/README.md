# README - Milestone P2 - CasierVert952

## 1. The project

### 1.1 Title 
Red, Blue, and Brew: How Politics Pours into Beer Preferences in the US

### 1.2 Description
In these modern times, it might be very easy to fall in the trap of certain stereotypes. Indeed, we know that people often take their personal beliefs and values, often linked to their political orientation, with them wherever they go. Thus, one could think for example that a Republican would prefer a strong, dark beer from ‘back home’, while a Democrat might prefer a lighter, more complex-tasting beer and that they wouldn’t care where it comes from. Our aim here will be to see whether these stereotypes are well-founded and to potentially debunk them.

To do this, we will compare two large datasets of beer reviews from two major beer review sites with the voting results for each state in the US presidential elections, from 2000 to 2020. By examining the data, our aim is to understand whether political trends can have a subtle impact on the way beer lovers choose and criticise their favourite beverages.


### 1.3 Research Questions
Thus, during this project we would like to answer these possible questions :

*Q1* : To what extent does a state’s political orientation (Democrat or Republican) influence beer ratings by consumption type - whether the beer is from a local (in state), a national (US), or a foreign brewery (International)?

*Q2* : Are certain beer styles or are there typical beer characteristics that get rated more favorably in Republican or Democrat-leaning states? 

*Q3* : Are certain words (excluding commonly used words) more frequently used in reviews and brewery names in Democrat versus Republican states?

*Q4* : How do preferences for beer differ among supporters of the smaller parties like the Green Party ?

*Q5* : To what extent are common stereotypes about beer preferences accurate? For example, do certain political or regional groups truly prefer specific types of beer or do the data reveal that these assumptions are largely unfounded?


### 1.4 Additional datasets

External dataset about constituency (state-level) returns for elections to the U.S. presidency from 1976 to 2020 coming from :

- [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX)

This dataset contains the statistics of the US presidential elections, published by the Clerk of the United States House of Representatives. Its data is organised to contain, among other: The year of the election, the state, the candidate's names, the party names detailed (exact party name) and simplified (DEMOCRAT, REPUBLICAN, LIBERTARIAN, or OTHER). In addition, for each candidate and state, the votes for the candidate are provided, along to the total cast votes of each state. This dataset's source is robust and reliable and the size of the dataset is small (50 states, 2-4 candidates by state, over 11 elections).

The data will first be filtered to only include election year's that match our beer review dataset, and the results expanded to reflect the state percentage by party. 

### 1.5 Methods and timeline

#### Part 1 : Make one with the Beer data
*Step 1: Preparing the data*

The available data were in different forms. The datasets on beer, brewery and users were in CSV, while ratings were in a multiple-lines TXT format. So we change them to regular CSV format.

*Step 2: Building the the full and cleaned dataset*

For easier work with data later on, we did merge of all datasets into one Dataframe for each website. Then, we saved both into new CSV files called BA_cleaned.csv and RB_cleaned.csv.

*Step 3 : Visualize and examining the data*

To be able to perform proper analysis and additionnal cleanups, we looked at the data from various angles, like the country representation, the distribution over time or the distribution over users.

*Step 4: Exploring Each Dataset*

After examination, we removed unwanted columns that won’t be used.


#### Part 2 : Make one with the external Politics dataset
*Step 1 : Prepare data*

Additionnal information was added from the already present data and dataframes were created.

*Step 2 : Visualize this external dataset*

See which states are more Democratic and which ones are more Republican.

#### Part 3 : First look into the questions / Observe initial trends
*Step 1 : Local vs National vs Foreign consumption*

Compute US states' prefered consumption type.

*Step 2 : Beer style vs Politics*
    
The goal here was to enhance a trend in the beer styles depending on the political side of the states. The first result we had was a table showing the top 5 beer style by state. This table shows interesting result, like a strong attract to the beer style "Gueuze" in the democrat states, while the republican ones prefer more "Quadrupel" and "American Double/Imperial Stout" styles. We plotted the results of this table too, using a weighted count to add more weight to a top1 beer than to a top5 beer. Then, we plotted these results in a bar plot with the beer styles and their mean rating for republican states and for democrat states. The beer styles shown are the top 5 beer styles for each state. Because we don't see a clear difference between the democrat and republican states, we conclude that this plot hides the previous found trend because it doesn't distinguish the 1st from the 5th best beer style. The second plot shows the popularity i.e number of reviews, versus the beer styles and points out that the popularity in beer styles doesn't change that much across the country. The only visible difference between republican and democrat states is for the "American Double/Imperial IPA".
    

*Step 3 : ABV vs Politics*
    
After having analyzed the favorite beer styles for different states, we wanted to see which of the republican or democrat states prefer "stronger" beers, with a higher abv. So our last plot is the beer abv in function of the states top 5 beers abv mean. It displays the median of republican and democrat states too, where we observe a significant higher median (+2.0%) for the republican states. We decided to plot the median instead of the mean because democrat and republican states have extreme values.
    
#### Part 4 : Deeper dive into the questions

*Step 1 : Q1 & Q2*

Plot graphs for Q1 to compare it with US Politics and for Q2 plot other beer characteristics with the political orientation of the 50 states.
    
*Step 2 : Q3*

In order to start answering this question, it will be necessary to tokenize the reviews, and discard tokens related to common works. In addition, the tokenized treated review will be grouped by state, normalized (to account any difference in review Numbers by state) and displayed on an histogram, focusing first on the top 5 most democrat-tendent states and the top 5 most republican states. Depending on the result, some additional dive into the data (e.g by slicing into elections periods) will be required and the results compared with the other states. That plan is subject to change, depending on the results of the first step of analysis, if any unexpected result appear.


*Step 3 : Q4*

In order to answer this question, we need to evaluate for each state the results of the smallest parties, from the election results dataset. Then, for different types of beers, we will look for potential correlation with these. Map libraries for python (e.g folium) can be used for better illustration and analysis of the results.


#### Part 5: Datastory and website

*Step 1 : Analysis & Datastory*

Answer to Q5 and create the datastory.

*Step 2 : Website*

Create a website to show the datastory.

**This part is still to be detailed later.**


#### Proposed timeline :
15.11.2024 : Part 1 and 2

29.11.2024 : Homework 2

08.12.2024 : Part 4 (Step 1 to 4)

12.12.2024 : Part 5 (Step 1 & 2)

20.12.2024 : Deadline Milestone 3


#### Organization within the team
Alberto : Step 4.3 & 4.4

Daniel : Step 4.1

Fabian : Step 5.2

Samuel : Step 4.1

Vincent : Step 5.1


#### Questions for TA 

Do you think that we went too large on the number of questions we want to answer or is it fine like this?
